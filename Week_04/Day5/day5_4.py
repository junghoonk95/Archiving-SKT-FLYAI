import cv2
import numpy as np

'''
15 by 10 특정한 구역의 값을 프린트하세요
'''

if __name__ == "__main__":
    image = cv2.imread('./IMG_0033.jpeg', cv2.IMREAD_GRAYSCALE)

    x = int(np.random.randint(0, image.shape[1], 1))
    y = int(np.random.randint(0, image.shape[0], 1))

    roi = image[y:y+150, x:x+100]

    for i in range(roi.shape[1]):
        for j in range(roi.shape[0]):
            print(roi[j, i], end=' ')
        print()

    cv2.imshow('title', roi)
    cv2.waitKey()
