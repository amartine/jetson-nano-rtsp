import cv2
#print(cv2.__version__)

camSet= 'rtsp://your_rpi_ip:80/live/stream'
cam = cv2.VideoCapture(camSet)

cv2.namedWindow('Camera')
cv2.moveWindow('Camera',800,400)

while (True):
    ret, frame= cam.read()
    cv2.imshow('Camera', frame)
    if (cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
