import sqlite3

import cv2     # tensorflow==1.14.0, opencv-python

import argparse
import numpy as np
#from keras.models import model_from_json
#from keras.preprocessing import image
#from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.saving.model_config import model_from_json

json_file = open('top_models\\fer.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

# Load weights and them to model
model.load_weights('top_models\\fer.h5')

classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

import glob

conn = sqlite3.connect('Form.db')
cursor = conn.cursor()
with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM imgsave")
    rows = cursor.fetchall()
    for row in rows:
        filename = row[0]


img = cv2.imread(filename)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces_detected = classifier.detectMultiScale(gray_img, 1.18, 5)

for (x, y, w, h) in faces_detected:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray_img[y:y + w, x:x + h]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        img_pixels = img.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255.0

        predictions = model.predict(img_pixels)
        max_index = int(np.argmax(predictions))

        emotions = ['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear']
        predicted_emotion = emotions[max_index]

        cv2.putText(img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

resized_img = cv2.resize(img, (200,200))
cv2.imshow('Facial Emotion Recognition', resized_img)

if cv2.waitKey(1000) :
     cv2.destroyAllWindows()
