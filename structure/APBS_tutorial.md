# Tutorial: Electrostatic Surfaces with the APBS Web Server and PyMOL

In this tutorial you will calculate the electrostatic potential of a protein using the APBS-PDB2PQR web server and then visualize it in PyMOL as a red/blue colored surface. No software installation is needed for the calculation part.

**You need:** a web browser, [PyMOL](https://pymol.org) installed, and a PDB ID (e.g. `1UBQ`, ubiquitin, a small protein that runs quickly) or your own PDB file.

## Part 1: Prepare the structure with PDB2PQR

APBS needs a **PQR** file, which is a PDB file with added hydrogens, partial charges and atomic radii. PDB2PQR creates it for you.

1. Go to <https://server.poissonboltzmann.org> and start a new job by selecting **PDB2PQR**.
2. Under *PDB source*, enter a **PDB ID** (e.g. `1UBQ`) or upload your own PDB file.
3. Set the **force field to AMBER**. Leave every other setting at its default.
4. Click **Start Job**.
5. Wait for the job to finish. This usually takes well under a minute for a small protein. The page will update by itself.

> [!TIP]
> If you uploaded your own file and the job fails, check that the file contains protein atoms only and no unusual residues or formatting problems.

## Part 2: Run APBS

1. On the finished PDB2PQR results page, click **Next: Use results with APBS**.
2. Keep all **default parameters**.
3. Click **Start Job** and wait until it completes.

## Part 3: Download the files you need

On the APBS results page, download:

| File | What it is |
|---|---|
| `.pqr` file (from the PDB2PQR step) | The structure with charges and radii |
| `.dx` file (electrostatic potential map) | The calculated potential on a 3D grid |

Save both into the same folder. If the `.dx` file is compressed (for example `.dx.gz`), unzip it first. The file names on the server may differ slightly from job to job; look for the one that ends in `.dx`.

> [!NOTE]
> Use the `.pqr` file (or the original PDB file) together with the `.dx` file. Use the same structure that went into the calculation so the map lines up with the protein.

## Part 4: Visualize in PyMOL

You can use the menus (**File > Open**) or type the commands into the PyMOL command line at the bottom of the window.

### Step 1: Load the protein and the potential map

```
load 1ubq.pqr, protein
load 1ubq.dx, e_map
```

Replace the file names with yours. Two objects now appear in the right-hand panel: `protein` and `e_map`. The map is just data; you will not see much of it yet.

### Step 2: Show the protein as a surface

```
hide everything
show surface, protein
```

The protein is now a plain surface.

### Step 3: Create a color ramp from the potential map

```
ramp_new e_lvl, e_map, [-5, 0, 5], [red, white, blue]
```

This defines a color scale: **red** for negative potential (-5 kT/e), **white** for neutral (0), and **blue** for positive potential (+5 kT/e).

### Step 4: Color the surface with the ramp

```
set surface_color, e_lvl, protein
```

The surface should now be colored red, white and blue. If it is still plain, run `rebuild`.

### Step 5: Make it look good

```
bg_color white
set surface_quality, 1
ray 1200, 1000
png electrostatics.png, dpi=300
```

`ray` renders a high-quality image and `png` saves it. Adjust the range (for example `[-3, 0, 3]`) if the colors look too weak or too saturated.

### Quick alternative: the APBS Tools plugin

If your PyMOL has the plugin: with the protein and `.dx` map loaded, go to **Plugin > APBS Electrostatics**, open the **Visualization** tab, and press **Show** in the *Molecular Surface* section. The default is blue at +1 kT and red at -1 kT.

## How to read the result

- **Red regions** are negatively charged (acidic residues such as Asp and Glu).
- **Blue regions** are positively charged (basic residues such as Lys and Arg).
- **White regions** are roughly neutral or hydrophobic.

Electrostatic patches often point to binding sites for DNA, ligands or other proteins.

## Troubleshooting

- **Surface stays gray:** check that `ramp_new` used the loaded map name and that `set surface_color` names your protein object. Then run `rebuild`.
- **Everything is fully red or blue:** widen the range, e.g. `[-10, 0, 10]`.
- **Map and protein do not overlap:** make sure you loaded the PQR/PDB file from the same job as the `.dx` file.
- **Water or ligands cover the surface:** remove them with `remove solvent` or `remove organic`.

## Optional exercises

1. Compare two related proteins side by side.
2. Run the job again with a different force field and see whether the potential changes.
3. Select the residues of a binding site (`select site, resi 14-20`) and describe their charge.
