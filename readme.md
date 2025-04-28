### **Installing Anaconda & Basic Unix Commands**  

This guide will help absolute beginners install Anaconda on macOS and introduce 20 essential Unix commands for file manipulation.

---

## **1. Installing Anaconda on macOS**  

### **Step 1: Download Anaconda**  
1. Open a web browser and go to the official [Anaconda website](https://www.anaconda.com/products/distribution).  
2. Click **Download** and select the macOS version (Apple Silicon or Intel, depending on your Mac). It also works on Windows but the details will differ from here.

### **Step 2: Install Anaconda**  
1. Open the downloaded `.pkg` file.  
2. Follow the on-screen instructions to install Anaconda.  
3. Click **Continue** through the installation steps and allow system changes if prompted.  

### **Step 3: Open Terminal and Verify Installation**  
1. Open **Terminal** (press `Command + Space`, type "Terminal", and hit `Enter`).  
2. Type the following command to verify the installation:  

   ```bash
   conda --version
   ```

   You should see something like:  
   ```
   conda 23.3.1
   ```

### **Step 4: Initialize Conda**  
Run the following command to enable Conda in your terminal:  

```bash
conda init
```

Close and reopen the terminal for the changes to take effect.

---

## **2. Basic Unix Commands for File Manipulation**  

Once you have Anaconda installed, it’s useful to know some basic Unix commands to navigate and manage files in the terminal. These commands can be used directly in the terminal or included in scripts to automate tasks, but they are not considered programming—they are simply instructions for the shell to execute.

### **Navigation Commands**  
| Command | Description | Example |
|---------|------------|---------|
| `pwd` | Print current directory | `pwd` |
| `ls` | List files in the current directory | `ls` |
| `cd <directory>` | Change directory | `cd Documents` |
| `cd ..` | Move up one directory level | `cd ..` |

### **File and Directory Management**  
| Command | Description | Example |
|---------|------------|---------|
| `mkdir <dirname>` | Create a new directory | `mkdir my_project` |
| `rmdir <dirname>` | Remove an empty directory | `rmdir old_folder` |
| `rm <filename>` | Delete a file | `rm oldfile.txt` |
| `rm -r <dirname>` | Delete a directory and its contents | `rm -r my_folder` |
| `cp <source> <destination>` | Copy a file | `cp file.txt backup/` |
| `mv <source> <destination>` | Move or rename a file | `mv oldname.txt newname.txt` |

For more commands, I recommend the excellent "cheat sheet" here: [Cheat sheet](https://upload.wikimedia.org/wikipedia/commons/7/79/Unix_command_cheatsheet.pdf). 
 

### **Running Python Scripts in the Terminal**  
You can run Python scripts directly from the terminal using the following command:

| Command | Description | Example |
|---------|------------|---------|
| `python <script.py>` | Run a Python script | `python my_script.py` |

### **Viewing and Editing Files**  
| Command | Description | Example |
|---------|------------|---------|
| `cat <filename>` | Display file contents | `cat notes.txt` |
| `vi <filename>` | Open a file in vi text editor | `vi script.py` |
| `less <filename>` | View a file one page at a time | `less longfile.txt` |

### **System and Process Commands**  
| Command | Description | Example |
|---------|------------|---------|
| `whoami` | Show the current user | `whoami` |
| `clear` | Clear the terminal screen | `clear` |
| `history` | Show command history | `history` |
| `exit` | Close the terminal | `exit` |

---

The Tab key is extremely useful in the terminal. Pressing Tab while typing a command or filename will autocomplete it if possible. For example:

```bash
cd my_pro<TAB>
```

If there is a folder named my_project, pressing Tab will complete it to:

```bash
cd my_project
```

## **3. Next Steps**  
- Practice using the commands above in the terminal.  
- Explore Anaconda by running `conda list` to see installed packages.  
- Try creating a new Conda environment:  

  ```bash
  conda create --name myenv python=3.9
  ```

You’re now ready to start working with Python in Anaconda on macOS!

Also it is a good idea to download Visual Studio Code for writing our python scripts later.
