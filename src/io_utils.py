from pathlib import Path
import SimpleITK as sitk


def load_dicom_series(folder_path):
    """
    Load a DICOM folder as a 3D SimpleITK image.
    """
    folder_path = Path(folder_path)

    reader = sitk.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(str(folder_path))
    reader.SetFileNames(dicom_names)

    image = reader.Execute()
    return image


def print_image_info(image, name="Image"):
    """
    Print key metadata for a SimpleITK image.
    """
    print(f"{name} Size:", image.GetSize())
    print(f"{name} Spacing:", image.GetSpacing())
    print(f"{name} Origin:", image.GetOrigin())
    print(f"{name} Direction:", image.GetDirection())