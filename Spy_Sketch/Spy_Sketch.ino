#include <Servo.h>

Servo Yservo; // Spin Axis
Servo Xservo; // Tilt Axis

int posY = 0;
int posX = 0;

void setup() {
  Yservo.attach(9);
  Xservo.attach(8);
}

void loop() {
  for (posY = 0; posY <= 180; posY += 1) {
    Yservo.write(posY);
    delay(15);
  }
  for (posY = 180; posY >= 0; posY -= 1) {
    Yservo.write(posY);
    delay(15);
  }

  for (posX = 0; posX <= 180; posX += 1) {
    Xservo.write(posX);
    delay(15);
  }
  for (posX = 180; posX >= 0; posX -= 1) {
    Xservo.write(posX);
    delay(15);
  }
}
