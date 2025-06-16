import requests
import PyPDF2
import io
import re
from urllib.parse import urlparse
import os
from datetime import datetime
import math

class ClaudeFriendlyPaperSummarizer:
    def __init__(self):
        # Very conservative token limits for Claude
        self.max_tokens_per_chunk = 50000   # ~50k tokens to be very safe
        self.chars_per_token = 4  # Rough estimate
        self.max_chars_per_chunk = self.max_tokens_per_chunk * self.chars_per_token  # 200k chars
        
        self.ai_prompts = {
            "general_summary": """Please summarize this research paper section in simple, easy-to-understand English. Focus on:

1. What the researchers were trying to find out
2. How they did their research (keep it simple)
3. What they discovered
4. Why this matters

Use everyday language and avoid jargon. Explain like you're talking to a curious friend without a science background.

Paper section:
""",
            
            "eli5_summary": """Explain this research paper section like I'm 5 years old. Use simple words and short sentences. Focus on:

- What problem were the scientists trying to solve?
- What did they do?
- What cool thing did they find?
- Why should we care?

Paper section:
""",
            
            "key_insights": """Extract the most important insights from this research paper section and explain each in plain English:

1. State the finding clearly
2. Explain why it's important
3. Describe what it means for the real world

Avoid jargon and focus on practical implications.

Paper section:
""",
            
            "methodology_explained": """Explain the research methods in this section using simple terms:

1. What kind of study/experiment was this?
2. What tools did they use?
3. How did they collect data?
4. What made their approach reliable?

Use analogies where helpful.

Paper section:
""",
            
            "implications_future": """Based on this research section, explain in simple English:

1. What are the implications of these findings?
2. How might this change our understanding?
3. What questions does this raise?
4. How might this impact society or technology?

Focus on the bigger picture.

Paper section:
"""
        }
    
    def get_pdf_content(self, source):
        """Get PDF content from URL or local file"""
        if self.is_local_file(source):
            return self.read_local_pdf(source)
        else:
            return self.download_pdf(source)
    
    def is_local_file(self, source):
        """Check if source is a local file path"""
        return os.path.exists(source) or (not source.startswith(('http://', 'https://')) and '.' in source)
    
    def read_local_pdf(self, file_path):
        """Read PDF from local file"""
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            
            with open(file_path, 'rb') as file:
                return file.read()
        except Exception as e:
            raise Exception(f"Failed to read local PDF: {e}")
    
    def download_pdf(self, url):
        """Download PDF from URL"""
        try:
            response = requests.get(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            raise Exception(f"Failed to download PDF: {e}")
    
    def extract_text_from_pdf(self, pdf_content):
        """Extract text from PDF content"""
        try:
            pdf_file = io.BytesIO(pdf_content)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            
            return text
        except Exception as e:
            raise Exception(f"Failed to extract text from PDF: {e}")
    
    def clean_text(self, text):
        """Clean and format extracted text"""
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r'\(Fig\.?\s*\d+[a-z]?\)', '', text)
        text = re.sub(r'\(Table\s*\d+\)', '', text)
        return text.strip()
    
    def split_text_intelligently(self, text):
        """Split text into smaller, Claude-safe chunks at logical breakpoints"""
        # More aggressive chunking - aim for ~30k chars max per chunk
        target_chunk_size = 30000  # Much smaller target
        
        chunks = []
        current_chunk = ""
        
        # First try to split by major sections
        section_breaks = re.split(r'(\n\s*(?:Abstract|Introduction|Methods|Results|Discussion|Conclusion|References)\s*\n)', text, flags=re.IGNORECASE)
        
        if len(section_breaks) > 3:  # If we found section breaks
            sections = []
            for i in range(0, len(section_breaks), 2):
                if i + 1 < len(section_breaks):
                    sections.append(section_breaks[i] + section_breaks[i + 1])
                else:
                    sections.append(section_breaks[i])
            
            for section in sections:
                if len(current_chunk) + len(section) > target_chunk_size and current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = section
                else:
                    current_chunk += section
        else:
            # Fall back to paragraph splitting
            paragraphs = text.split('\n\n')
            
            for paragraph in paragraphs:
                test_chunk = current_chunk + "\n\n" + paragraph if current_chunk else paragraph
                
                if len(test_chunk) > target_chunk_size and current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = paragraph
                else:
                    current_chunk = test_chunk
        
        # Add the last chunk
        if current_chunk.strip():
            chunks.append(current_chunk.strip())
        
        # Further split any chunks that are still too large
        final_chunks = []
        for chunk in chunks:
            if len(chunk) > target_chunk_size:
                # Split long chunks by sentences
                sentences = re.split(r'(?<=[.!?])\s+', chunk)
                temp_chunk = ""
                
                for sentence in sentences:
                    if len(temp_chunk) + len(sentence) > target_chunk_size and temp_chunk:
                        final_chunks.append(temp_chunk.strip())
                        temp_chunk = sentence
                    else:
                        temp_chunk += " " + sentence if temp_chunk else sentence
                
                if temp_chunk.strip():
                    final_chunks.append(temp_chunk.strip())
            else:
                final_chunks.append(chunk)
        
        return final_chunks
    
    def get_paper_title(self, text):
        """Extract paper title from text"""
        first_lines = text.split('\n')[:10]
        for line in first_lines:
            line = line.strip()
            if 20 < len(line) < 150 and not line.isupper():
                return line
        return "Research Paper"
    
    def create_chunk_files(self, paper_text, source, base_filename):
        """Create separate files for each chunk and prompt type"""
        
        title = self.get_paper_title(paper_text)
        text_chunks = self.split_text_intelligently(paper_text)
        
        # Create output directory
        output_dir = f"{base_filename}_chunks"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        created_files = []
        
        # Determine source type for display
        source_type = "Local file" if self.is_local_file(source) else "URL"
        source_display = os.path.basename(source) if self.is_local_file(source) else source
        
        # Create index file
        index_content = f"""# Paper Summary Chunks - Index
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Paper: {title}
# Source: {source_display} ({source_type})
# Total chunks: {len(text_chunks)}

## How to Use These Files

This paper has been split into {len(text_chunks)} Claude-friendly chunks. Each chunk has 5 prompt files:

- `chunk_N_general.txt` - General summary prompt
- `chunk_N_eli5.txt` - Explain like I'm 5 prompt  
- `chunk_N_insights.txt` - Key insights prompt
- `chunk_N_methods.txt` - Methodology prompt
- `chunk_N_implications.txt` - Implications prompt

## Recommended Workflow

1. Start with chunk 1, general summary
2. Process chunks in order for complete understanding
3. Use different prompt types based on your needs
4. Combine insights from all chunks for full picture

## File List
"""
        
        # Create files for each chunk and prompt type
        for i, chunk in enumerate(text_chunks, 1):
            chunk_info = f"\n### Chunk {i} ({len(chunk):,} characters)\n"
            index_content += chunk_info
            
            for prompt_name, prompt_text in self.ai_prompts.items():
                filename = f"chunk_{i:02d}_{prompt_name.replace('_', '')}.txt"
                filepath = os.path.join(output_dir, filename)
                
                content = f"""# CLAUDE PROMPT - CHUNK {i} of {len(text_chunks)}
# Paper: {title}
# Source: {source_display}
# Prompt Type: {prompt_name.replace('_', ' ').title()}
# Chunk Size: {len(chunk):,} characters

{prompt_text}

{chunk}
"""
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                created_files.append(filepath)
                index_content += f"- {filename}\n"
        
        # Save index file
        index_path = os.path.join(output_dir, "00_INDEX.txt")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        created_files.insert(0, index_path)
        return created_files, output_dir
    
    def create_combined_prompts(self, paper_text, paper_url, base_filename):
        """Create combined prompt files (one per prompt type) if paper is small enough"""
        title = self.get_paper_title(paper_text)
        output_dir = f"{base_filename}_combined"
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        created_files = []
        
        for prompt_name, prompt_text in self.ai_prompts.items():
            filename = f"complete_{prompt_name}.txt"
            filepath = os.path.join(output_dir, filename)
            
            content = f"""# CLAUDE PROMPT - COMPLETE PAPER
# Paper: {title}
# Prompt Type: {prompt_name.replace('_', ' ').title()}
# Paper Size: {len(paper_text):,} characters

{prompt_text}

{paper_text}
"""
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            created_files.append(filepath)
        
        return created_files, output_dir

