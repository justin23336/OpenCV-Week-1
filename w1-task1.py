import cv2 as cv

def main():

  beach = cv.imread("C:\code\OpenCV-Week-1\.git\download.jpeg")

  cv.imshow("Beach", beach) # Show window_

  cv.waitKey(0) # Wait and close window only when key is pressed_

if __name__ == "__main__":

  main()