/* fan controller */

#include <SoftwareSerial.h>
SoftwareSerial myserial(12, 13);  // (RX, TX)

int LEFT_PINS = 3, RIGHT_PINS = 3;
                     // 排放順序 x, y, 按鈕
int LEFT_JOYSTICK[] = {14, 15, 2};
int RIGHT_JOYSTICK[] = {17, 16, 4};

boolean flag = true;
int switch_btn = 0;
char remote;

void setup() {
  /* 腳位 */
  for (int i = 0; i < LEFT_PINS - 1; i++) {
     pinMode(LEFT_JOYSTICK[i], INPUT);
  }
  for (int i = 0; i < RIGHT_PINS - 1; i++) {
     pinMode(RIGHT_JOYSTICK[i], INPUT);
  }
  pinMode(LEFT_JOYSTICK[2], INPUT_PULLUP);  // 左邊搖桿 按鈕
  pinMode(RIGHT_JOYSTICK[2], INPUT_PULLUP); // 右邊搖桿 按鈕

  Serial.begin(2000000);
  myserial.begin(9600);
}

void loop() {
  /* 左邊搖桿 */
  int left_x = analogRead(LEFT_JOYSTICK[0]);
  int left_y = analogRead(LEFT_JOYSTICK[1]);
  int left_button = digitalRead(LEFT_JOYSTICK[2]);
// ----------------------------------------------------------------------------------------------------------
  /* 右邊搖桿 */
  int right_x = analogRead(RIGHT_JOYSTICK[0]);
  int right_y = analogRead(RIGHT_JOYSTICK[1]);
  int right_button = digitalRead(RIGHT_JOYSTICK[2]);
// ----------------------------------------------------------------------------------------------------------

  Serial.flush();
  Serial.print(left_x);
  Serial.print(',');
  Serial.print(left_y);
  Serial.print(',');
  Serial.print(!left_button);
  Serial.print(',');
  Serial.print(right_x);
  Serial.print(',');
  Serial.print(right_y);
  Serial.print(',');
  Serial.print(!right_button);
  Serial.println();
//  printInfo(left_y);

// 左右中間位置 => 範圍: 490 ~ 515  (參考值)                     
  /* 風扇電壓調整 */
  char SPEED;
  
  if (right_y <= 600 && right_y >= 400) {
    SPEED = 'N';  // 無變化
  }
  else if (right_y > 600) {
    SPEED = 'L';  // 遞減
  }
  else if (right_y < 400){
    SPEED = 'H';  // 遞增
  }
  
  myserial.write(SPEED);

  /* 風扇擺頭 (手動) */
  char angle_mode;
  if (right_x < 300) {
    angle_mode = 'l';
  }
  else if (right_x > 600) {
    angle_mode = 'r';
  }
  else {
    angle_mode = 's';
  }
  myserial.write(angle_mode);
  
  /* relay 繼電器 */
  if (!right_button && !flag) {
    switch_btn = !switch_btn;
    flag = true;
  }
  else if (right_button && flag) {
    flag = false;
  }
//  Serial.println(switch_btn);
  if (switch_btn == 1) {
    remote = '1';
  }
  else if (switch_btn == 0) {
    remote = '0';
  }

  /* 緊急停止 */
//  if (right_button == HIGH) {
//    remote = 'M';
//  }
  
  myserial.write(remote);
  delay(20);
}

void printInfo(int left_y) {
  Serial.print("leff_x : ");
  Serial.println(left_y);
}
