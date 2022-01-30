import cv2
import serial
import time

arduino = serial.Serial(port='/dev/cu.usbmodem14301', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


cascPath = './haarcascades/haarcascade_frontalface_alt.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

global lastX 
global lastY 
lastX = 15
lastY = 15

def width_convert(x):
  width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
  face_pos_deg = ((width - x) / width) * 40
  global lastX
  if (face_pos_deg < int(lastX + 5) and face_pos_deg > int(lastX - 5)):
    return lastX
  else:
    lastX = int(((width - x) / width) * 40)
    return int(((width - x) / width) * 40)

def height_convert(y):
  height = video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
  face_pos_deg = ((height - y) / height) * 40
  global lastY
  if (face_pos_deg < int(lastY + 3) and face_pos_deg > int(lastY - 3)):
    return lastY
  else:
    lastY = int(((height - y) / height) * 40)
    return int(((height - y) / height) * 40)
    

while video_capture.isOpened():
  ret, frame = video_capture.read()

  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  frame_gray = cv2.equalizeHist(frame_gray)

  faces = faceCascade.detectMultiScale(frame_gray)
  # print(type(faces))

  for (x, y, w ,h) in faces:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

  cv2.imshow('Video', frame)

  if (len(faces) > 0):
    xInt = int(width_convert(((faces[0][0])+faces[0][2]) - ((faces[0][2]) / 2)))
    yInt = int(height_convert(((faces[0][1])+faces[0][3]) - ((faces[0][3]) / 2)))
    print( str(xInt)+':'+str(yInt) +'_'+str(lastX)+':'+str(lastY))
    write_read( str( str(xInt) + ':' + str(yInt) ) )

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

video_capture.release()
cv2.destroyAllWindows()