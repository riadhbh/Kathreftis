import pandas as pd
import cv2
import numpy as np


dataset_path = 'data_set/fer2013/fer2013.csv'
size=(48,48)

def load_data():
		data = pd.read_csv(dataset_path)
		pixels = data['pixels'].tolist()
		w, h = 48, 48
		faces = []
		for pixel_sequence in pixels:
			try:
				face = [int(float(pixel)) for pixel in pixel_sequence.split(' ')]
			except ValueError:
				continue
			face = np.asarray(face).reshape(w, h, 1)
			face = cv2.resize(face.astype('uint8'),size)
			faces.append(face.astype('float32'))
			faces = np.asarray(faces)
			faces = np.expand_dims(faces, -1)
			emotions = pd.get_dummies(data['emotion']).as_matrix()
			return faces, emotions

def treatData(x):
	x = x.astype('float32')
	x = x / 255.0
	x = x - 0.5
	x = x * 2.0
	return x