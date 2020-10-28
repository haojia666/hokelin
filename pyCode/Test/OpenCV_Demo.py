import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from CVMethod import CVMethod

# tf.print('----------------')
# mat0 = tf.zeros([3,4])
# tf.print(mat0)
# tf.print(tf.multiply(data1,data2))

img = cv2.imread('D:\\0.png',1)
imgInfo = img.shape
print('-------------------')
print(imgInfo)

#cv2.namedWindow('name',cv2.WINDOW_NORMAL)
#测试缩放功能
# dst = CVMethod.reSize(img,0.7,0.7)

scale = np.float32([[0.5,0,0],[0,0.5,0]])
dst = cv2.warpAffine(img,scale,(int(img.shape[1]/2),int(img.shape[0]/2)))
print(dst.shape)
cv2.imshow('name',dst)
cv2.waitKey(0)


    