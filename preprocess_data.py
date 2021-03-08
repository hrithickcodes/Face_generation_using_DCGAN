"""
To preprocess the celerity faces dataset
"""
import numpy as np
import cv2
import os
from tqdm import tqdm 
import random


def make_npy_file(datapath, savepath, image_shape, face_limit = 60_000):
	# faces will get appended in the below list
	face_images = []
	# to get a progress bar
	face_image_files = os.listdir(datapath)
	random.shuffle(face_image_files)
	
	pbar = tqdm(total = face_limit)
	count = 0
	for faces in face_image_files:
		face_path = os.path.join(datapath, faces)
		pbar.update(n = 1)
		face = cv2.imread(face_path)
		face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
		resizedRGBface = cv2.resize(face, image_shape, interpolation = cv2.INTER_AREA)
		face_images.append(resizedRGBface)
		count += 1
		if count == face_limit:
			break
		
	pbar.close()
	face_images = np.array(face_images)
	# saving the npy file
	saver_path = os.path.join(savePath, "celebrity_faces.npy")
	np.save(saver_path, face_images)
	print(f"File saved at : {savepath}")

# Paths
dataPath = os.path.join(os.getcwd(), "data/face_image_data/img_align_celeba")
savePath = os.path.join(os.getcwd(), "data/preprocessed_data")

make_npy_file(datapath = dataPath,
			  savepath = savePath,
			  image_shape = (64,64),
			  face_limit= 60_000)
