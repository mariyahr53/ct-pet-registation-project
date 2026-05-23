import SimpleITK as sitk


def rigid_registration(fixed_image, moving_image):
    """
    Perform rigid CT-PET registration using mutual information.
    """

    # Convert both images to Float32
    fixed_float = sitk.Cast(fixed_image, sitk.sitkFloat32)
    moving_float = sitk.Cast(moving_image, sitk.sitkFloat32)

    # Initialize transform
    initial_transform = sitk.CenteredTransformInitializer(
        fixed_float,
        moving_float,
        sitk.Euler3DTransform(),
        sitk.CenteredTransformInitializerFilter.GEOMETRY
    )

    registration_method = sitk.ImageRegistrationMethod()

    registration_method.SetMetricAsMattesMutualInformation(
        numberOfHistogramBins=50
    )

    registration_method.SetMetricSamplingStrategy(
        registration_method.RANDOM
    )

    registration_method.SetMetricSamplingPercentage(0.01)

    registration_method.SetInterpolator(sitk.sitkLinear)

    registration_method.SetOptimizerAsRegularStepGradientDescent(
        learningRate=2.0,
        minStep=1e-4,
        numberOfIterations=100,
        gradientMagnitudeTolerance=1e-8
    )

    registration_method.SetOptimizerScalesFromPhysicalShift()

    registration_method.SetInitialTransform(
        initial_transform,
        inPlace=False
    )

    final_transform = registration_method.Execute(
        fixed_float,
        moving_float
    )

    registered_image = sitk.Resample(
        moving_image,
        fixed_image,
        final_transform,
        sitk.sitkLinear,
        0.0,
        moving_image.GetPixelID()
    )

    return registered_image, final_transform