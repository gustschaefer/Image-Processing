import cv2 
import os
import glob
import func as f

input_dir = "C:/resize"
new_dir = "C:/new_dir"
new_size = (710, 405)
min_size = 710

classes = ['Human', 'Skull', 'Zombie']
all_not_resized = []
all_resized = []

if f.check_dir(new_dir) == False:
	os.mkdir(new_dir)

all_resized, all_not_resized = f.resize(input_dir, new_dir, new_size, min_size, classes)


f.create_txt("imagees.txt", all_resized)
f.create_txt("disregarded.txt", all_not_resized)