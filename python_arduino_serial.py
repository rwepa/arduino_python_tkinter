# -*- coding: utf-8 -*-
"""
file  : python_arduino_serial.py
author: Ming-Chang Lee
email : alan9956@gmail.com
RWEPA : http://rwepa.blogspot.tw/
date  : 2021.5.28
"""

import serial
s = serial.Serial('COM4',9600)
while True:
    print(s.readline())
    
