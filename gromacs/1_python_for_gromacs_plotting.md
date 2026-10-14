# Working with GROMACS XVG Files in Python

This short tutorial shows how to display and histogram a GROMACS `.xvg` file directly in the Python interpreter (REPL).
For now, we will not use Jupyter or save a `.py` script—just type commands one at a time.

## 1. Start Python

Open a terminal and start Python:

```python
python
```

or, if needed:

```python
python3
```

You should see a prompt such as `>>>`. Everything below is typed at that prompt.

## 2. Import the needed libraries

```python
import numpy as np
import matplotlib.pyplot as plt
```

- `numpy` reads the numerical data. (Remember to install numpy with `pip install numpy`)
- `matplotlib.pyplot` makes the plot. (Remember to install matplotplib with `pip install matplotlib`)

## 3. Load an XVG file

For a typical two-column xvg file, such as time versus RMSD:

```python
x, y = np.loadtxt("rmsd.xvg", comments=["@", "#", "&"], unpack=True)
```

- Replace `"rmsd.xvg"` with your file name.
- `comments=["@", "#", "&"]` ignores GROMACS/Grace metadata lines.
- `unpack=True` puts column 1 into `x` and column 2 into `y`.

Check that the data loaded:

```python
x[:5]
y[:5]
```

## 4. Display the data as a line plot

```python
plt.plot(x, y)
plt.show()
```

A window should appear showing the time series. To make it clearer:

```python
plt.plot(x, y)
plt.xlabel("Time (ps)")
plt.ylabel("RMSD (nm)")
plt.show()
```

## 5. Make a histogram

To examine the distribution of the y-values, for example the distribution of RMSD values:

```python
plt.hist(y, bins=50)
plt.show()
```

With labels:

```python
plt.hist(y, bins=50)
plt.xlabel("RMSD (nm)")
plt.ylabel("Number of frames")
plt.show()
```

- `bins=50` controls how many intervals the data are divided into.
- Try `bins=20` or `bins=100` to see how the appearance changes.

## 6. Optional: normalized histogram

If you want the histogram area to represent probability density rather than frame counts:

```python
plt.hist(y, bins=50, density=True)
plt.xlabel("RMSD (nm)")
plt.ylabel("Probability density")
plt.show()
```

## Quick reference

```python
import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt("file.xvg", comments=["@", "#", "&"], unpack=True)

plt.plot(x, y)
plt.show()

plt.hist(y, bins=50)
plt.show()
```

That is the core workflow: **load the xvg data, inspect it, plot it, and histogram the values of interest**.


## Addendum: Saving the Current Figure

After making a plot or histogram, save the figure that is currently displayed with `plt.savefig()`.

### Save as PDF

```python
plt.savefig("my_figure.pdf")
```

### Save as PNG

```python
plt.savefig("my_figure.png")
```

### Typical workflow

```python
plt.plot(x, y)
plt.xlabel("Time (ps)")
plt.ylabel("RMSD (nm)")

plt.savefig("rmsd_plot.pdf")
plt.savefig("rmsd_plot.png", dpi=300)
plt.show()
```

- The file type is determined by the extension: `.pdf` or `.png`.
- `dpi=300` is useful for a higher-resolution PNG, suitable for presentations or manuscripts.
- Call `plt.savefig()` **before** `plt.show()`; after the plot window closes, the current figure may no longer be available.
- The files are saved in the folder where you started Python, unless you provide a path, for example:

```python
plt.savefig("figures/rmsd_plot.pdf")
```

For a histogram, the same commands work:

```python
plt.hist(y, bins=50)
plt.xlabel("RMSD (nm)")
plt.ylabel("Number of frames")

plt.savefig("rmsd_histogram.pdf")
plt.show()
```
