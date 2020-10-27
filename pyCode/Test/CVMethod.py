import cv2
import numpy as np
class CVMethod(object):
    
    """
    最近领域插值法，进行图片缩放
    :param mat: 原始图片
    :param xScale: X方向缩放比例 0~1
    :param yScale: Y方向缩放比例 0~1
    :return:返回缩放后的图片
    """
    @staticmethod
    def reSize(mat,xScale,yScale):
        info = mat.shape
        height = int(info[0] * xScale)
        width = int(info[1]*yScale)
        dstImg = np.zeros((height,width,3),np.uint8)
        for i in range(0,height):
            for j in range(0,width):
                iNew = int(i*(info[0]*1.0/height))
                jNew = int(j*(info[1]*1.0/width))
                dstImg[i,j] = mat[iNew,jNew]
        return dstImg