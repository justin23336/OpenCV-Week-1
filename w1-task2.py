import cv2 as cv

import cv2 as cv

capture = cv.VideoCapture("C:\code\OpenCV-Week-1\y2mate.is - Gandalf laugh !!!!haha-fjUO7xaUHJQ-720p-1691718045.mp4")

while True:

  retval, frame = capture.read() # retval is bool for successful read_

  # Exit loop once end of the video is reached_

  if not retval:

    break

  cv.imshow("Display name", frame)

  if cv.waitKey(17) ==ord('d'): # Close if 'd' is pressed_

    break

capture.release()

cv.destroyAllWindows()