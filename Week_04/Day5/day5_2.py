import cv2
import numpy as np
from tqdm import tqdm

image = cv2.imread('./sample_image/IMG_0033.jpeg', cv2.IMREAD_GRAYSCALE)
before_image = image.copy()

MAX_PIXEL = 255


def mat_access(mat):
    pbar = tqdm(total=mat.shape[0] * mat.shape[1])

    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            # k = mat[i, j]  # 원소 접근 - mat1[i][j] 방식도 가능
            # mat[i, j] = MAX_PIXEL - k  # 원소 할당
            k = mat.item(i, j)  # 원소 접근
            mat.itemset((i, j), MAX_PIXEL - k)  # 원소 할당
            pbar.update(1)

    pbar.close()


mat_access(image)

cv2.imshow('gray', np.hstack([before_image, image]))
cv2.waitKey()
