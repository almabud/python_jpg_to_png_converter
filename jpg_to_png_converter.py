import os
import sys
from PIL import Image


if __name__ == "__main__":
    if len(sys.argv) == 2:
        image_folder = sys.argv[1]
        print("Please Enter output folder")
        output_folder = input().strip()
    elif len(sys.argv) == 1:
        print("Please Enter image folder and output folder")
        image_folder, output_folder = input().strip()
    else:
        image_folder = sys.argv[1]
        output_folder = sys.argv[2]
    print("{0!s} {1!s}".format(image_folder, output_folder))
    if not os.path.exists(image_folder):
        print("Image folder not found.")
        exit()
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(image_folder):
        image = Image.open(f'{image_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        image.save(f'{output_folder}{clean_name}.png', 'png')
        print("Done!!")


