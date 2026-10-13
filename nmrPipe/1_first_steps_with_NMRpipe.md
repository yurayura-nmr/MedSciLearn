# First Steps with NMRPipe

This guide prepares you for your first NMRPipe session: moving around the terminal, downloading processing scripts, converting raw Bruker data, and looking at your first spectrum.

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

5. **Verify your edit.** Before running anything, print the script in the terminal and check that your changes really went in:

   ```
   cat fidft_hqsc.com
   ```

   You should see the `bruk2pipe` block from `fid.com` (with your own spectral widths and number of points) in the conversion section, followed by the Fourier transform commands. If you still see the placeholder text, or the file looks unchanged, you probably forgot to save in `gedit` (**Ctrl+S**). Go back and repeat the edit.

---

## 8. Optional: Switching on Linear Prediction (Comments in Linux)

In Linux scripts, a line that starts with `#` is a **comment**: the computer ignores it completely. Script authors use this to leave notes, or to keep a command in the file without running it.

```
# this line is a comment and does nothing
-fn LP auto      <- this line is active and will be executed
```

Our processing script contains some commands that are switched off by a `#`. To switch one on, you only have to **remove the `#`** (this is called *uncommenting*).

1. Open the script:

   ```
   gedit fidft_hqsc.com &
   ```

2. Find the lines with `-lb` and `-fn LP auto` (in the processing section for the F1 dimension) and **delete the `#` at the beginning of those lines**. Leave everything else on the line unchanged.

3. Save with **Ctrl+S** and check your edit again:

   ```
   cat fidft_hqsc.com
   ```

**What does this do?** `-fn LP auto` tells NMRPipe to perform **linear prediction** (LP). In an HSQC the F1 dimension (vertical, <sup>15</sup>N) is usually measured with only a small number of increments, because every extra point costs measurement time. LP uses the points that were measured to *predict* additional points. The result is a spectrum with **better resolution in the F1 dimension**, meaning sharper and better separated peaks along the <sup>15</sup>N axis.

> Tip: You can run the script once with and once without the `#` and compare both spectra in `nmrDraw` to see the difference yourself.

---

## 9. Running the Script

Make sure you are in the experiment folder and in the tcsh shell, and that you have checked your edits with `cat` (steps 7 and 8), then run:

```
./fidft_hqsc.com
```

The `./` means "run the file that is in *this* directory". If it works, new files appear (use `ls`), for example a processed spectrum with the ending `.ft2`.

If you get `Permission denied`, you forgot `chmod +x` (step 4). If you get `command not found`, you probably forgot the `./`.

---

## 10. Looking at Your Spectrum: `nmrDraw`

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
| `cat` | Check that your edits are really in the script |
| `#` | Comment: removing it from `-fn LP auto` switches on linear prediction |
| `./fidft_hqsc.com` | Run the processing script |
| `nmrDraw` | Display the spectrum |

**This is the end of the first lesson.** In the next lesson we will look at what the processing script actually does, line by line.
