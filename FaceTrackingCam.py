import cv2
import serial

face_cascade = cv2.CascadeClassifier("C:\Libraries\opencv\haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture(0)
frame_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
serial_p = serial.Serial('COM3',9600)
start_angle = 90
serial_p.write(start_angle.to_bytes(1,'big'))


while True:
    cap_success, frame = cap.read()
    if not cap_success:
        break
    grey_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grey_frame = cv2.equalizeHist(grey_frame)
    faces = face_cascade.detectMultiScale(grey_frame,scaleFactor=1.05, minNeighbors=4,minSize=(30,30))
   
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (128, 0, 128), 2)
        center_x = float(x) + (float(w)/2.0)
        center_y = float(y) + (float(h)/2.0)
        x_angle = int(center_x*(180.0/frame_w))
        y_angle = int(center_y*(180.0/frame_h))
        if x_angle != "'" and y_angle != "'":
            print(x_angle, " ", y_angle)
            serial_p.write(x_angle.to_bytes(1,'big'))
            serial_p.write(y_angle.to_bytes(1,'big'))
       
    cv2.imshow('Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()