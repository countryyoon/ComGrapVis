import cv2
import numpy as np

def main():
    switch = 0
    v_cont = 0
    s_cont = 0

    def callback_v(x):
        nonlocal v_cont
        v_cont = x - 100
        img_remake()

    def callback_s(x):
        nonlocal s_cont
        s_cont = x - 100
        img_remake()

    def callback_switch(x):
        nonlocal switch
        switch = x
        img_remake()

    def img_remake():
        nonlocal switch
        nonlocal v_cont
        nonlocal s_cont
        nonlocal img_ed

        img_ed = cv2.cvtColor(img.astype('uint8'), cv2.COLOR_BGR2HSV)
        img_ed = img_ed.astype('float64')
        h, s, v = cv2.split(img_ed)

        if switch == 0:
            if v_cont >= 0 and s_cont >= 0:
                v[:] = v[:] * (1.0 + 1.0 / 128.0) ** v_cont
                s[:] = s[:] * (1.0 + 1.0 / 128.0) ** s_cont
            elif v_cont >= 0 and s_cont < 0:
                v[:] = v[:] * (1.0 + 1.0 / 128.0) ** v_cont
                s[:] = s[:] * (1.0 - 1.0 / 128.0) ** - s_cont
            elif v_cont < 0 and s_cont >= 0:
                v[:] = v[:] * (1.0 - 1.0 / 128.0) ** - v_cont
                s[:] = s[:] * (1.0 + 1.0 / 128.0) ** s_cont
            elif v_cont < 0 and s_cont < 0:
                v[:] = v[:] * (1.0 - 1.0 / 128.0) ** - v_cont
                s[:] = s[:] * (1.0 - 1.0 / 128.0) ** - s_cont
        else:
            v[:] = v[:] * float(1 + v_cont / 128)
            s[:] = s[:] * float(1 + s_cont / 128)

        print(np.median(s), np.median(v))

        img_ed = cv2.merge((h, s, v))
        np.clip(img_ed, 0, 255, img_ed)
        img_edd = img_ed.astype('uint8')
        img_edd = cv2.cvtColor(img_edd, cv2.COLOR_HSV2BGR)
        cv2.imshow('image', img_edd)

    img = cv2.imread("/home/countryyoon/02.jpg")
    img_ed = img.astype('float64')

    cv2.namedWindow('image')
    cv2.createTrackbar('V 명도 : ', 'image', 100, 200, callback_v)
    cv2.createTrackbar('S 채도 : ', 'image', 100, 200, callback_s)
    cv2.createTrackbar('S or Line : ', 'image', 0, 1, callback_switch)

    cv2.imshow('image', img_ed.astype('uint8'))
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
