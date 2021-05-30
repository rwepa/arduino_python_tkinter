# -*- coding: utf-8 -*-
"""
file  : python_tkinter.py
author: Ming-Chang Lee
email : alan9956@gmail.com
RWEPA : http://rwepa.blogspot.tw/
date  : 2021.5.28
"""

# 命令提示列
# python -m tkinter

# ex1 第一個範例
from tkinter import *
window = Tk() # 建立初使化物件
window.title("我的第1個Python視窗-107400168李明昌") # 視窗標題
window.mainloop() # 

# ex2 文字與按鈕範例
from tkinter import *
window = Tk()
window.title("按鈕範例")
window.geometry('300x200')

# 建立文字
lbl = Label(window, text="Hello World!")
lbl.grid(column=0, row=0)

# 建立按鈕
btn = Button(window, text="按我")
btn.grid(column=1, row=0)

window.mainloop()

# ex3 按鈕事件
from tkinter import *
window = Tk()
window.title("按鈕事件")
window.geometry('200x200')

lbl = Label(window, text="請按下按鈕!")
lbl.grid(column=0, row=0)

# 按鈕事件
def clicked():
    lbl.configure(text="已經按下按鈕囉!!!")

btn = Button(window, text="按我", command=clicked)
btn.grid(column=1, row=0)

window.mainloop()

# ex4 組合方塊 combobox (下拉式選單)
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("組合方塊 combobox (下拉式選單)")
window.geometry('350x200')
combo = Combobox(window)

combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=0)

window.mainloop()

# ex5 滑桿 scale
from tkinter import *

window = Tk()
window.title("滑桿 scale")

var = DoubleVar()
scale = Scale(window, variable = var )
scale.pack(anchor=CENTER)

def sel():
   selection = "Value = " + str(var.get())
   label.config(text = selection)
   
button = Button(window, text="Get Scale Value", command=sel)
button.pack(anchor=CENTER)

label = Label(window)
label.pack()

window.mainloop()
