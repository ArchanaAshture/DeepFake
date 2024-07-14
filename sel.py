#load the xml files for face, eye and mouth detection into the program
import sqlite3

import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

conn = sqlite3.connect('Form.db')
with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM imgsave")
    rows = cursor.fetchall()
    for row in rows:
        filename = row[0]

image = cv2.imread(filename)
#show the original image
cv2.imshow('Original image', image)
cv2.waitKey(100)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(image, 1.4, 4)
for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    roi_gray = gray_image[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(gray_image, 1.3, 5)
    mouth = mouth_cascade.detectMultiScale(gray_image, 1.5, 11)
for(ex, ey, ew, eh) in eyes:
           cv2.rectangle(image,(ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
for(mx, my, mw, mh) in mouth:
       cv2.rectangle(image, (mx, my), (mx+mw, my+mh), (255, 0, 0), 2)
cv2.imshow('face, eyes and mouth detected image', image)
cv2.waitKey()