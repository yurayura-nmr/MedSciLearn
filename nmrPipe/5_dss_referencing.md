# DSS Referencing: Finding the True 0 ppm

In this lesson we leave the 3D processing for now and process a simple **1D proton spectrum** of **DSS**. DSS is our chemical shift reference. All we need from this lesson is **one number**: the chemical shift of the DSS peak in our spectrum. We will later use this number for all our measurements.

> **Before you start:** You should be in the `tcsh` shell. Stop the 3D work for now (close `nd` if it is still open).

---

## Background: DSS in the Sample

DSS is added to the sample as an internal reference. In our lab:

```
0.2 mM DSS in the sample (stock solution: 100 mM)
For example: 0.7 µl DSS stock solution for 350 µl sample
```

The sharp methyl peak of DSS defines **0 ppm**. Because the measured position of that peak is not exactly at 0.000 ppm in the spectrometer frequency scale, we measure where it really is. From that number, a script later calculates the properly referenced 0 ppm points for <sup>1</sup>H, <sup>15</sup>N and <sup>13</sup>C for any multidimensional experiment (for example HBHAcoNH, <sup>15</sup>N-edited NOESY).

---

## 1. Go to the 1D Experiment Folder

Go to the experiment folder that contains the **1D spectrum of DSS** (remember to work on a copy, `cp -r`, and use the Tab key):

```
cd <your_dss_experiment_folder>
ls
```

You should see the raw data files, such as `fid` and `acqus`.

---

## 2. Download the Processing Script: `wget`

```
wget https://raw.githubusercontent.com/yurayura-nmr/nmrpipe-scripts/main/dss_1d/fidft_dss.com
chmod +x fidft_dss.com
```

> **Note:** As before, use the **raw** link, not the normal GitHub page link.

Check with `ls -l` that the file is there and has an `x` in its permissions.

---

## 3. Read the Experiment Parameters: `bruker`

Just like in Lesson 1:

```
bruker
```

Check that the parameters look reasonable and save. This writes `fid.com` into the folder.

> Remember: if you suspend `bruker` with **Ctrl+Z**, type `bg` and press **Enter**.

---

## 4. Edit the Script

Open both files:

```
gedit fid.com &
gedit fidft_dss.com &
```

In `fidft_dss.com` find the `bruk2pipe` block. It looks like this (the numbers are from our example, **yours will be different**):

```
bruk2pipe -in ./fid \
  -bad 0.0 -noaswap -DMX -decim 16 -dspfvs 12 -grpdly -1  \
  -xN              8192  \
  -xT              4096  \
  -xMODE            DQD  \
  -xSW         9615.385  \
  -xOBS         600.133  \
  -xCAR          4.6729  \
  -xLAB              1H  \
  -ndim               1  \
```

Compare it with the same block in your own `fid.com` and make the lines in `fidft_dss.com` match, especially:

| Line | Meaning |
|------|---------|
| `-xN` | Number of points (total, real + imaginary) |
| `-xT` | Number of complex points |
| `-xSW` | Spectral width in Hz |
| `-xOBS` | Spectrometer frequency in MHz |
| `-xCAR` | Carrier position in ppm |

> **Be careful:** The easiest and safest way is to **change only the numbers**. Do not delete a `\` at the end of a line, do not add spaces after it, and never insert new lines (see the warning in Lesson 3).

Save with **Ctrl+S** and verify:

```
cat fidft_dss.com
```

You should see your own numbers in the `bruk2pipe` block. If you still see the old numbers, you probably forgot to save.

---

## 5. Run the Script

```
./fidft_dss.com
```

If it works, a processed spectrum appears (check with `ls`).

---

## 6. Display and Phase the Spectrum

Open the viewer:

```
nd
```

By default, `nd` tries to read the **FID file**, which is not what we want. Load the processed spectrum instead:

1. Press **Shift+S** (Caps Lock must be off) to open the file selection window.
2. Select **`dss.ft`**.
3. Click **Read/Draw**.

Now check the phase of the peaks.

> **No `h` needed this time:** In Lesson 2 you pressed **`h`** to show a horizontal slice through a 2D spectrum. Our DSS spectrum is already **1D**, so you see the spectrum itself and there is nothing to slice.

Just use the **p0 slider** (drag = large change, click next to it = small change) until **all peaks are in phase**, meaning they have a symmetric, positive, **absorptive lineshape**. Actually, we only need the DSS peak near 0 ppm to be phased (no need to have the protein part phased for now).

Note down the p0 value you found and put it into the first `PS -p0` line of `fidft_dss.com` (change only the number), save, run `./fidft_dss.com` again and recheck. This is the same procedure as in Lesson 2.

---

## 7. Find the DSS Peak

Zoom into the region around **0 ppm** and look for the **sharp peak of DSS**. This is the DSS methyl signal.

To zoom in `nd`:

1. Press **`z`**.
2. **Draw a rectangle** around the region you want to see, using the mouse.
3. **Right-click** the mouse to apply the zoom.
4. Repeat if needed, until **only the DSS peak** is displayed.

---

## 8. Record the Chemical Shift of DSS

Determine the **chemical shift of the DSS peak** in your spectrum, for example by placing the mouse at the peak maximum or by peak picking in `nd`.

**Write this number down.** It is the only result we need from this lesson. We will use it for all our measurements.

---

## Summary of Commands and Actions

| Command / Action | Purpose |
|------------------|---------|
| `cd` | Go to the 1D DSS experiment folder |
| `wget` | Download `fidft_dss.com` |
| `chmod +x` | Make the script executable |
| `bruker` | Read the experiment parameters, generates `fid.com` |
| `gedit` | Copy the parameters into the `bruk2pipe` block |
| `cat` | Check that the edit is really in the script |
| `./fidft_dss.com` | Run the script |
| `nd` | Open the viewer |
| Shift+S, select `dss.ft`, **Read/Draw** | Load the processed 1D spectrum (the default is the FID) |
| p0 slider | Phase the spectrum if needed |
| `z`, draw a rectangle, right-click | Zoom in until only the DSS peak is displayed |
| Record the DSS shift | The one number we need for referencing |

**This is the end of the fifth lesson.**
