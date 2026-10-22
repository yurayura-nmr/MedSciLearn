# Assigning the Carbonyl Carbons (i-1)

In Lesson 7 you loaded the HNCO into CCPN and confirmed that the referencing worked. Now we start the **actual assignment work**: we assign a few carbonyl carbons.

> **Remember:** In an HNCO, the <sup>1</sup>H<sup>N</sup> and <sup>15</sup>N of a peak belong to amino acid **i**, but the <sup>13</sup>C' belongs to the **previous** amino acid, **i-1**. So for every root resonance in the HSQC, the HNCO gives us the carbonyl carbon of its **preceding neighbor**.

> **Before you start:** You need the windows from Lesson 7 (the HSQC window and the strip window **`CO`**), and your HSQC must be peak picked with the root resonances prepared.

---

## 1. Open the Peak List

Open the **peak list** in CCPN. Inside the peak list, choose the **HSQC**.

It already contains the prepared list of **root resonances**. Depending on your project, these are **assigned** or still **unassigned**.

---

## 2. Navigate Through the HSQC Peaks Automatically

### Switch on "Find Peak"

1. Tick the **Find Peak** checkbox (set it to *yes*).
2. Check that the field to the right of it says **Window:** followed by the **name of your HSQC window**.

From now on, whenever you **click an entry in the peak list**, CCPN navigates to that <sup>1</sup>H and <sup>15</sup>N resonance with a crosshair in the HSQC.

This is already extremely useful: you can **jump from peak to peak just by going down the list**, without searching for each peak by hand.

---

## 3. Navigate the `CO` Strip Automatically Too

Below **Find Peak**, also select **Go to position** and choose the window **`CO`** (<sup>1</sup>H / <sup>15</sup>N).

Now CCPN also navigates to the same <sup>1</sup>H/<sup>15</sup>N position in the `CO` strip window. All you have to do is **find the peak in the strip**. That peak is the **carbonyl carbon of residue i-1** of the root resonance you just selected in the HSQC.

### About the guide markers

CCPN draws **markers** (navigation guidelines) to show you where it navigated to. They are very useful, but after a few peaks your spectrum can get **covered in guidelines**. You can erase them by pressing **`n`**.

---

## 4. Pick and Assign the Carbonyl Peak

1. **Pick the new peak** in the `CO` strip.
2. **Right-click** and choose **Assign**, or just press **`a`**.
3. CCPN should already **offer the assignments of the <sup>1</sup>H and <sup>15</sup>N** in the list, because these were done before in the HSQC.
4. For the <sup>13</sup>C, choose **Add new and assign**, and assign it to the **<sup>13</sup>C (carbonyl) of residue i-1**.

**Example (ubiquitin):** For the root resonance **V70**, the carbonyl carbon in the HNCO belongs to **L69**. So the <sup>1</sup>H and <sup>15</sup>N are assigned to V70, and the new <sup>13</sup>C' is assigned to the carbonyl of L69.

---

## 5. Continue Down the List

Go down the peak list and repeat steps 2 to 4 for the next root resonance:

1. Click the next entry in the peak list.
2. Find the peak in the `CO` strip.
3. Pick it and assign it (`a`).

Assign **as many i-1 carbonyls as you can**.

> **Tip:** If the strip window gets too crowded, press **`n`** to clear the guide markers.

---

## Summary of Actions

| Action | Purpose |
|--------|---------|
| Open the peak list, choose the HSQC | Get the list of root resonances |
| **Find Peak** = yes, **Window:** HSQC window | Jump to the clicked peak in the HSQC |
| **Go to position**, select `CO` | Jump to the same <sup>1</sup>H/<sup>15</sup>N position in the strip |
| `n` | Erase the guide markers |
| Pick the peak in `CO`, then **`a`** (or right-click, **Assign**) | Assign the carbonyl |
| **Add new and assign** for <sup>13</sup>C | Create the carbonyl resonance of residue i-1 |
| Go down the list | Assign as many i-1 carbonyls as possible |

**This is the end of the eighth lesson.**
