import cv2 as cv
import numpy as np
from skimage import img_as_float, img_as_ubyte

def show(final):
       print('display')
       cv.imshow('Temple', final)
       cv.waitKey(0)

def white_balance(img):
       result = cv.cvtColor(img, cv.COLOR_BGR2LAB)
       avg_a = np.average(result[:, :, 1])
       avg_b = np.average(result[:, :, 2])
       result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
       result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
       result = cv.cvtColor(result, cv.COLOR_LAB2BGR)
       return result

def auto_wite(img):
       img = img_as_float(img)
       N = img.size / 3
       R = np.sum(img[:, :, 0]) / N
       G = np.sum(img[:, :, 1]) / N
       B = np.sum(img[:, :, 2]) / N
       Avg = np.average([R, G, B])
       rw = R / Avg
       gw = G / Avg
       bw = B / Avg
       del N, R, G, B, Avg
       img[:, :, 0] /= rw
       img[:, :, 1] /= gw
       img[:, :, 2] /= bw
       img = np.clip(img, 0, 1)
       img = img_as_ubyte(img)
       return img

def balanceWhite_GrayworldWB(img, k = 0.99):
       wb = cv.xphoto.createGrayworldWB()
       wb.setSaturationThreshold(k)
       return wb.balanceWhite(img)

def balanceWhite_LearningBasedWB(img, k = 0.99):
       wb = cv.xphoto.createLearningBasedWB()
       wb.setSaturationThreshold(k)
       return wb.balanceWhite(img)
def nothing():
       pass
def brightness(img):
    cv.namedWindow('image')
    cv.createTrackbar('val', 'image', 100, 150, nothing)

    while True:
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        hsv = np.array(hsv, dtype=np.float64)
        val = cv.getTrackbarPos('val', 'image')
        val = val/100 # dividing by 100 to get in range 0-1.5

        # scale pixel values up or down for channel 1(Saturation)
        hsv[:, :, 1] = hsv[:, :, 1] * val
        hsv[:, :, 1][hsv[:, :, 1] > 255] = 255 # setting values > 255 to 255.
        # scale pixel values up or down for channel 2(Value)
        hsv[:, :, 2] = hsv[:, :, 2] * val
        hsv[:, :, 2][hsv[:, :, 2] > 255] = 255 # setting values > 255 to 255.

        hsv = np.array(hsv, dtype=np.uint8)
        res = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

        cv.imshow("original", img)
        cv.imshow('image', res)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cv.destroyAllWindows()
def sepia(img):
    res = img.copy()
    res = cv.cvtColor(res, cv.COLOR_BGR2RGB) # converting to RGB as sepia matrix is for RGB
    res = np.array(res, dtype=np.float64)
    res = cv.transform(res, np.matrix([[0.393, 0.769, 0.189],
                                        [0.349, 0.686, 0.168],
                                        [0.272, 0.534, 0.131]]))
    res[np.where(res > 255)] = 255 # clipping values greater than 255 to 255
    res = np.array(res, dtype=np.uint8)
    res = cv.cvtColor(res, cv.COLOR_RGB2BGR)
    
    cv.imshow("Sepia", res)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
img = cv.imread('15.dng')
h, w, _ = img.shape
##img = cv.resize(img, (w//5, h//5))
cv.imshow("original", img)

cv.imshow('white_balance', white_balance(img))
cv.imshow('GrayworldWB', balanceWhite_GrayworldWB(img))
##cv.imshow('LearningBasedWB', )
cv.imshow('LearningBasedWB', balanceWhite_LearningBasedWB(img))
cv.imshow('auto_wite', auto_wite(img))
##cv.imshow('', )


##sepia(auto_wite(white_balance(img)))

##cv.imwrite('test2/ORIGIN.jpg', img)
##cv.imwrite('test2/white_balance.jpg', white_balance(img))
##cv.imwrite('test2/GrayworldWB.jpg', balanceWhite_GrayworldWB(img))
##cv.imwrite('test2/LearningBasedWB.jpg', balanceWhite_LearningBasedWB(img))
##cv.imwrite('test2/auto_wite.jpg', auto_wite(img))
##cv.imwrite('test2/LearningBasedWB_0.99.jpg', balanceWhite_LearningBasedWB(img))
##cv.imwrite('test2/LearningBasedWB_0.75.jpg', balanceWhite_LearningBasedWB(img, 0.75))
##cv.imwrite('test2/LearningBasedWB_0.5.jpg', balanceWhite_LearningBasedWB(img, 0.5))
##cv.imwrite('test2/LearningBasedWB_0.25.jpg', balanceWhite_LearningBasedWB(img, 0.25))

