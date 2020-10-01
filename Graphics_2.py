#Importing the directive
from PIL import Image
#Opening the image
image = Image.open(r'backiee-127383.jpg')
# Height and width
width, height = image.size
#mode of image
mode = image.mode
#get pixel of image
pix_val = image.getpixel((0, 0))
# Printing the values
print("Height :", height, "Width :", width)
print("Mode:", mode)
print("Pixels :", pix_val)
# Showing the image
image.show()
# Display the mode of image

