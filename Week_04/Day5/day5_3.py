import time
import cv2
import numpy as np

image = cv2.imread('./sample_image/IMG_0033.jpeg', cv2.IMREAD_GRAYSCALE)


def pixel_access1(image):
    canvas = np.zeros(image.shape[:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            canvas[i, j] = 255 - image[i, j]

    return canvas


def pixel_access2(image):
    tmp = np.zeros(image.shape[:2], image.dtype)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            tmp.itemset((i, j), 255 - image.item(i, j))

    return tmp


def pixel_access3(image):
    lut = [255 - i for i in range(256)]
    lut = np.array(lut, np.uint8)
    return lut[image]


def pixel_access4(image):
    return cv2.subtract(255, image)


def pixel_access5(image):
    return 255 - image


def time_check(func, msg):
    start_time = time.perf_counter()
    ret_img = func(image)
    elapsed = (time.perf_counter() - start_time) * 100
    print(f'{msg} 수행시간: {elapsed:02}ms')
    return ret_img


if __name__ == "__main__":
    time_check(pixel_access1, "[방법1] 직접 접근 방식")
    time_check(pixel_access2, "[방법2] item() 함수 접근 방식")
    time_check(pixel_access3, "[방법3] lookup table 방식")
    time_check(pixel_access4, "[방법4] OpenCV 함수  방식")
    time_check(pixel_access5, "[방법5] ndarray 연산 방식")