def main():
    paper_url = input("Enter the URL of the Nature paper: ").strip()
    
    if not paper_url:
        print("Please provide a valid URL")
        return
    
    # Create base filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    base_filename = f"paper_{timestamp}"
    
    summarizer = ClaudeFriendlyPaperSummarizer()
    
    try:
        print("📥 Downloading PDF...")
        pdf_content = summarizer.download_pdf(paper_url)
        
        print("📄 Extracting text from PDF...")
        paper_text = summarizer.extract_text_from_pdf(pdf_content)
        
        print("🧹 Cleaning and formatting text...")
        clean_text = summarizer.clean_text(paper_text)
        
        paper_size = len(clean_text)
        print(f"📊 Paper size: {paper_size:,} characters")
        
        # Always chunk papers for Claude safety - even small ones
        print("📂 Creating chunked files for Claude compatibility...")
        created_files, output_dir = summarizer.create_chunk_files(clean_text, paper_url, base_filename)
        
        num_chunks = len([f for f in created_files if 'chunk_' in f]) // 5  # 5 prompts per chunk
        print(f"✅ Split into {num_chunks} chunks, created {len(created_files)} files in: {output_dir}/")
        print(f"📋 Start with: {output_dir}/00_INDEX.txt")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n🔧 Troubleshooting tips:")
        print("1. Ensure URL points to accessible PDF")
        print("2. Check internet connection")
        print("3. Some papers may be behind paywalls")

