import cv2 
import os
import glob

input_dir = "C:/PATH"
new_dir = "C:/RESIZE"
new_size = (1920, 1080)

if os.path.isdir(new_dir) == False:
	os.mkdir(new_dir) 

folderlen = len(input_dir)
for img in glob.glob(input_dir + "/*.jpg"):
	image = cv2.imread(img)
	image = cv2.resize(image, new_size)
	cv2.imwrite(new_dir + img[folderlen:], image)
	cv2.imshow('image', image)
	cv2.waitKey(50)
cv2.destroyAllWindows()