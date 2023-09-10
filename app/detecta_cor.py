# Python program to identify
#color in images
  
# Importing the libraries OpenCV and numpy
import cv2
import numpy as np
  
# Read the images
#img = cv2.imread("imagens/shapes.jpg")
img = cv2.imread("images/photo_5118776271898258939_y.jpg")
  
# Resizing the image
#image = cv2.resize(img, (700, 600))
#######
# Get green color
green = np.uint8([[[0, 255, 0]]])
  
# Convert Green color to Green HSV
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
  
# Print HSV Value for Green color
print(hsv_green)
# Encontrado [[[ 60 255 255]]]
lower = [50, 255, 255]
upper = [70, 255, 255]

# Make python sleep for unlimited time
#cv2.waitKey(10 * 10000)

mask = cv2.inRange(hsv_green, lower, upper)

#cv2.imshow("Image", img)
cv2.imshow("Mask", mask)

cv2.waitKey(5 * 1000)
#######
# Convert Image to Image HSV
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
  
# # Defining lower and upper bound HSV values
# lower = np.array([50, 100, 100])
# upper = np.array([70, 255, 255])
  
# # Defining mask for detecting color
# mask = cv2.inRange(hsv, lower, upper)
  
# # Display Image and Mask
# cv2.imshow("Image", image)
# cv2.imshow("Mask", mask)
  
# # Make python sleep for unlimited time
# cv2.waitKey(10 * 1000)