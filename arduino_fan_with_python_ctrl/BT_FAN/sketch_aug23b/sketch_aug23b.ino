/* control fan motor & server */
#include <Servo.h>

Servo fan_angle;

int speed_pin = 5, switch_pin = 4, servo_pin = 6, fan_speed = 0, angle = (30 + 120) / 2;
char readBT = 0;

void fan_angle_change(char mode, int min_angle = 30, int max_angle = 120);

void setup() {
  Serial.begin(2000000);
  pinMode(speed_pin, OUTPUT);
  pinMode(switch_pin, OUTPUT);

  fan_angle.attach(servo_pin);
}

void loop() {
  if (Serial.available() > 0) {
    readBT = Serial.read();
    if (readBT == '1') {
      digitalWrite(switch_pin, HIGH);
    }
    else if (readBT == '0') {
      digitalWrite(switch_pin, LOW);
    }
    else if (readBT == 'L') {
      fan_speed-=10;
    }
    else if (readBT == 'H') {
      fan_speed+=10;
    }
    else if (readBT == 'N') {
      fan_speed += 0;
    }
//    else if (readBT == 'M') {
//      fan_speed = 0;
//      digitalWrite(switch_pin, LOW);
//    }

    else if (readBT == 's') {
      angle += 0;
    }
    else if (readBT == 'l') {
      angle+=5;      
    }
    else if (readBT == 'r') {
      angle-=5;
    }

    if (fan_speed > 1023) {
      fan_speed = 1023;
    }
    else if (fan_speed < 0) {
      fan_speed = 0;
    }

    if (angle <= 30) {
      angle = 30;
    }
    else if (angle >= 120) {
      angle = 120;
    }

    Serial.println(fan_speed);
    fan_angle.write(angle);
    analogWrite(speed_pin, fan_speed);
  }
//  else if (!Serial.available()) {
//    digitalWrite(switch_pin, LOW);
//  }
}
