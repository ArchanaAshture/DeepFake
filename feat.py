import sqlite3

import cv2
from matplotlib import pyplot as plt
# Reading color image as grayscale
from skimage.filters import prewitt_h, prewitt_v

conn = sqlite3.connect('Form.db')
with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM imgsave")
    rows = cursor.fetchall()
    for row in rows:
        filename = row[0]

# reading the image
image2 = cv2.imread(filename, 0)

from skimage import filters, feature

# prewitt kernel
pre_hor = prewitt_h(image2)
pre_ver = prewitt_v(image2)

# Sobel Kernel
ed_sobel = filters.sobel(image2)

# canny algorithm
can = feature.canny(image2)

cv2.imshow("img", pre_ver)
cv2.waitKey(0)