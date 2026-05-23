import SimpleITK as sitk


def affine_registration(fixed_image, moving_image):
    """
    Perform affine CT-PET registration using mutual information.
    """

    # Convert images to Float32
    fixed_float = sitk.Cast(fixed_image, sitk.sitkFloat32)
    moving_float = sitk.Cast(moving_image, sitk.sitkFloat32)

    # Initialize affine transform
    initial_transform = sitk.CenteredTransformInitializer(
        fixed_float,
        moving_float,
        sitk.AffineTransform(3),
        sitk.CenteredTransformInitializerFilter.GEOMETRY
    )

    registration_method = sitk.ImageRegistrationMethod()

    # Mutual information metric
    registration_method.SetMetricAsMattesMutualInformation(
        numberOfHistogramBins=50
    )

    # Random sampling
    registration_method.SetMetricSamplingStrategy(
        registration_method.RANDOM
    )

    registration_method.SetMetricSamplingPercentage(0.01)

    # Interpolation
    registration_method.SetInterpolator(sitk.sitkLinear)

    # Optimizer
    registration_method.SetOptimizerAsRegularStepGradientDescent(
        learningRate=1.0,
        minStep=1e-4,
        numberOfIterations=150,
        gradientMagnitudeTolerance=1e-8
    )

    registration_method.SetOptimizerScalesFromPhysicalShift()

    registration_method.SetInitialTransform(
        initial_transform,
        inPlace=False
    )

    # Execute registration
    final_transform = registration_method.Execute(
        fixed_float,
        moving_float
    )

    # Resample moving image into fixed image space
    registered_image = sitk.Resample(
        moving_image,
        fixed_image,
        final_transform,
        sitk.sitkLinear,
        0.0,
        moving_image.GetPixelID()
    )

    return registered_image, final_transform