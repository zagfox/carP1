import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Read in the image and convert to grayscale
image = mpimg.imread('test_images/solidWhiteCurve.jpg')

plt.imshow(image)