def batch_process_urls(urls):
    """Process multiple papers with chunking"""
    summarizer = ClaudeFriendlyPaperSummarizer()
    results = []
    
    for i, url in enumerate(urls, 1):
        try:
            print(f"\n📄 Processing paper {i}/{len(urls)}")
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            base_filename = f"batch_paper_{i}_{timestamp}"
            
            pdf_content = summarizer.download_pdf(url)
            paper_text = summarizer.extract_text_from_pdf(pdf_content)
            clean_text = summarizer.clean_text(paper_text)
            
            if len(clean_text) > summarizer.max_chars_per_chunk:
                files, output_dir = summarizer.create_chunk_files(clean_text, url, base_filename)
            else:
                files, output_dir = summarizer.create_combined_prompts(clean_text, url, base_filename)
            
            results.append({"url": url, "files": files, "directory": output_dir, "status": "success"})
            
        except Exception as e:
            results.append({"url": url, "files": [], "directory": None, "status": f"error: {e}"})
    
    return results

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Command line mode
        if sys.argv[1] == "--folder":
            if len(sys.argv) > 2:
                process_folder(sys.argv[2])
            else:
                print("❌ Please provide folder path: python script.py --folder /path/to/pdfs")
        elif sys.argv[1] == "--interactive":
            interactive_mode()
        else:
            # Assume it's a file path or URL
            source = sys.argv[1]
            # Quick single file processing
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            if source.startswith(('http://', 'https://')):
                base_filename = f"paper_{timestamp}"
            else:
                filename_base = os.path.splitext(os.path.basename(source))[0]
                base_filename = f"{filename_base}_{timestamp}"
            
            summarizer = ClaudeFriendlyPaperSummarizer()
            try:
                pdf_content = summarizer.get_pdf_content(source)
                paper_text = summarizer.extract_text_from_pdf(pdf_content)
                clean_text = summarizer.clean_text(paper_text)
                files, output_dir = summarizer.create_chunk_files(clean_text, source, base_filename)
                print(f"✅ Processed: {output_dir}")
            except Exception as e:
                print(f"❌ Error: {e}")
    else:
        # Interactive mode by default
        main()
