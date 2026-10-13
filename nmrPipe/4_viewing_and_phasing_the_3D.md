# Your First 3D Dataset: Looking at the Projections

In Lesson 3 you processed the HNCO with `ft_hnco.com` and opened it with `nd`. Now we look at the data for the first time. A 3D spectrum is a **data cube**, which is hard to look at all at once, so we start with **2D projections** of it.

> **Before you start:** `ft_hnco.com` has finished and you are in your experiment folder, in the `tcsh` shell.

---

## 1. Open `nd` and the File Selector

Start the viewer:

```
nd
```

This is the first time you load a 3D dataset, so there is a new command to learn:

1. **Right-click** the **File** button.
2. In the menu that appears, select **File**.

A file selection window opens.

> **Shortcut:** Instead of the right-click menu you can press **Shift+S** while the mouse is over the nmrDraw window. If it does not work, check that **Caps Lock is off**. With Caps Lock on, the Shift key combination is not recognized.

---

## 2. The Three `.dat` Files

You should now see **three `.dat` files**. These are **2D projections** of the original 3D data cube. The three axes of the cube are <sup>1</sup>H<sup>N</sup>, <sup>15</sup>N and <sup>13</sup>C':

| File | Axes | What to expect |
|------|------|----------------|
| `HN.15N.dat` | <sup>1</sup>H<sup>N</sup> vs <sup>15</sup>N | Looks like the HSQC you already know |
| `13C.15N.dat` | <sup>13</sup>C' vs <sup>15</sup>N | Unfamiliar |
| `HN.13C.dat` | <sup>1</sup>H<sup>N</sup> vs <sup>13</sup>C' | The one we actually want |

Load each of them with **Read/Draw** and look at them one by one.

---

## 3. Look at Each Projection

### `HN.15N.dat`: the familiar one

This should look **almost the same as the HSQC** from Lessons 1 and 2. Compared to the HSQC you will probably notice:

- **lower resolution** (broader peaks)
- maybe **lower sensitivity** (weaker peaks)

That is normal. A 3D experiment has to spread its measurement time over more increments.

### `13C.15N.dat`: the unfamiliar one

This is a nitrogen-carbonyl correlation. We do not often display it, so it will not look familiar. Just have a look.

### `HN.13C.dat`: the important one

This is what we actually want to see. It shows the correlation between:

- the <sup>1</sup>H on the **x-axis** (the amino acid "fingerprint"), and
- the <sup>13</sup>C' (carbonyl carbon) on the **y-axis**, which carries the **important assignment information**.

> **Why is this useful for assignment?** In an HNCO, the <sup>1</sup>H<sup>N</sup> and the <sup>15</sup>N belong to amino acid **i**, but the <sup>13</sup>C' belongs to the **previous** amino acid, **i-1**. So every peak links an amino acid to its **neighbor** in the sequence. This is exactly the information we need to walk along the protein backbone.

---

## 4. Lower the Contour Levels First

Before you check the phase, make small peak problems easier to see:

1. Click the **`-`** button with the mouse (one or several times). This changes the contour levels so that the spectrum is shown at more drastic contour levels.
2. Press the **`r`** key to **redraw** the spectrum.

At these contour levels a phase mismatch is much easier to see than at the default level.

---

## 5. Check the Phase of All Projections

As in Lesson 2, go through the projections again and check the phase:

1. Press **`h`** to show the horizontal trace.
2. Move to the **maximum** of an example peak and check the trace: is it perfectly in phase?
3. Do this for **all three projections**.

If a peak is not perfectly in phase, adjust **p0** with the slider (drag = large change, click next to it = small change), exactly as you did in Lesson 2.

In our example, the phase mismatch was easiest to see at the lower contour levels, and the value we found was:

```
p0 = +7
```

Note down your own value of p0.

---

## 6. Put the p0 Value into `ft_hnco.com`

Go back to the terminal (you can close nmrDraw now) and open the script:

```
gedit ft_hnco.com &
```

Find this line:

```
| nmrPipe -fn PS -p0 0 -p1 0 -di                \
```

and replace it by (using your own p0 value, `+7` in our example):

```
| nmrPipe -fn PS -p0 +7 -p1 0 -di                \
```

> **The easiest and safest way:** do not retype the line. Just click next to the `0` after `-p0` and **change that one number**. This way you cannot accidentally damage the `|` at the start or the `\` at the end of the line (see the warning in Lesson 3).

Save with **Ctrl+S** and verify your edit:

```
cat ft_hnco.com
```

You should see your new p0 value in the `PS` line. If you still see `-p0 0`, you probably forgot to save in `gedit` (**Ctrl+S**).

---

## 7. Run the Script Again

```
./ft_hnco.com
```

Then reopen `nd`.

---

## 8. Verify All Planes

Load **each of the three projections** again (`HN.15N.dat`, `13C.15N.dat` and `HN.13C.dat`) and, for each one:

1. Lower the contour levels (`-` button, then `r` to redraw).
2. Press **`h`** to show the horizontal trace.
3. Check an example peak on the right side and one on the left side of the spectrum.

All peaks in **all planes** should now be perfectly in phase. If one is not, repeat steps 5 to 7 with a corrected p0 value.

---

## Summary of Commands and Actions

| Command / Action | Purpose |
|------------------|---------|
| `nd` | Open the viewer |
| Right-click **File**, select **File** | Open the file selection window |
| **Read/Draw** | Load and display the selected file |
| `HN.15N.dat` | HSQC-like projection |
| `13C.15N.dat` | N-C' projection |
| `HN.13C.dat` | H-C' projection, the one used for assignment |
| Shift+S | Shortcut for the file selection window (Caps Lock must be off) |
| `-` button, then `r` | Lower the contour levels and redraw |
| `h` | Show the horizontal trace to check the phase |
| p0 slider | Adjust the phase if a peak is not perfectly in phase |
| `gedit` | Change the number after `-p0` in the `PS` line of `ft_hnco.com` |
| `cat` | Check that the edit is really in the script |
| `./ft_hnco.com` | Run the script again |
| `nd` + `h` | Verify that all three projections are in phase |

**This is the end of the fourth lesson.**
