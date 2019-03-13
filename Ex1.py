import cv2
import numpy as np
#from pynput.keyboard import Key, Controller
#/home/countryyoon/01.jpg

def display_size(img): #이미지의 width, height, depth 왼쪽 상단에 표시
    c_img = img
    w, h, d = c_img.shape
    strr = "w:" + str(w) + ", h:" + str(h) + " ,d:" + str(d)
    cv2.putText(c_img, strr, (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0))
    cv2.imshow('imageNsize', c_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def gray_scale(img): #회색조 이미지로 변경
    c_img = img
    img_gray = cv2.cvtColor(c_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('imageNgray', img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def original_image(img): #원래 이미지 표시
    c_img = img
    cv2.imshow('image', c_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def mosaic_image(img): #모자이크 이미지
    size_x = int(input("가로 블럭 수: "))
    size_y = int(input("세로 블럭 수: "))

    height, width, depth = img.shape
    org_img = np.zeros_like(img)

    pixel_x = int(width/size_x)
    pixel_y = int(height/size_y)

    mean_method = input("1-평균값, 2-중간값, 3-중심화소값: ")

    if mean_method == '1': #평균값으로 모자이크
        for i in range(size_x):
            for j in range(size_y):
                x_start = round(i * pixel_x)
                x_end = round((i + 1) * pixel_x)
                y_start = round(j * pixel_y)
                y_end = round((j + 1) * pixel_y)
                cropped_r = img[x_start:x_end, y_start:y_end, 0]
                cropped_g = img[x_start:x_end, y_start:y_end, 1]
                cropped_b = img[x_start:x_end, y_start:y_end, 2]
                block = np.zeros_like(org_img[x_start:x_end, y_start:y_end])
                block[0:x_end, 0:y_end] = np.mean(cropped_r, dtype=int), np.mean(cropped_g, dtype=int), np.mean(
                    cropped_b, dtype=int)
                cv2.putText(block, str(i) + "," + str(j), (int(pixel_y / 2), int(pixel_x / 2)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
                org_img[x_start:x_end, y_start:y_end] = block

    elif mean_method == '2': #중간값으로 모자이크
        for i in range(size_x):
            for j in range(size_y):
                x_start = round(i * pixel_x)
                x_end = round((i + 1) * pixel_x)
                y_start = round(j * pixel_y)
                y_end = round((j + 1) * pixel_y)
                cropped_r = img[x_start:x_end, y_start:y_end, 0]
                cropped_g = img[x_start:x_end, y_start:y_end, 1]
                cropped_b = img[x_start:x_end, y_start:y_end, 2]
                block = np.zeros_like(org_img[x_start:x_end, y_start:y_end])
                block[0:x_end, 0:y_end] = np.median(cropped_r), np.median(cropped_g), np.median(cropped_b)
                cv2.putText(block, str(i) + "," + str(j), (int(pixel_y / 2), int(pixel_x / 2)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
                org_img[x_start:x_end, y_start:y_end] = block

    elif mean_method == '3': #중심화소값으로 모자이크
        for i in range(size_x):
            for j in range(size_y):
                x_start = round(i * pixel_x)
                x_end = round((i + 1) * pixel_x)
                y_start = round(j * pixel_y)
                y_end = round((j + 1) * pixel_y)
                cropped_r = img[int((x_start + x_end) / 2), int((y_start + y_end) / 2), 0]
                cropped_g = img[int((x_start + x_end) / 2), int((y_start + y_end) / 2), 1]
                cropped_b = img[int((x_start + x_end) / 2), int((y_start + y_end) / 2), 2]
                block = np.zeros_like(org_img[x_start:x_end, y_start:y_end])
                block[0:x_end, 0:y_end] = cropped_r, cropped_g, cropped_b
                cv2.putText(block, str(i) + "," + str(j), (int(pixel_y / 2), int(pixel_x / 2)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0))
                org_img[x_start:x_end, y_start:y_end] = block

    cv2.imshow('mosaic_image', org_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def loop_exit(): #루프종료
    exit()



if __name__ == "__main__":
    path = input("파일명을 입력하세요: ")
    original_img = cv2.imread(path, 1)
    cv2.imshow('image', original_img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    while True:
        #cv2.waitKey()
        k = input()
        if k == 'r':
            display_size(original_img)

        elif k == 'g': #k.press('g'): # k == ord('g'):
            gray_scale(original_img)

        elif k == 'c': #k.press('c'): #k == ord('c'):
            original_image(original_img)

        elif k == 'm': #k.press('m'): #k == ord('m'):
            mosaic_image(original_img)

        elif k == 'q': #k.press('q'): #k == ord('q'):
            loop_exit()

        else:
            pass
