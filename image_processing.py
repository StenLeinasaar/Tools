from PIL import Image, ImageEnhance, ImageFilter
import os

"""

Basic tool to edit that can allow quick edits for a group of photos. Once I have a need for certain edits, I can modify the code and run it. 

This is just for practice to test some of the capabilities of the Pillow library for python. 

"""

# Specify folder to take photos. 
path = "./images"

# Photos to go after editing.
path_out= "/edited_photos"

# For each file in the folder
for file in os.listdir(path):
    print(f"the file is {file}")
    img = Image.open(f"{path}/{file}")

    # Sharpen and turn it into black and white
    edited = img.filter(ImageFilter.SHARPEN).convert('L')


    # Enhance 
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edited)

    edited =  enhancer.enhance(factor)

    clean_name = os.path.splitext(file)[0]
    
    edited.save(f".{path_out}/{clean_name}_edited.jpg")


    # Create a thumbnail as well of size 128,128

    size = 128, 128

    edited = img.thumbnail(size)

    clean_name = os.path.splitext(file)[0]

    img.save(f".{path_out}/{clean_name}_thumbnail.jpg")


