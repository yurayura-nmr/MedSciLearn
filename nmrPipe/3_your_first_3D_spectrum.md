# Processing a 3D HNCO with NMRPipe

So far you have processed a 2D HSQC. In this lesson we move to a **3D HNCO**. The workflow is the same idea as before, but the processing is split into **two scripts**:

| Script | Purpose |
|--------|---------|
| `fid_hnco.com` | Converts the raw Bruker data into NMRPipe format |
| `ft_hnco.com` | Fourier transforms the converted data |

In this first part of the lesson we download both scripts and adapt the conversion script to **your** experiment.

> **Before you start:** Work on a copy of your data (`cp -r`, see Lesson 1) and make sure you are in the `tcsh` shell.

---

## 1. Download the Scripts: `wget`

Go into your HNCO experiment folder (the one containing `ser` and `acqus`) and download both scripts from the course GitHub repository:

```
wget https://raw.githubusercontent.com/yurayura-nmr/nmrpipe-scripts/main/co/hnco/fid_hnco.com
wget https://raw.githubusercontent.com/yurayura-nmr/nmrpipe-scripts/main/co/hnco/ft_hnco.com
```

> **Note:** As before, use the **raw** link (`raw.githubusercontent.com/...`), not the normal GitHub page link.

Check that both files arrived:

```
ls
```

Make them executable:

```
chmod +x fid_hnco.com ft_hnco.com
```

Check with `ls -l`. Both files should now have an `x` in their permissions.

---

## 2. Read the Experiment Parameters: `bruker`

Just like in Lesson 1, we let the `bruker` tool read the experiment parameters for us.

```
bruker
```

Check that the parameters shown (spectral widths, number of points, etc.) look reasonable for **all three dimensions**, then save. This writes `fid.com` into the folder.

> You will not run this `fid.com` directly. We only use it as a source of the correct parameters for your experiment.

### Tip: Ctrl+Z and `bg`

Programs like `bruker` and `nd` (`nmrDraw`) keep your terminal busy while they are open. If you press **Ctrl+Z** to get your prompt back, the program is only **suspended**: its window stays open, but it is **frozen and unresponsive**.

To let it continue running in the background, type:

```
bg
```

and press **Enter**. The window becomes responsive again and your terminal is free.

> To avoid this, you can start a program in the background from the beginning by adding `&` (for example `bruker &` or `nd &`).

---

## 3. Adapt `fid_hnco.com` to Your Experiment

Open both files in the editor:

```
gedit fid.com &
gedit fid_hnco.com &
```

Copy the conversion block from `fid.com` (the `bruk2pipe` command with your spectral widths, number of points, etc.) into the marked section of `fid_hnco.com`, replacing the placeholder text, as you did with `fidft_hqsc.com` in Lesson 1.

Save with **Ctrl+S** and close the editors.

> Only replace the part the script tells you to replace. Keep the rest of the script as it is.

**Verify your edit.** Print the script and check that your changes really went in:

```
cat fid_hnco.com
```

You should see the `bruk2pipe` block with your own parameters. If you still see the placeholder text, you probably forgot to save in `gedit` (**Ctrl+S**).

---

## Summary of Commands

| Command | Purpose |
|---------|---------|
| `wget` | Download `fid_hnco.com` and `ft_hnco.com` |
| `chmod +x` | Make both scripts executable |
| `bruker` | Read the experiment parameters, generates `fid.com` |
| `Ctrl+Z`, then `bg` | Suspend a program, then let it continue in the background |
| `gedit` | Copy the parameters into `fid_hnco.com` |
| `cat` | Check that the edit is really in the script |

**To be continued:** in the next step we run `fid_hnco.com` and then `ft_hnco.com`.
