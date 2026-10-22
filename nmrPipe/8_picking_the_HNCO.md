# The HNCO in CCPN: Checking the Referencing

Well done: you processed the HNCO from the scripts on your own (Lesson 3 and 4) 
and you referenced your spectra with DSS (Lessons 5 and 6). 
Now we start with the **CCPN part**: we load the HNCO into CCPN and check that the referencing really worked.

> **What we assume from here on:** The HSQC is already **peak picked** in CCPN, and, if there is prior knowledge, a few peaks are already **assigned**. The **molecule has been created**, so the project contains either **dummy resonances** that are still unassigned or a **partially assigned** system.
> In any case, the next step after this lesson is **assigning the HNCO peaks**. For that we need, at the very least, the **root resonances picked in the HSQC**.

> **Before you start:** You need your processed HNCO (the output of `ft_hnco.com`, run with the
> DSS-referenced values) and your referenced HSQC. Both should be loaded in your CCPN project.

---

## 1. Open the HNCO

In CCPN, open the spectrum:

1. Use the **open spectrum** dialog.
2. Look for a file called **`HNCO.pipe`**.

> **Tip:** By default the dialog only shows certain file types. If you do not see `HNCO.pipe`,
> change the file filter to show **all files** (`*.*`).

---

## 2. Tell CCPN What Spectrum This Is

After opening, CCPN does not yet know what kind of experiment you loaded. In the loading dialog:

1. **Double-click** the empty space in the **type synonym** field.
2. Select the correct experiment type for your spectrum (**HNCO**).

This tells the program what spectrum this is.

---

## 3. Create a Window for the Strips (`CO`)

We now create a window that shows the HNCO as **strips** (<sup>1</sup>H on the x-axis, <sup>13</sup>C' on the y-axis, one strip per <sup>15</sup>N plane).

1. Go to **Window**, then **Create**.
2. Set the axes:

| Axis | Nucleus |
|------|---------|
| x-axis | <sup>1</sup>H |
| y-axis | <sup>13</sup>C |
| z-axis | <sup>15</sup>N |

3. Name the window **`CO`**.
4. Click **Create window**.

---

## 4. Create a Window for the <sup>1</sup>H-<sup>15</sup>N View

Now create **another window**:

1. Go to **Window**, then **Create** again.
2. Set the axes:

| Axis | Nucleus |
|------|---------|
| x-axis | <sup>1</sup>H |
| y-axis | <sup>15</sup>N |
| z-axis | <sup>13</sup>C |

3. Click **OK**.

---

## 5. Check the Referencing

In the <sup>1</sup>H-<sup>15</sup>N window, **drag the z-axis slider** to move through the <sup>13</sup>C dimension.

As you move through the carbon planes, the **HNCO peaks should perfectly overlay on the HSQC peaks**, **if** the referencing (and everything else) worked correctly.

Go through all the planes and check:

- Do the HNCO peaks sit **right on top** of the HSQC peaks?
- Is this true for peaks all over the spectrum, not just a few?

If yes, your referencing worked and you are ready for the next lesson.

If the peaks are **shifted** relative to each other, something went wrong, for example in the referencing (Lessons 5 and 6) or in the processing parameters. Go back, check your edits with `cat`, and process again.

---

## Summary of Actions

| Action | Purpose |
|--------|---------|
| Open spectrum, show all files (`*.*`) | Find and load `HNCO.pipe` |
| Double-click **type synonym** | Tell CCPN this is an HNCO |
| **Window**, **Create**: x = <sup>1</sup>H, y = <sup>13</sup>C, z = <sup>15</sup>N, name `CO` | Strip window for the HNCO |
| **Window**, **Create**: x = <sup>1</sup>H, y = <sup>15</sup>N, z = <sup>13</sup>C | <sup>1</sup>H-<sup>15</sup>N view |
| Drag the z-axis slider | Move through the <sup>13</sup>C planes |
| Compare HNCO and HSQC peaks | Confirm that the referencing worked |

**This is the end of the seventh lesson.**
