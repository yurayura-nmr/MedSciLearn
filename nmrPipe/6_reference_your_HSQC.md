# Referencing the HSQC with DSS

In Lesson 5 we measured the chemical shift of DSS in a 1D spectrum.
Now we use that number to **properly reference** our HSQC, so that the chemical shifts in both 
the <sup>1</sup>H and the <sup>15</sup>N dimension are correct with respect to DSS.

> **Before you start:** You need the **DSS chemical shift** you wrote down in Lesson 5 (in our example: `-0.0016` ppm). You should be in the `tcsh` shell.

---

## Overview

1. Go to the HSQC folder
2. Download `dss.py`
3. Run it in the same folder
4. Enter your measured DSS shift
5. Read the new, referenced centers
6. Put them into the processing script
7. Run the script to get the final, referenced HSQC

---

## 1. Go to the HSQC Folder

Go back to the folder of your **HSQC experiment**, the one containing `fid`, `acqus` and your processing script `fidft_hqsc.com`:

```
cd <your_hsqc_folder>
ls
```

> It is important to work in the **experiment folder itself**. The script needs access to the experiment parameters stored in `acqus` and related files.

---

## 2. Download `dss.py`: `wget`

```
wget https://raw.githubusercontent.com/yurayura-nmr/nmrpipe-scripts/main/dss_1d/dss.py
```

> **Note:** As always, use the **raw** link, not the normal GitHub page link.

Check with `ls` that the file arrived.

---

## 3. Run the Script

Execute it **in the same folder**:

```
python3 dss.py
```

---

## 4. Enter the Measured DSS Shift

The script asks you for the DSS chemical shift. Enter the value you measured in Lesson 5. In our example:

```
-0.0016
```

(The unit is ppm. Enter your own number, with its sign.)

---

## 5. Read the New Centers

From your DSS shift and the parameters of the experiment, the script now calculates the **new, referenced centers** (the corrected 0 ppm reference) for the dimensions of your experiment.

**Write these numbers down**, or keep the terminal window open. You need them in the next step.

---

## 6. Put the New Centers into the Processing Script

Open the HSQC processing script:

```
gedit fidft_hqsc.com &
```

Find the `bruk2pipe` block (the same one you edited in Lesson 1) and replace the old values by the new ones from `dss.py`:

| Line | Dimension | Replace by |
|------|-----------|------------|
| `-xCAR` | <sup>1</sup>H (direct dimension) | new <sup>1</sup>H center |
| `-yCAR` | <sup>15</sup>N (indirect dimension) | new <sup>15</sup>N center |

> **Be careful:** As always, **change only the numbers**. Do not delete a `\` at the end of a line, do not add spaces after it, and never insert new lines (see the warning in Lesson 3).

Save with **Ctrl+S** and verify your edit:

```
cat fidft_hqsc.com
```

You should see the new values. If you still see the old numbers, you probably forgot to save.

---

## 7. Run the Script

```
./fidft_hqsc.com
```

This creates your **final HSQC**, referenced with respect to DSS in both the <sup>1</sup>H and the <sup>15</sup>N dimension.

---

## 8. Look at the Result

```
nd
```

Press **Shift+S** (Caps Lock must be off), select your processed spectrum (the `.ft2` file) and click **Read/Draw**.

Your peaks now sit at their correctly referenced chemical shifts. The spectrum may look very similar to the previous one, but the **ppm values** are now correct, and these are the numbers we will use for all later work.

---

## Summary of Commands and Actions

| Command / Action | Purpose |
|------------------|---------|
| `cd` | Go to the HSQC experiment folder |
| `wget` | Download `dss.py` |
| `python3 dss.py` | Calculate the referenced centers |
| Enter the DSS shift | The number you measured in Lesson 5 |
| `gedit` | Put the new centers into `fidft_hqsc.com` |
| `cat` | Check that the edit is really in the script |
| `./fidft_hqsc.com` | Run the script and get the referenced HSQC |
| `nd`, Shift+S | Display the final spectrum |

**This is the end of the sixth lesson.**
