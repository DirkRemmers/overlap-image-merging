import numpy as np
from skimage import io
import os
import matplotlib.pyplot as plt

# load images
image_dir = './images'
files = sorted(os.listdir(image_dir))
images = []
for file_name in files:
    image = io.imread(f"{image_dir}/{file_name}")
    images.append(image)
# plt.imshow(images[0])

# start with the merging
