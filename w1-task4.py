import cv2 as cv
import matplotlib.pyplot as plt

def main():
    beach = cv.imread("C:\code\OpenCV-Week-1\.git\download.jpeg")
    beach = cv.cvtColor(beach, cv.COLOR_BGR2GRAY)

    plt.imshow(beach)
    plt.show()

if __name__ == "__main__":
    main()
