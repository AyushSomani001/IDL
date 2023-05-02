# Copyright (C) 2023, Ayush Somani.

"""
The below Python code defines a function called overlay_mask which takes in two PIL.Image objects, background_img and mask_img, 
and overlays the mask onto the image with transparency alpha. The mask is first resized to the same size as img and then a colormap 
is applied to it using cm.get_cmap(colormap) from matplotlib. The masked image is then blended with the original img with transparency 
alpha using numpy and PIL. The function raises a TypeError if img or mask are not PIL.Image objects and a ValueError if alpha is not a 
float between 0 and 1.
"""

def overlay_mask(background_img: Image.Image, mask_img: Image.Image, colormap: str = "jet", alpha: float = 0.75) -> Image.Image:
    """
    Overlay a colored mask on a background image.

    Args:
        background_img: A PIL image to use as the background.
        mask_img: A grayscale PIL image to use as the mask.
        colormap: A string indicating the name of the colormap to use.
        alpha: A float between 0 and 1 indicating the transparency of the background image.

    Returns:
        A PIL image with the mask overlaid on the background image.
    """

    if not isinstance(background_img, Image.Image) or not isinstance(mask_img, Image.Image):
        raise TypeError("Both background_img and mask_img must be PIL.Images")

    if not isinstance(alpha, float) or alpha < 0 or alpha >= 1:
        raise ValueError("alpha must be a type float between 0 and 1.")

    # Get the colormap and resize the mask.
    cmap = cm.get_cmap(colormap)
    resized_mask = mask_img.resize(background_img.size, resample=Image.BICUBIC)

    # Apply the colormap to the mask.
    color_mask = (255 * cmap(np.asarray(resized_mask) ** 2)[:, :, :3]).astype(np.uint8)

    # Overlay the mask on the background image.
    overlayed_img = Image.fromarray((alpha * np.asarray(background_img) + (1 - alpha) * color_mask).astype(np.uint8))

    return overlayed_img
