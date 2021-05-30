# -*- coding: utf-8 -*-
"""
file  : python_tkinter_led.py
author: Ming-Chang Lee
email : alan9956@gmail.com
RWEPA : http://rwepa.blogspot.tw/
date  : 2021.5.28
"""

# Import following packages
import serial
import tkinter
import tk_tools

# Connect to arduino via serial port 
# com4 --> Change port accordingly to yours
arduino = serial.Serial('com4', 9600)

#Function call for led_on button
def led_on():
    arduino.write(b'0') #write this value to arduino 
    led.to_green(True)  #Glow the led to green --> Refer to tk-tools docs
    button_on.config(state = "disabled") #disable button_on 
    button_off.config(state = "normal") # enable button_off to normal state

#function call for led_off button
def led_off():
    arduino.write(b'1') #write this value to arduino 
    led.to_green() #Switch off the led --> Refer to tk-tools docs
    button_off.config(state = "disabled") #disable button_off
    button_on.config(state = "normal") #enable button_on to normal state

#exit function call for closing the program
def close_window():
    arduino.close() #close Serial connection with arduino
    window.destroy() #destro tkinter app
    
# MAIN
window = tkinter.Tk() #create tkinter window
window.title("Arduino RGB Led Control") #give title
window.configure(background="white") #change background color 

#Create buttons
button_on = tkinter.Button(window, text="ON", 
                           font= ('Verdana',16), padx=50, pady =20, 
                           bg="green",fg="white",
                           command = led_on)

button_off = tkinter.Button(window, text="OFF", 
                            font=('Verdana',16), padx=50, pady =20, 
                            bg="red",fg="white",
                            command = led_off)

button_exit = tkinter.Button(window, text="Exit", 
                             font=('Verdana',16), 
                             padx=130, pady =20, 
                             command = close_window)

#Pack buttons
button_on.grid(row=1,column=1)
button_off.grid(row=1,column=2)
button_off.config(state = "disabled")
button_exit.grid(row=2,column=1, columnspan =2)

#Create interactive led using tk-tools
led = tk_tools.Led(window, size=100)
led.to_green() #set led to green switch off condition) --> Refer tk-tools docs
led.grid(row=0,column=1, columnspan =2)
    
#execute the loop
window.mainloop()
