import numpy as np, cv2
image = np.zeros((300, 400, 3), np.uint8)
image[:] = (255, 255, 255)
pt1, pt2 = (50, 130), (200, 300)
cv2.line(image, pt1, (100, 200), (255,0,0) )
cv2.line(image, pt2, (100, 200), (100, 100, 100))
cv2.rectangle(image, pt1, pt2, (255, 0, 255))
cv2.rectangle(image, pt1, pt2, (0, 0, 255))
title = "Line & Rectangle"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
