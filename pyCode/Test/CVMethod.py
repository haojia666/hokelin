import cv2
import numpy as np
import random
class CVMethod(object):
    
    """
    最近领域插值法，进行图片缩放
    :param mat: 原始图片
    :param xScale: X方向缩放比例 0~1
    :param yScale: Y方向缩放比例 0~1
    :return:返回缩放后的图片
    """
    @staticmethod
    def reSize(img,xScale,yScale):
        info = img.shape
        height = int(info[0] * xScale)
        width = int(info[1]*yScale)
        dstImg = np.zeros((height,width,3),np.uint8)
        for i in range(0,height):
            for j in range(0,width):
                iNew = int(i*(info[0]*1.0/height))
                jNew = int(j*(info[1]*1.0/width))
                dstImg[i,j] = img[iNew,jNew]
        return dstImg
    """
    opencv中仿射变换矩阵的使用方法
    """
    @staticmethod
    def GetAffineTrans(sourcePoint,targetPoint):
        return cv2.getAffineTransform(sourcePoint,targetPoint)
        #使用时， cv2.warpAffine(img,matAffine,(width,height))

    @staticmethod
    def Canny(img):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        imgG = cv2.GaussianBlur(gray,(3,3),0)
        dst = cv2.Canny(img,50,50)
        return dst
    """
    视频分解图片，图片保存到本地
    """
    @staticmethod
    def Video2JPG(path):
        cap = cv2.VideoCapture(path)
        if cap.isOpened():
            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            i = 0
            while(True):
                if i == 10:
                    break
                else:
                    i += 1
                (flag,frame) = cap.read()
                fileName = 'image'+str(i)+'.jpg'
                if flag == True:
                    cv2.imwrite(fileName,frame,[cv2.IMWRITE_JPEG_QUALITY,100])
        return cap.isOpened()
