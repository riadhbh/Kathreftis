from keras.preprocessing.image import img_to_array
#import pandas
import csv
import imutils
import cv2
from keras.models import load_model
import numpy as np

em_count=[0,0,0,0,0,0,0]
em_sum=[0,0,0,0,0,0,0]
em_avg=[0,0,0,0,0,0,0]

Learning_model_path = 'trace_face/haarcascade_frontalface_default.xml'
emotion_model_path = 'models/_mini_XCEPTION.102-0.66.hdf5'


Capture = cv2.CascadeClassifier(Learning_model_path)
trained_classifier = load_model(emotion_model_path, compile=False)
EMOTIONS = [ "neutral", "happy","surprised","angry" ,"disgust","scared", "sad"]


feelings_faces = []
for index, emotion in enumerate(EMOTIONS):
	feelings_faces.append(cv2.imread('feelings_faces/' + emotion + '.png', -1))

cv2.namedWindow('Welcome in FIS')
camera = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video_writer = cv2.VideoWriter('Candidate.m4v', fourcc, 30.0, (640, 480))


def optimizeMetrics():
	global em_avg
	sum = 0
	for i in range(7):
	 sum+=em_avg[i]
	if(sum<100):
		minpos=0
		minval=100
		for i in range(7):
			if(em_avg[i]<minval):
				minval=em_avg[i]
				minpos=i
		em_avg[minpos]+=(100-sum)
	elif (sum>200):
		maxpos=0
		maxval=0
		for i in range(7):
			if(em_avg[i]>maxval):
				maxval=em_avg[i]
				maxpos=i
		em_avg[maxpos]+=(100-sum)


while True:
	(grabbed,frame) = camera.read()
	frame = cv2.resize(frame, (640,480))
	key = cv2.waitKey(33) & 0xFF 
	video_writer.write(frame)
	if key==27:
		 break;
	frame = imutils.resize(frame,width=800)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = Capture.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(40,40),flags=cv2.CASCADE_SCALE_IMAGE)
	
	canvas = np.zeros((250, 300, 3), dtype="uint8")
	frameClone = frame.copy()
	if len(faces) > 0:
		faces = sorted(faces, reverse=True,
		key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
		(fX, fY, fW, fH) = faces
		var = gray[fY:fY + fH, fX:fX + fW]
		var = cv2.resize(var, (64, 64))
		var = var.astype("float") / 255.0
		var = img_to_array(var)
		var = np.expand_dims(var, axis=0)
		
		
		preds = trained_classifier.predict(var)[0]
		label = EMOTIONS[preds.argmax()]

	else:
		continue
	
	for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
				text = "{}: {:.2f}%".format(emotion, prob * 100)
				
				# draw the label + probability bar on the canvas
				em_count[i]+=1
				em_sum[i]+=prob
				em_avg[i]=round((em_sum[i]/em_count[i])*100)
				
				if(i==6):
					with open(r'report.csv', 'w', newline='') as csvfile:
						out = csv.writer(csvfile)
						for j in range(7):
							optimizeMetrics()
							data = [EMOTIONS[j], em_avg[j]]
							out.writerow(data)
				
				emoji_face = feelings_faces[np.argmax(preds)]
				w = int(prob * 300)
				cv2.rectangle(canvas, (7, (i * 35) + 5),
				(w, (i * 35) + 35), (10,255,10), -1)
				cv2.putText(canvas, text, (10, (i * 35) + 23),
				cv2.FONT_HERSHEY_SIMPLEX, 0.45,
				(255, 255, 255), 2)
				cv2.putText(frameClone, label, (fX, fY - 10),
				cv2.FONT_HERSHEY_SIMPLEX, 0.45, (10,255,10), 2)
				cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
							  (10,255,10), 2)

	cv2.imshow('Candidate profile', frameClone)
	cv2.imshow("Criteria resume", canvas)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

camera.release()
video_writer.release()
cv2.destroyAllWindows()
