import sys
import os
import numpy as np
from PIL import Image
from operator import itemgetter


path = "train"
folder_names = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
# print(folder_names)

# Each row is an image
img = np.zeros([160, 2025], dtype = float)
labels = np.zeros([160])

j = 0
for i in range(10):
	for image in os.listdir(path + "/" + folder_names[i]):
		train_image = path + "/" + folder_names[i] + "/" + image
		img[j] = np.asarray(Image.open(train_image).convert('L').resize((45,45), Image.ANTIALIAS)).flatten()
		img[j] = img[j] / 255.0
		labels[j] = folder_names[i]
		j += 1
