import csv
import os
from PIL import Image

# Define the folder to store images
output_folder = "images"

# Create the folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read the CSV file
csv_filename = "colors.csv"  # Change this if your file has a different name

with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        file_name, color_name, hex_code, r, g, b = row
        r, g, b = int(r), int(g), int(b)  # Convert RGB values to integers
        
        # Create an image with the color
        img = Image.new("RGB", (200, 200), (r, g, b))
        
        # Save the image inside the "images" folder
        img.save(os.path.join(output_folder, f"{file_name}.png"))

print("Images created successfully inside the 'images' folder!")
