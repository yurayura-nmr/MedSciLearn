# 🔬 Nature etc. Paper Summarizer - Claude Edition

A Python tool that downloads research papers and creates Claude-optimized prompts for easy-to-understand summaries. Perfect for making complex scientific papers accessible to everyone!

## ✨ Features

- **📥 Dual Input Support**: Works with both URLs and local PDF files
- **🧩 Smart Chunking**: Automatically splits large papers into Claude-friendly chunks (~30k characters each)
- **📝 Multiple Summary Types**: 5 different AI prompts for various summary needs
- **📁 Batch Processing**: Process entire folders of PDFs at once
- **🎯 Claude-Optimized**: Each output file is guaranteed to fit within Claude's context limits
- **📋 Organized Output**: Clean file structure with index and clear naming

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
pip install requests PyPDF2
```

### Basic Usage

```bash
# Interactive mode (recommended for beginners)
python paper_summarizer.py

# Single file processing
python paper_summarizer.py ./research_paper.pdf
python paper_summarizer.py "https://www.nature.com/articles/s41586-025-09152-2.pdf"

# Process entire folder
python paper_summarizer.py --folder ./pdf_directory

# Interactive menu mode
python paper_summarizer.py --interactive
```

## 📖 How It Works

### 1. Input Processing
The script accepts:
- **URLs**: Direct links to PDF papers (Nature, arXiv, etc.)
- **Local Files**: PDF files on your computer
- **Folders**: Batch process multiple PDFs

### 2. Smart Chunking
Large papers are intelligently split at:
- Section boundaries (Abstract, Introduction, Methods, etc.)
- Paragraph breaks
- Sentence boundaries (if needed)
- Maximum ~30k characters per chunk for Claude compatibility

### 3. AI Prompt Generation
Creates 5 specialized prompts for each chunk:

| Prompt Type | Description | Best For |
|-------------|-------------|----------|
| **General Summary** | Comprehensive overview in plain English | Overall understanding |
| **ELI5** | Explain Like I'm 5 - ultra-simple language | Teaching others |
| **Key Insights** | Main findings and their importance | Quick highlights |
| **Methodology** | How the research was conducted | Understanding methods |
| **Implications** | Future impact and significance | Big picture thinking |

## 📁 Output Structure

```
paper_20241216_143052_chunks/
├── 00_INDEX.txt                    # Start here - overview and instructions
├── chunk_01_general.txt            # Chunk 1 - General summary prompt
├── chunk_01_eli5.txt               # Chunk 1 - ELI5 prompt
├── chunk_01_insights.txt           # Chunk 1 - Key insights prompt
├── chunk_01_methods.txt            # Chunk 1 - Methodology prompt
├── chunk_01_implications.txt       # Chunk 1 - Implications prompt
├── chunk_02_general.txt            # Chunk 2 - General summary prompt
└── ... (continues for all chunks)
```

## 🎯 Usage Examples

### Example 1: Nature Paper URL
```bash
python paper_summarizer.py "https://www.nature.com/articles/s41586-025-09152-2.pdf"
```

**Output**: Creates folder `paper_20241216_143052_chunks/` with chunked prompts

### Example 2: Local PDF File
```bash
python paper_summarizer.py "./research/climate_study.pdf"
```

**Output**: Creates folder `climate_study_20241216_143052_chunks/`

### Example 3: Batch Processing
```bash
python paper_summarizer.py --folder "./research_papers/"
```

**Output**: Creates `batch_summaries/` folder with subfolders for each paper

## 🔧 Advanced Usage

### Command Line Options

```bash
# Process single file/URL
python paper_summarizer.py <path_or_url>

# Batch process folder
python paper_summarizer.py --folder <folder_path>

# Interactive menu
python paper_summarizer.py --interactive

# Default interactive mode
python paper_summarizer.py
```

### Programmatic Usage

```python
from paper_summarizer import ClaudeFriendlyPaperSummarizer

# Initialize
summarizer = ClaudeFriendlyPaperSummarizer()

# Process single paper
pdf_content = summarizer.get_pdf_content("./paper.pdf")
text = summarizer.extract_text_from_pdf(pdf_content)
clean_text = summarizer.clean_text(text)
files, output_dir = summarizer.create_chunk_files(clean_text, "./paper.pdf", "my_paper")

# Batch process
from paper_summarizer import process_folder
results = process_folder("./pdf_folder/")
```

## 📝 Using the Generated Prompts

1. **Open the output folder** and start with `00_INDEX.txt`
2. **Choose a chunk** (start with chunk 1 for sequential reading)
3. **Pick a prompt type** based on your needs
4. **Copy the entire file content** and paste into Claude
5. **Get your summary!** Claude will provide the requested analysis

### Pro Tips:
- Process chunks **sequentially** for complete understanding
- Use **General Summary** first, then specialized prompts
- **Combine insights** from multiple chunks for full picture
- Save Claude's responses to build a complete summary

## 🛠️ Requirements

- **Python 3.6+**
- **PyPDF2**: PDF text extraction
- **requests**: URL downloading
- **Internet connection**: For URL-based papers

## 📋 Installation Details

```bash
# Option 1: pip install
pip install requests PyPDF2

# Option 2: requirements.txt
pip install -r requirements.txt

# Option 3: conda
conda install requests
pip install PyPDF2  # PyPDF2 not available in conda
```

## 🔍 Troubleshooting

### Common Issues

**"File not found" Error**
```
✅ Solutions:
- Check file path is correct
- Use absolute paths: C:\Users\Name\file.pdf
- Ensure file exists and is readable
```

**"Failed to download" Error**
```
✅ Solutions:
- Check internet connection
- Verify URL is accessible
- Some papers may be behind paywalls
- Try direct PDF links
```

**"Claude rejects file as too big"**
```
✅ This shouldn't happen anymore! But if it does:
- The script should auto-chunk to ~30k chars
- Try processing again
- Check if PDF extraction worked properly
```

**PyPDF2 Issues**
```
✅ Solutions:
- Update PyPDF2: pip install --upgrade PyPDF2
- Some PDFs have extraction issues - try different papers
- Scan-based PDFs won't work (need OCR)
```

## 🤝 Contributing

Contributions welcome! Areas for improvement:

- **OCR Support**: Handle scanned PDFs
- **More Formats**: Support DOCX, HTML papers
- **Custom Prompts**: User-defined prompt templates
- **GUI Interface**: Simple drag-and-drop interface
- **Citation Extraction**: Automatically extract and format citations

## 📄 License

MIT License - feel free to use and modify!

## 🙋 FAQ

**Q: Does this work with arXiv papers?**
A: Yes! Works with any publicly accessible PDF URL.

**Q: Can I customize the prompts?**
A: Yes! Edit the `ai_prompts` dictionary in the script.

**Q: What about paywalled papers?**
A: The script can't access papers behind paywalls. Use local PDF files instead.

**Q: Does this work with other AI models?**
A: The prompts work with ChatGPT, Gemini, and other AI assistants too!

**Q: Can I process non-English papers?**
A: Yes, but the prompts are in English. The AI will handle translation.

## 🌟 Star History

If this tool helped you understand research papers better, consider giving it a star! ⭐

---

**Made with ❤️ for researchers, students, and curious minds everywhere**
