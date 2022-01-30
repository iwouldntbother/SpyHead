#include <Servo.h>
#include <ServoEasing.hpp>


ServoEasing Yservo; // Spin Axis
ServoEasing Xservo; // Tilt Axis

int posY = 0;
int posX = 0;
int x;
int y;
String data;

String getValue(String data, char separator, int index) {
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for (int i=0; i<=maxIndex && found<=index; i++) {
    if (data.charAt(i)==separator || i==maxIndex) {
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void setup() {
  Yservo.attach(8, 15);
  Xservo.attach(9, 40);
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  while (!Serial.available());
  data = Serial.readString();
  x = getValue(data, ':', 0).toInt();
  y = getValue(data, ':', 1).toInt();
  Xservo.startEaseTo(x, 5);
  Yservo.startEaseTo(y, 5);
}
