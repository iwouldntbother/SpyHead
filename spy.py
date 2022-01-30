import cv2
import sys

cascPath = './haarcascade_frontalface_alt.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
  ret, frame = video_capture.read()

  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  frame_gray = cv2.equalizeHist(frame_gray)

  faces = faceCascade.detectMultiScale(frame_gray)

  for (x, y, w ,h) in faces:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

  cv2.imshow('Video', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video_capture.release()
cv2.destroyAllWindows()