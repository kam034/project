import os
import cv2
from PIL import Image
import numpy as np

list_files_of_directory = os.listdir(r'C://Users/Admin/Desktop/data/gallop')
for i in range(0,580):
    filename = "{}{}".format('C://Users/Admin/Desktop/data/gallop/', list_files_of_directory[i])
    img = cv2.imread(filename)
    img = np.array(img)
    flipped_img = np.fliplr(img)
    output_path = "{}{}{}".format('C://Users/Admin/Desktop/data/gallop/', i, '_1.jpg')
    cv2.imwrite(output_path,flipped_img)

