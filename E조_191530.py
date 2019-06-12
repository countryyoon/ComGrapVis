import cv2
import numpy as np
import math


def mouse_callback(event, x, y, flags, param): #추적하고 싶은 물체 지정
    global pause, frame, sx, sy, roi

    if pause==False and event==1: #멈추고 있고, 마우스 눌렀을때 시작위치
        sx, sy = x, y

    elif pause==False and event == 4: #멈추고 있고 마우스 땠을때 마지막 위치
        roi = frame[sy:y, sx:x]
        cv2.imshow('roi', roi) #지정한 부분 새창으로 띄움
        pause = True #동영상 시작하도록 변수 True로 바꾸어줌


windowName = "Find Matching Video"
cv2.namedWindow(windowName)
pause = False


def main():
    global frame, roi, pause
    
    # SIFT선언, 루프 안에서 선언하면 계산의 낭비이므로 밖에서 미리 정해주고 들어감
    sift = cv2.xfeatures2d.SIFT_create()
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    
    #동영상 읽기
    filename = "1st_school_tour_researchcenter.avi"
    cap = cv2.VideoCapture(filename)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    
    # 동영상 크기 조정
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 360), interpolation=cv2.INTER_AREA)
    cv2.imshow(windowName, frame)
    
    while ret:
        if pause: #pause가 true일때만 동영상 재생
            ret, frame = cap.read()
            frame = cv2.resize(frame, (640, 360), interpolation=cv2.INTER_AREA)
            
            # 매칭 계산 시작
            kp1, des1 = sift.detectAndCompute(roi, None)
            kp2, des2 = sift.detectAndCompute(frame, None)
 
            matches = flann.knnMatch(des1, des2, k=2)
            
            good = []
            for m,n in matches:
                if m.distance < 0.6*n.distance:
                    good.append(m)
                    
            if len(good)==0: # 만약 재생중인 동영상에 지정한 부분과 매칭되는 객체가 더이상 없으면 
                pause=False # pause가 False이므로 영상이 멈추고 다시 지정할 수 있음
                cv2.destroyWindow('roi') #멈추면 roi창과
                cv2.destroyWindow('result') #매칭result창이 꺼지도록 
            
            if len(good)>4:
                src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
                dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
                
                M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                
                if M is not None :     
                    h, w = roi.shape[:2]
                    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
                    dst = cv2.perspectiveTransform(pts,M)
                    pt1=(dst[0][0][0], dst[0][0][1]) # 구한 매칭의 양 대각선 꼭짓점
                    pt2=(dst[2][0][0], dst[2][0][1])
                    mid = ((int)((pt1[0] + pt2[0])/2), (int)((pt1[1] + pt2[1])/2)) #중점
                    rad = (int)(math.sqrt(math.pow(pt1[0]-pt2[0], 2) + math.pow(pt1[1]-pt2[1], 2)) / 2) #반지름
                    #area = w*h                    
                    if abs(pt1[0]-pt2[0]) > (1.2*w) or abs(pt1[1]-pt2[1])>(1.2*h): #기존의 매칭과 너무 다른 비율이 detection되면 오류로 처리하고 표시하지 않음
                        pass
                    else:
                        frame = cv2.circle(frame, mid, rad, (0, 255, 255), 2) # detection 성공
                else:
                    pass
            
                img3 = cv2.drawMatches(roi, kp1, frame, kp2, good, None, (0, 0, 255), flags=2) #매칭 키포인트 연결선 보이게 출력
                cv2.imshow('result', img3)
            cv2.imshow(windowName, frame)
            
        if cv2.waitKey(1) == 27: #종
            break

    cv2.destroyAllWindows()
    cap.release()
   
cv2.setMouseCallback(windowName, mouse_callback)
    
if __name__ == "__main__":
    main()
