# First Steps with NMRPipe

This guide prepares you for your first NMRPipe session: moving around the terminal, 
downloading processing scripts, converting raw Bruker data, and looking at your first spectrum.

> **Before you start:** NMRPipe usually runs on Linux (or macOS with a working installation). The commands below assume NMRPipe is already installed on your computer or on the lab server. If `nmrDraw` is not found, ask your supervisor to check the NMRPipe setup.

---

## 1. Navigation Refresher

| Command | Description | Example |
|---------|-------------|---------|
| `pwd` | Print the current directory ("where am I?") | `pwd` |
| `ls` | List files in the current directory | `ls` |
| `ls -l` | List files with details (size, date, permissions) | `ls -l` |

### The Tab key is your best friend

Pressing **Tab** while typing a path or filename autocompletes it. If several options match, pressing **Tab twice** shows all of them.

```
cd my_exp<TAB>        # completes to my_experiment/ if it is unique
cd 1<TAB><TAB>        # shows all folders starting with "1"
```

Bruker data folders have names like `1`, `2`, `3`, ... Tab completion saves a lot of typing and prevents typos.

---

## 2. Copying Whole Folders: `cp -r`

Never process your data in the original folder. Always work on a copy.

```
cp -r original_data/ my_processing/
```

The `-r` flag means *recursive*: it copies the folder **and everything inside it**. Without `-r`, `cp` refuses to copy folders.

---

## 3. Downloading the Scripts: `wget`

`wget` downloads a file from the internet directly into your current directory. We use it to get the processing scripts from the course GitHub repository:

```
wget https://raw.githubusercontent.com/yurayura-nmr/nmrpipe-scripts/main/fidft_hqsc.com
```

> **Note:** Use the **raw** file link (`raw.githubusercontent.com/...`), not the normal GitHub page link. Otherwise you will download an HTML web page instead of the script.

Check that the file arrived:

```
ls
```

---

## 4. Making the Script Executable: `chmod +x`

A freshly downloaded script is just a text file. To run it as a program you must give it permission:

```
chmod +x fidft_hqsc.com
```

Check with `ls -l`. The permissions should now contain an `x`, for example `-rwxr-xr-x`.

---

## 5. The tcsh Shell

NMRPipe scripts are written for the **tcsh** shell (a relative of csh), not for bash or zsh. Start it by typing:

```
tcsh
```

Your prompt may change slightly. Stay in this shell for the rest of the NMRPipe session. To leave it, type `exit`.

---

## 6. Converting Bruker Data: `bruker`

Your spectrometer saves raw data in Bruker format. NMRPipe needs to convert it first. The `bruker` command opens a small graphical tool that reads the experiment parameters and **generates a conversion script** called `fid.com`.

1. Go into your Bruker experiment folder (the one containing the files `fid` or `ser`, and `acqus`):

   ```
   cd my_processing/1/
   ls
   ```

2. Start the converter:

   ```
   bruker
   ```

3. Check that the parameters shown (spectral widths, number of points, etc.) look reasonable, then save. This writes `fid.com` into the folder.

4. Look at the result:

   ```
   ls
   ```

   You should now see `fid.com` next to your raw data.

---

## 7. Putting `fid.com` into the Processing Script: `gedit`

`fid.com` only converts the data. The full processing script (`fidft_hqsc.com`) converts **and** Fourier transforms it. We combine the two by copying the conversion part into our full script.

1. Open both files in the text editor:

   ```
   gedit fid.com &
   gedit fidft_hqsc.com &
   ```

   (The `&` keeps the terminal free while the editor is open.)

2. In `fid.com`, select the conversion commands (the block starting with `bruk2pipe` and ending before the `-ov -out ...` line, including its parameters) and copy them with **Ctrl+C**.

3. In `fidft_hqsc.com`, find the marked section for the conversion step and paste with **Ctrl+V**, replacing the placeholder text.

4. Save the file (**Ctrl+S**) and close the editors.

> Only copy the part the script tells you to replace. Do not delete the Fourier transform commands that follow.

---

## 8. Running the Script

Make sure you are in the experiment folder and in the tcsh shell, then run:

```
./fidft_hqsc.com
```

The `./` means "run the file that is in *this* directory". If it works, new files appear (use `ls`), for example a processed spectrum with the ending `.ft2`.

If you get `Permission denied`, you forgot `chmod +x` (step 4). If you get `command not found`, you probably forgot the `./`.

---

## 9. Looking at Your Spectrum: `nmrDraw`

Open the NMRPipe viewer:

```
nmrDraw &
```

In the window that opens, load your processed spectrum (the `.ft2` file) via the file menu. You should see your first 2D spectrum.

---

## Summary of Commands

| Command | Purpose |
|---------|---------|
| `pwd`, `ls` | Where am I, what is here |
| `<Tab>` | Autocomplete paths and filenames, show options |
| `cp -r` | Copy a whole folder |
| `wget` | Download the scripts from GitHub |
| `chmod +x` | Make a script executable |
| `tcsh` | Start the shell NMRPipe scripts need |
| `bruker` | Convert Bruker data, generates `fid.com` |
| `gedit` | Copy `fid.com` into the full processing script |
| `./fidft_hqsc.com` | Run the processing script |
| `nmrDraw` | Display the spectrum |

