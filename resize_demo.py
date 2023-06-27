#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Quick and dirty code for my blog at **** add post here ****
"""

import cv2
import numpy

# Load in our input image
input_image = cv2.imread("1330-sole-fish.jpg")

# Get the dimensions of the original image 
height, width, channels = input_image.shape

# Print out the dimensions
print(f"Image Width: {width} Height: {height}")

# Display the original image to the user
cv2.imshow("Original Image", input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Now we do a "dumb" image resizing.  Here we simple take each pixel
# and double it in the X- and Y-directions.

# First create an empty image twice the size of the original
empty_mat = numpy.zeros((height * 2, width * 2, channels), dtype=numpy.uint8)

# Now loop through to effectively double the image.  Here we use loops
# so it's easier to understand what we're doing.
for y in range(height):
    for x in range(width):
        pixel = input_image[y, x]
        empty_mat[y * 2, x * 2] = pixel
        empty_mat[y * 2, x * 2 + 1] = pixel
        empty_mat[y * 2 + 1, x * 2] = pixel
        empty_mat[y * 2 + 1, x * 2 + 1] = pixel

# Now display both the original and the doubled image to compare.
cv2.imshow("Original Image", input_image)
cv2.imshow("Doubled Image", empty_mat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Now we use OpenCV's resize function and interpolation methods to resize an image.
# First we use a simple linear interpolation
double_width = width * 2
double_height = height * 2
linear_double_image = cv2.resize(input_image, (double_width, double_height), interpolation=cv2.INTER_LINEAR)

# Now display both the original and the linear interpolated image to compare.
cv2.imshow("Original Image", input_image)
cv2.imshow("Linear Interpolated image", linear_double_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Linear interpolation to quad size
quad_width = width * 4
quad_height = height * 4
linear_quad_image = cv2.resize(input_image, (quad_width, quad_height), interpolation=cv2.INTER_LINEAR)

# Now display both the original and the linear interpolated image to compare.
cv2.imshow("Original Image", input_image)
cv2.imshow("Linear Interpolated 4x image", linear_quad_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Cubic interpolation
cubic_quad_image = cv2.resize(input_image, (quad_width, quad_height), interpolation=cv2.INTER_CUBIC)

# Now display both the original and the linear interpolated image to compare.
cv2.imshow("Original Image", input_image)
cv2.imshow("Cubic Interpolated 4x image", cubic_quad_image)
cv2.waitKey(0)
cv2.destroyAllWindows()