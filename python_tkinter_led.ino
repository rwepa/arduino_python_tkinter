/*
file  : arduino_tkinter_led.ino
author: Ming-Chang Lee
email : alan9956@gmail.com
RWEPA : http://rwepa.blogspot.tw/
date  : 2021.5.28 
*/

// 參考 NARESH KUMAR T & THILEEPAN S, Arduino + Python Programming for Robots, 2020.

// 宣告變數
char serialData;

// 初使化設定
void setup() {
  pinMode(13, OUTPUT); // LED pin on arduino
  Serial.begin(9600);
}
  
// 執行主程式
void loop() {
  if (Serial.available() > 0) { // 收到 Python 資料進行判斷
    serialData = Serial.read(); // 儲存序列資料
    Serial.print(serialData); // 列印序列資料

    if(serialData == '0') {
      digitalWrite(13, HIGH); //開啟LED
    }
  } else if(serialData == '1') {
    digitalWrite(13, LOW); //關閉LED
  }
}
