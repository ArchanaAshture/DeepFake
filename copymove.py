import glob
import sqlite3
from tkinter import messagebox
import cv2
from PIL import Image
import imagehash
ctr=0
cutoff = 5
conn = sqlite3.connect('Form.db')
with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM imgsave")
    rows = cursor.fetchall()
    for row in rows:
        filename = row[0]

ctr1=0
ctr2=0
for f in glob.iglob("img\\fake\\*"):
  hash0 = imagehash.average_hash(Image.open(filename))
  hash1 = imagehash.average_hash(Image.open(f))
  x = hash0 - hash1

  if x<=cutoff:
      ctr1=1
      break


for f in glob.iglob("img\\real\\*"):
  hash0 = imagehash.average_hash(Image.open(filename))
  hash1 = imagehash.average_hash(Image.open(f))
  x = hash0 - hash1

  if x<=cutoff:
      ctr2=1
      break


if ctr1==1:
       messagebox.showinfo("Forgery","Fake")
else:

    messagebox.showinfo("Forgery", "Real")









