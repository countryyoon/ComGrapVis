import cv2
import numpy as np

def emptyFunction():
    pass

def main():
    
    windowName = "Live Video Feed Blending Image"
    cv2.namedWindow(windowName)
    
    cap = cv2.VideoCapture(0)
    cap.set(3, 400)
    cap.set(4, 300)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    alpha = 0.5
    cv2.createTrackbar('Alpha', windowName, 50, 100, emptyFunction)
        
    while ret:
        ret, frame = cap.read()
        
        edge_img = cv2.Canny(frame, 50, 100, L2gradient=False)
        edge_img = cv2.GaussianBlur(edge_img, (3, 3), 0)
        edge_img = cv2.cvtColor(edge_img, cv2.COLOR_GRAY2BGR)

        img = cv2.addWeighted(frame, alpha, edge_img, 1-alpha, 0)
        
        alpha = cv2.getTrackbarPos('Alpha', windowName) / 100
        
        whole = np.hstack((frame, img, edge_img))
        
        #cv2.imshow('edge video', edge_img)
        #cv2.imshow('original', frame)
        #cv2.imshow(windowName, img)
        cv2.imshow(windowName, whole)
        
        if cv2.waitKey(1)==27:
            break
        
    cv2.destroyAllWindows()    
    cap.release()
    
    
if __name__ == "__main__":
    main()
