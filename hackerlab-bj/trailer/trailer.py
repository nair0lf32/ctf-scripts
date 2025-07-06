#!/usr/bin/python3
"""XOR all images in a folder and save the result as a new image."""

import os
from PIL import Image
import numpy as np


def xor_images(image_paths):
    """XOR all images in the given paths and return the result as a PIL Image."""
    result = np.array(Image.open(image_paths[0]).convert("L"))
    for path in image_paths[1:]:
        img = np.array(Image.open(path).convert("L"))
        result = np.bitwise_xor(result, img)
        return Image.fromarray(result, mode="L")


def main():
    """ entry point of the script."""
    frames_folder = "frames"
    output_folder = "out"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    image_paths = [os.path.join(frames_folder, f) for f in os.listdir(
        frames_folder) if os.path.isfile(os.path.join(frames_folder, f))]
    try:
        result_image = xor_images(image_paths)
        output_path = os.path.join(output_folder, "result.png")
        result_image.save(output_path)
        print("Output image saved to: ", output_path)
    except ValueError as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
