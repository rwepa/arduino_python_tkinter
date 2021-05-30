# -*- coding: utf-8 -*-
"""
file  : python_arduino_led.py
author: Ming-Chang Lee
email : alan9956@gmail.com
RWEPA : http://rwepa.blogspot.tw/
date  : 2021.5.28
"""

# conda install pyfirmata
import pyfirmata
pin = 13
port = 'COM4'
board = pyfirmata.Arduino(port)
board.digital[pin].write(1) # Python 程式 ON
board.digital[pin].write(0) # Python 程式 OFF

