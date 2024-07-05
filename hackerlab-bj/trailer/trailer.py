#!/usr/bin/python3
from PIL import Image
import numpy as np
import os

def xor_images(image_paths):
    result = np.array(Image.open(image_paths[0]).convert("L"))
    for path in image_paths[1:]:
        img = np.array(Image.open(path).convert("L"))
        result = np.bitwise_xor(result, img)
        return Image.fromarray(result, mode="L")

def main():
    frames_folder = "frames"
    output_folder = "out"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    image_paths = [os.path.join(frames_folder, f) for f in os.listdir(frames_folder) if os.path.isfile(os.path.join(frames_folder, f))]
    try:
        result_image = xor_images(image_paths)
        output_path = os.path.join(output_folder, "result.png")
        result_image.save(output_path)
        print("Output image saved to: ", output_path)
    except ValueError as e:
        print("Error: ", e)

if __name__ == "__main__":
    main()
