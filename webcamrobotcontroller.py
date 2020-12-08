import numpy as np
import cv2
from pynput import keyboard

cap = cv2.VideoCapture(0)

import thread
import serial
s = serial.Serial('/dev/ttyUSB0', 9600)

#for i in range(5):
#while True:
    #return_value, image = camera.read()
    #cv2.imshow("stream",image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #cv2.imwrite("opencv"+str(i)+".png", image)

def webcam():
    while True:
        ret,frame = cap.read()
    
        cv2.imshow('stream',frame)
    
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

def on_press(key):
	print("Pressed" + key.char)
	#keycmd = unicode(key.char, "utf-8")
	if(key.char == 'w'):
		s.write('w')
	if(key.char == 's'):
		s.write('s')
	if(key.char == 'a'):
		s.write('a')
	if(key.char == 'd'):
		s.write('d')
	if(key.char == 'z'):
		s.write('z')
	if(key.char == 'x'):
		s.write('x')
	if(key.char == '0'):
		s.write('0')
	if(key.char == '1'):
		s.write('1')
	if(key.char == '2'):
		s.write('2')
	if(key.char == '3'):
		s.write('3')
	if(key.char == '4'):
		s.write('4')
	if(key.char == '5'):
		s.write('5')
	if(key.char == '6'):
		s.write('6')
	if(key.char == '7'):
		s.write('7')
	if(key.char == 'c'):
		s.write('c')
	
	
def on_release(key):
	print('released')

thread.start_new_thread(webcam, ()) 
#thread.start_new_thread(loop,())


with keyboard.Listener(
on_press=on_press,
on_release=on_release) as listener:
	listener.join()




#del(camera)
