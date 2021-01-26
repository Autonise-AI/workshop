import matplotlib.pyplot as plt
import cv2
from PIL import Image

x = Image.open('image.jpg')  # Returns an Image object
print(x.size)  # (310, 310)

x = cv2.imread('image.jpg')  # Returns a numpy array in the BGR format
print(x.shape)  # (310, 310, 3)

x = plt.imread('image.jpg')  # Returns a numpy array in the RGB format
print(x.shape)  # (310, 310, 3)

plt.imshow(x)
plt.show()

import numpy as np

np.linalg.norm