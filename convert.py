from PIL import Image
import os

def convert_to_ico(image_path, output_path):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Resize the image to 256x256 pixels
    image = image.resize((256, 256))

    # Save the image as a .ico file
    image.save(output_path, format='ICO')

# Path to the input folder containing images
input_folder = 'images'

# Path to the output folder where the .ico files will be saved
output_folder = 'outputs'

# Loop through all files in the input folder
for file_name in os.listdir(input_folder):
    # Get the full path to the file
    file_path = os.path.join(input_folder, file_name)

    # Skip if the file is not an image
    if not file_path.endswith('.jpg') and not file_path.endswith('.jpeg') and not file_path.endswith('.png'):
        continue

    # Create the output file path by replacing the extension with .ico
    output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.ico')

    # Convert the image to .ico format and save it
    convert_to_ico(file_path, output_path)
