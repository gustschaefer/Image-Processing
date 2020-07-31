import cv2 
import os
import glob

all_not_resized = []
all_resized = []

def check_dir (path):
	if os.path.isdir(path) == False:
		return False

	else:
		return True

def processed_image (file_name, classes):
	name = file_name[0] # nome da image (imagem.jgp)
	classe = file_name[0][0] # primeira letra da image (H, S ou Z)
	for prefix in classes:
		if classe == prefix[0]: # Confere com qual prefixo a imagem bate
			classe = prefix
	formated_line = ''.join([name,', ' ,classe]) # formata para nome, classe
	all_resized.append(formated_line)

def unprocessed_image (file_name, shape):
	name = file_name[0] # nome da image (imagem.jgp)
	classe = file_name[0][0] # primeira letra da image (H, S ou Z)
	formated_line = ''.join([name,', ' , str(shape)])
	all_not_resized.append(formated_line)

def resize (input_dir, new_dir, new_size, min_size, classes):
	folderlen = len(input_dir)
	for img in glob.glob(input_dir + "/*.jpg"):
		image = cv2.imread(img)
		file_name = os.path.splitext(os.path.basename(img))

		width, height = image.shape[1::-1]
		shape = image.shape[1::-1]

		if width > min_size or height > min_size:
			if height > min_size and width < min_size:
				image = cv2.resize(image, (width, min_size))

			elif width > min_size and height < min_size:
				image = cv2.resize(image, (min_size, height))

			elif width > min_size and height > min_size:
				image = cv2.resize(image, new_size)

			processed_image(file_name, classes)

		else:
			unprocessed_image(file_name, shape)

		cv2.imwrite(new_dir + img[folderlen:], image)

	'''all_resized = '\n'.join(all_resized)
	all_not_resized = '\n'.join(all_not)'''

	return '\n'.join(all_resized), '\n'.join(all_not_resized)


def create_txt (txt_name, info_list):
	with open(txt_name, "w") as file:
  		file.write(str(info_list))

