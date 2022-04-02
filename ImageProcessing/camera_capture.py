import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray, 64, 127)
        
        cv2.imshow('frame', edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()