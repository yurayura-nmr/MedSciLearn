## Start CCPN Analysis

Open a **new terminal window**. This matters because the NMRPipe workflow used `tcsh`, whereas the `ana` shortcut is configured for the Bash shell.

```bash
cd ~/3_ccpn
ana
```

## Create and save a project

Once CCPN Analysis has opened:

1. Create a **new project** using the Project menu.
2. Give it a short, descriptive name that you will recognize later, such as `sampleName_HSQC`.
3. **Save it immediately**, even though it is empty. This creates the project directory and establishes a clear, reusable filename before spectra and assignments are added. CCPN project saving records the project under its chosen name and location. [sites.google](https://sites.google.com/site/ccpnwiki/home/documentation/ccpnmr-analysis/tutorials/loading-projects-and-spectra)


## Open the HSQC spectrum

In CCPN Analysis:

1. Select **Project → Open Spectra**.
2. Change **File format** to **NMRPipe**.
3. Navigate to the folder containing the processed HSQC data.
4. Select the referenced HSQC `.ft2` file.
5. In the **Experiment** field at the bottom, double-click `Expt1` and replace it with a clear name, for example `HSQC_15N` or `SampleName_HSQC`.
6. Click **Open Spectrum**.
7. Click **Commit** to import the spectrum.

## Set the experiment type

On the next screen:

1. Double-click the **Type** or **Synonym** field.
2. Select **15N HSQC/HMQC**.
3. Click **Close**.

The referenced HSQC is now imported into the newly saved CCPN project.
