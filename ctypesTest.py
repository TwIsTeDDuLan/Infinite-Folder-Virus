from PIL import Image
import numpy as np

# Load the image
image_path = 'D:/Test.jpg'
img = Image.open(image_path)

# Convert the image to a numpy array
bitmap = np.array(img)

# Function to convert an RGB tuple to a hexadecimal string
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

# Check if the image is grayscale or RGB
if len(bitmap.shape) == 2:  # Grayscale image
    hex_bitmap = np.vectorize(lambda x: "#{:02x}{:02x}{:02x}".format(x, x, x))(bitmap)
else:  # RGB image
    hex_bitmap = np.apply_along_axis(rgb_to_hex, 2, bitmap)

# Print the first few rows of the hex bitmap for illustration
for row in hex_bitmap[:5]:  # Print only the first 5 rows for brevity
    print(" ".join(row))

