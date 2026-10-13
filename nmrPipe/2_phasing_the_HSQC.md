# Phase Correction with NMRPipe (p0)

In the first lesson you converted your data, ran the processing script, and looked at your first spectrum. Now we make that spectrum **look right**. The most important step is **phase correction**: making every peak purely absorptive (a nice symmetric positive peak, no wiggles or negative parts).

> **Before you start:** You should have a processed spectrum (a `.ft2` file) from Part 1, and you should be inside your experiment folder, in the `tcsh` shell.

---

## 1. Open the Spectrum: `nd`

In our environment, `nd` is a shortcut for `nmrDraw`:

```
nd
```

Your spectrum is displayed right away. (If it is not, load the `.ft2` file via the file menu as in Part 1.)

---

## 2. Show a Horizontal Trace

Press the **`h`** key while the mouse is over the spectrum. A **horizontal trace** (a 1D slice through the spectrum along the direct dimension) appears. This is the view you need to judge the phase.

---

## 3. Check One Peak on the Right Side

1. Pick **one clear example peak on the right side** of the spectrum.
2. Move the mouse to the **peak maximum**. The trace follows the mouse and shows the slice through that peak.
3. Ask yourself: **is the peak in phase?**

An in-phase peak is symmetric, positive, and its baseline is flat on both sides. A peak that is out of phase looks lopsided: one side dips below the baseline and the other side is raised, or the peak looks like a mixture of a peak and a wiggle.

If it already looks good, that is a good start. But the question is not "is it roughly in phase?", it is: **is it perfectly in phase?**

---

## 4. Adjust p0

Use the **p0 slider** in the nmrDraw window:

| Action | Effect |
|--------|--------|
| **Drag** the slider | Large change in phase |
| **Click next to** the slider | Small change in phase |

Start with small clicks and watch the trace until the peak is **perfectly symmetric** with a flat baseline on both sides.

### Write down the p0 value

**Note down the value of p0** shown by the slider. You will need it in a moment.

In our example the peak was almost in phase, but not perfectly, and the value we found was:

```
p0 = -11
```

---

## 5. Check a Peak on the Left Side

Now move to **one more peak at the opposite (left) end of the spectrum** and look at its trace.

- If it is **also in phase**, your p0 value is good for the whole spectrum.
- If one end is in phase and the other is not, see the note on p1 at the end of this lesson.

---

## 6. Put the p0 Value into the Script

Go back to the terminal (you can close nmrDraw now).

1. Open the processing script:

   ```
   gedit fidft_hqsc.com &
   ```

2. Find the **first** `PS` line. It looks like this:

   ```
   | nmrPipe -fn PS -p0 0
   ```

   (The exact line may contain more options after `-p0 0`. Leave everything else as it is.)

3. Replace the `0` after `-p0` with the value you just determined (`-11.0` in our example):

   ```
   | nmrPipe -fn PS -p0 -11.0
   ```

4. Save with **Ctrl+S**.

> Only change the **first** `PS -p0` line. Do not touch the other lines.

5. **Verify your edit.** As in Part 1, print the script and check that the change really went in:

   ```
   cat fidft_hqsc.com
   ```

   You should see your new p0 value. If you still see `-p0 0`, you probably forgot to save in `gedit` (**Ctrl+S**).

---

## 7. Run the Script Again

```
./fidft_hqsc.com
```

The script overwrites the old processed spectrum with the newly phased one.

---

## 8. Check the Result

Reopen nmrDraw:

```
nd
```

Press **`h`** again and recheck the same peaks (one on the right, one on the left). They should now be **perfectly in phase**.

If not, repeat steps 3 to 7. Remember to use the **new** value of p0 (it is the value you read from the slider relative to the current spectrum, so check carefully whether you need to start from the old value or from zero).

---

> **Note on p1:** It is possible that one peak is in phase at one end of the spectrum while a peak at the other end is out of phase. In that case, p0 alone is not enough and you also need to adjust **p1**. The procedure is analogous. We will cover it when it comes up.

---

## Summary of Commands and Actions

| Command / Action | Purpose |
|------------------|---------|
| `nd` | Shortcut for `nmrDraw`, displays the spectrum |
| `h` (in nmrDraw) | Show the horizontal trace |
| Mouse on peak maximum | Look at the trace through that peak |
| p0 slider (drag) | Large phase change |
| p0 slider (click next to it) | Small phase change |
| Note down p0 | You need it for the script |
| `gedit` | Change the first `PS -p0 0` to `PS -p0 <value>` |
| `cat` | Check that the edit is really in the script |
| `./fidft_hqsc.com` | Run the script again |
| `nd` + `h` | Recheck that peaks are now perfectly in phase |

**This is the end of the second lesson.**
