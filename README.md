# PET/CT Image Registration Project

This project develops a Python-based pipeline for registering PET and CT medical images using data from **The Cancer Imaging Archive (TCIA)**.

The pipeline currently implements three classical registration methods:

* **Rigid registration** – translation and rotation
* **Affine registration** – translation, rotation, scaling and shearing
* **B-spline registration** – local deformable registration

## Current Features

* DICOM loading and metadata inspection
* DICOM-to-NIfTI conversion
* CT and PET visualisation
* PET resampling into CT space
* Rigid, affine and B-spline registration
* PET/CT before-and-after overlays
* Runtime and TRE evaluation
* Single-patient and batch-processing pipelines
* Automatic saving of registered images and results

## Technologies

Python, SimpleITK, NumPy, Pandas, Matplotlib and Jupyter.

## Dataset

Initial development uses PET/CT data from the **QIN-BREAST** collection on TCIA. Raw medical imaging data is not included in this repository.

## Project Status

The core classical registration pipeline is complete. Current development focuses on registration evaluation, deformation-field analysis, parameter comparison and final results visualisation.
