import cv2 as cv

def rescale(frame: cv.Mat, scale:float) : #-\> cv.Mat :

  height =int(frame.shape[0] * scale)

  width =int(frame.shape[1] * scale)

  dim = (width, height)

  return cv.resize(frame, dim, interpolation=cv.INTER_AREA)
                   
img = cv.imread("C:\code\OpenCV-Week-1\.git\download.jpeg")

img_resize = rescale(img, 0.5)

cv.imshow("Image", img_resize)

cv.waitKey(0)