import cv2
import numpy as np
import imutils

windowName1 = 'Original Image'
windowName2 = 'License Plate'
cv2.namedWindow(windowName1)
cv2.namedWindow(windowName2)

# 읽을 파일명
sample_name = ['S01.jpg', 'S02.jpg', 'S03.jpg', 'S04.jpg', 'S05.jpg'] #'S06.jpg', 'S07.jpg', 'S08.jpg', 'S09.jpg', 'S10.jpg',
               #'S11.jpg', 'S12.jpg', 'S13.jpg', 'S14.jpg', 'S15.jpg'

# 번호판 검출 반복문
for i in range(len(sample_name)):
    # 사진 읽어온 후 크기조정
    path = sample_name[i]
    img = cv2.imread(path, 1)
    img = cv2.resize(img, (720, 540), interpolation=cv2.INTER_AREA)
    
    # 사진 전처리
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 9, 75, 75) #양방향필터처리
    mask = np.zeros(gray.shape, np.uint8) #에러시 띄울 창
    
    # 에러처리
    try:
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) #사각형 추출 필터
        morph_image = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=15) #모폴로지 필터 씌우기
        sub_morp_image = cv2.subtract(gray, morph_image) # 사각형만 보이게
        
        # contouring
        edged = cv2.Canny(sub_morp_image, 50, 300, L2gradient=False) #캐니에지추출
        cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #컨투어 객체 추출
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
        screenCnt = None
    
        # 번호판 찾기
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018*peri, True)
            if len(approx) == 4:
                screenCnt = approx
                break
    
        # 번호판 감지 확인    
        if screenCnt == None:
            detected = 0
        else:
            detected = 1
                
        # 번호판 정상 변환
        if detected == 1:  #감지된 번호판이 있을 시          
            x0, y0 = screenCnt[0][0]
            x1, y1 = screenCnt[1][0]
            x2, y2 = screenCnt[2][0]
            x3, y3 = screenCnt[3][0]
            
            a = [[x0, y0], [x1, y1], [x2, y2], [x3, y3]]
            a.sort()
            a1 = a[:2]
            a2 = a[2:]
            a1.sort(key=lambda x:x[1])
            a2.sort(key=lambda x:x[1])
            anew=a1+a2
            
            point1 = np.float32(anew)
            point2 = np.float32([[0, 0], [0, 75], [300, 0], [300, 75]])
            P = cv2.getPerspectiveTransform(point1, point2)
            output = cv2.warpPerspective(img, P, (300, 75))
        else: #감지된 번호판이 없을 시
            output = mask
            output = cv2.resize(output, (300, 75))
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(output, 'No License Plate', (10, 40), font, 1, (255, 255, 255))
       
    except: # 에러감지시 
        output = mask
        output = cv2.resize(output, (300, 75))
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(output, 'Error!', (10, 40), font, 1, (255, 255, 255))
            
    cv2.imshow(windowName1, img)
    cv2.imshow(windowName2, output)
    cv2.waitKey(0)

cv2.destroyAllWindows()