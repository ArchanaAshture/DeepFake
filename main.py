import cv2
import sqlite3
from tkinter.filedialog import askopenfilename
from matplotlib import pyplot as plt
from tkinter import *
from PIL import ImageTk, Image
import os
root = Tk()
root.geometry('1366x768')
root.title("ImageForgery")
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(2,2, anchor=NW, image=photo)

def readimg():
        os.system("python test1.py")
        ''' filename = askopenfilename(filetypes=[("images", "*.*")])'''
        fn="filename.jpg"
        img = cv2.imread(fn)
        conn = sqlite3.connect('Form.db')
        cursor = conn.cursor()
        cursor.execute('delete from imgsave')
        cursor.execute('INSERT INTO imgsave(img ) VALUES(?)', (fn,))
        conn.commit()
        cv2.imshow("Forgery", img)  # I used cv2 to show image
        cv2.waitKey(0)
        # Reading color image as grayscale
        conn = sqlite3.connect('Form.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM imgsave")
            rows = cursor.fetchall()
            for row in rows:
                filename = row[0]
        gray = cv2.imread(filename, 0)
        # Showing grayscale image
        cv2.imshow("Grayscale Image", gray)
        # waiting for key event
        cv2.waitKey(0)
        # destroying all windows
        cv2.destroyAllWindows()
        img = cv2.imread(filename)
        dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
        cv2.imshow("DeepFake", dst)
        # waiting for key event
        cv2.waitKey(0)
        plt.subplot(121), plt.imshow(img)
        plt.subplot(122), plt.imshow(dst)
        plt.show()


def readimg1():
    #os.system("python test1.py")
    filename = askopenfilename(filetypes=[("images", "*.*")])
    fn = filename
    img = cv2.imread(fn)
    conn = sqlite3.connect('Form.db')
    cursor = conn.cursor()
    cursor.execute('delete from imgsave')
    cursor.execute('INSERT INTO imgsave(img ) VALUES(?)', (fn,))
    conn.commit()
    cv2.imshow("Forgery", img)  # I used cv2 to show image
    cv2.waitKey(0)
    # Reading color image as grayscale
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM imgsave")
        rows = cursor.fetchall()
        for row in rows:
            filename = row[0]
    gray = cv2.imread(filename, 0)
    # Showing grayscale image
    cv2.imshow("Grayscale Image", gray)
    # waiting for key event
    cv2.waitKey(0)
    # destroying all windows
    cv2.destroyAllWindows()
    img = cv2.imread(filename)
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    cv2.imshow("DeepFake", dst)
    # waiting for key event
    cv2.waitKey(0)
    plt.subplot(121), plt.imshow(img)
    plt.subplot(122), plt.imshow(dst)
    plt.show()


def sel():
    os.system("python sel.py")

def fac():
    os.system("python feat.py")
    os.system("python seg.py")

def emo():
    os.system("python face4.py")
def clf():
        os.system("python copymove.py")

Button(root, text='Select Image ', width=40, bg='green', fg='white',  height=2,font=("bold", 10),command=readimg1).place(x=1000, y=250)
Button(root, text='Capture Image & Detect Facial Region ', width=40, bg='green', fg='white',  height=2,font=("bold", 10),command=readimg).place(x=1000, y=300)
Button(root, text='Open Selection', width=40, bg='green', fg='white', height=2,command=sel, font=("bold", 10)).place(x=1000, y=350)
Button(root, text='Feature Extraction & Segmentation', width=40, bg='green', fg='white',command=fac,height=2,  font=("bold", 10)).place(x=1000, y=400)
Button(root, text='Emotion Detection', width=40, bg='green', fg='white',command=emo,height=2,  font=("bold", 10)).place(x=1000, y=450)
Button(root, text='Classifier', width=40, bg='green', fg='white',command=clf,height=2,  font=("bold", 10)).place(x=1000, y=500)

root.mainloop()
