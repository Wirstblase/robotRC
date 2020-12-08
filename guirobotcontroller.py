#import thread
import serial
s = serial.Serial('/dev/ttyUSB0', 9600)

from tkinter import *

def rmovew():
    s.write('w')
def rmoves():
    s.write('s')
def rmovea():
    s.write('a')
def rmoved():
    s.write('d')
def rmovex():
    s.write('x')
    #print("stopped")
    
    

window = Tk()

window.title("Robot controller")

btn1 = Button(window, text="Forward",command = rmovew)
btn1.grid(column=0, row=0)

btn1 = Button(window, text="Backward",command = rmoves)
btn1.grid(column=1, row=0)

btn1 = Button(window, text="Left",command = rmovea)
btn1.grid(column=0, row=1)

btn1 = Button(window, text="Right",command = rmoved)
btn1.grid(column=1, row=1)

btn1 = Button(window, text="Stop",command = rmovex)
btn1.grid(column=0, row=2)

window.mainloop()
