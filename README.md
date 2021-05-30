## Arduino + Python tkinter 套件控制LED應用

![image](https://github.com/rwepa/arduino_python_tkinter/blob/main/imgs/arduino_tkinter_led.png)

檔名: python_arduino-2021.05.28.pdf
[https://github.com/rwepa/arduino_python_tkinter/blob/main/python_arduino-2021.05.28.pdf]

Python + Arduino 應用說明:

## 大綱

+ Python 簡介
+ 視窗設計 - tkinter 套件
+ Arduino 簡介
+ Python + Arduino - LED 實作

## 視窗設計 - tkinter套件

+ ex1 簡單視窗
+ ex2 文字與按鈕範例
+ ex3 按鈕事件
+ ex4 組合方塊 combobox (下拉式選單)
+ Ex5 滑桿 scale

檔名: python_tkinter.py [https://github.com/rwepa/arduino_python_tkinter/blob/main/python_tkinter_led.py]

## Python + Arduino - LED 實作

### 範例1 Arduino + LED

+ 準備工具: Arduino 板子, LED, 電阻 1KΩ, 接線, 麵包板.

檔名: arduino_led.ino [https://github.com/rwepa/arduino_python_tkinter/blob/main/arduino_led.ino]

操作影片

[![Arduino car](https://github.com/rwepa/arduino_python_tkinter/blob/main/imgs/arduino_led_youtube.png)](https://youtu.be/9nDX06hpkXM)

youtube: [https://youtu.be/9nDX06hpkXM]

### 範例2 Arduino – Firmata

+ Firmata 是一個控制器通訊協定。
+ 使用該協定，可以讓電腦或手持式裝置進行Arduino控制。

檔名: StandardFimata.ino, Arduino IDE 內建範例, [檔案 \ 範例 \ Fimata\ StandardFimata]], 驗證 --> 上傳 

測試程式 firmata_test.exe [http://www.firmata.org/wiki/Main_Page]

### 範例3 Arduino + Python- pyfirmata 套件

+ 使用 pyfirmata 套件可以將 Python 與 Arduino 連結

+ 安裝 pyfirmata 套件

方法1: conda install pyfirmata

方法2: pip install pyfirmata

檔名: python_arduino_led.py [https://github.com/rwepa/arduino_python_tkinter/blob/main/python_arduino_led.py]

操作影片

[![python + arduino + led 應用-使用 pyfirmata 套件](https://github.com/rwepa/arduino_python_tkinter/blob/main/imgs/python_arduino_led_youtube.png)](https://youtu.be/YGpsoZ5n_Tg)

youtube: [https://youtu.be/YGpsoZ5n_Tg]

### 範例4 Arduino + Python- pySerial 套件

+ 使用 pySerial 套件可以將 Python 與 Arduino 連結

+ 安裝 pySerial 套件

方法1: conda install pySerial

方法2: pip install pySerial

檔名: DigitalReadSerial.ino, Arduino IDE 內建範例 [檔案 \ 範例 \ 01.Basics \ DigitalReadSerial], 驗證 --> 上傳 

檔名: python_arduino_serial.py [https://github.com/rwepa/arduino_python_tkinter/blob/main/python_arduino_serial.py]

### 範例5 Arduino + Python - tkinter 套件

+ 使用 pySerial, tkinter 套件, 將 Python 與 Arduino 連結

檔名: arduino_tkinter_led.ino [https://github.com/rwepa/arduino_python_tkinter/blob/main/python_tkinter_led.ino]

檔名: python_tkinter_led.py [https://github.com/rwepa/arduino_python_tkinter/blob/main/python_tkinter_led.py]

操作影片

[![python + tkinter - LED 應用](https://github.com/rwepa/arduino_python_tkinter/blob/main/imgs/arduino_tkinter_led_youtube.png)](https://youtu.be/LjgFIm1S7tw)

youtube: [https://youtu.be/LjgFIm1S7tw]

### 參考資料

1. Python 程式設計-李明昌 免費電子書 - PDF 分享, 220頁, http://rwepa.blogspot.com/2020/02/pythonprogramminglee.html
2. Python與Arduino, http://andrewpythonarduino.blogspot.com/2018/04/python13-led.html
3. NARESH KUMAR T & THILEEPAN S, Arduino + Python Programming for Robots, 2020.
4. tkinter - Python interface to Tcl/Tk, https://docs.python.org/3/library/tkinter.html
5. Python GUI examples (Tkinter Tutorial), https://likegeeks.com/python-gui-examples-tkinter-tutorial/

### 參考網址
RWEPA [http://rwepa.blogspot.com/2021/05/arduino-python-tkinter-led.html]
