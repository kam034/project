import os
import cv2
list_files_of_directory = os.listdir(r'C://Users/Admin/Desktop/dataset/walk')
for i in range(0,665):
    filename = "{}{}".format('C://Users/Admin/Desktop/dataset/walk/', list_files_of_directory[i])
    img = cv2.imread(filename)
    img = cv2.resize(img,(640,480))
    output_path = "{}{}{}".format('C://Users/Admin/Desktop/data/walk/', i, '.jpg')
    cv2.imwrite(output_path,img)
