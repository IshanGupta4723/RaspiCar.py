from pynput import keyboard
import pygame
import RPi.GPIO as GPIO
import pygame
import time as tm
from tkinter import*

    
#GPIO.BOARD
GPIO.setmode(GPIO.BOARD)
pygame.mixer.init()
GPIO.setup(40,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)


for i in range(3):
    GPIO.output(40,True)
    GPIO.output(32,True)
    tm.sleep(0.3)
    GPIO.output(40,False)
    GPIO.output(32,False)
    tm.sleep(0.3)

def play():
    pygame.mixer.music.load('/home/pi/Downloads/tesla_autopilot_on.mp3')
    pygame.mixer.music.play()
pygame.mixer.music.load('/home/pi/Downloads/tesla_warning_chime.mp3')
pygame.mixer.music.play()
#headlights and indigators
    
tm.sleep(3)
currentstate = False
currentspeed = 'medium'
currentlight = False
in1 = 7
in2 = 12
en = 13
temp1=1
left = 15
right = 16
turnen = 18

#Sound effects
pygame.mixer.init()
#GPIO setup
#GUI
root = Tk()

#GPIO FRONT SETTINGS
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
#Turning off the engine
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(en,GPIO.LOW)
p=GPIO.PWM(en,1000)

#GPIO TURN SETTINGS
GPIO.setup(left,GPIO.OUT)
GPIO.setup(right,GPIO.OUT)
GPIO.setup(turnen,GPIO.OUT)
GPIO.setwarnings(False)
#Turning off the axel
GPIO.output(left,GPIO.LOW)
GPIO.output(right,GPIO.LOW)
GPIO.output(turnen,GPIO.LOW) 
h = GPIO.PWM(turnen,1000)

#Starting the Motors
p.start(13)
h.start(18)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("Controls:\nr-Starts the engine\ns-Turns off the engine")
print("\n")

def on_press(key):
    global currentlight
    global currentspeed
    global p
    global h
    try:
        if key.char == 'w':
            if currentspeed == 'high':
                p.ChangeDutyCycle(80)
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                
            elif currentspeed == 'medium':
                p.ChangeDutyCycle(60)
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                
            elif currentspeed == 'low':
                p.ChangeDutyCycle(40)
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,wGPIO.LOW)
            
            elif currentspeed == 'keep':
                p.ChangeDutyCycle(25)
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                
            elif currentspeed == 'ultra':
                p.ChangeDutyCycle(100)
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                
            else:
                a = 1
        elif key.char == 's':
            p.ChangeDutyCycle(75)
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            temp1=0
        elif key.char == 'a':
            h.ChangeDutyCycle(100)
            GPIO.output(left,GPIO.HIGH)
            GPIO.output(right,GPIO.LOW)
        elif key.char == 'd':
            h.ChangeDutyCycle(100)
            GPIO.output(left,GPIO.LOW)
            GPIO.output(right,GPIO.HIGH)
        elif key.char == 'i':
            currentspeed = 'high'
            p.ChangeDutyCycle(75)
            print('Drivemode engaged - Ludicrous')
            play()
        elif key.char == 'o':
            currentspeed = 'medium'
            p.ChangeDutyCycle(50)
            print('Drivemode engaged - Normal')
            play()
        elif key.char == 'p':
            currentspeed = 'low'
            p.ChangeDutyCycle(25)
            print('Drivemode engaged - Eco')
            play()
        elif key.char == 'k':
            currentspeed = 'ultra'
            p.ChangeDutyCycle(100)
            print('Drivemode engaged - Plaid')
            play()
        elif key.char == 'j':
            currentspeed = 'keep'
            p.ChangeDutyCycle(20)
            print('Drivemode engaged - Crawl')
            play()
        elif key.char == 'r':
            for i in range(0,80):
                p.ChangeDutyCycle(i)
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                tm.sleep(0.0001)
                
        elif key.char == 'l':
            print('L was pressed')
            if currentlight == False:
                GPIO.output(40,True)
                GPIO.output(32,True)
                currentlight = True
                print('turned light on')
            elif currentlight == True:
                GPIO.output(40,False)
                GPIO.output(32,False)
                currentlight = False
                print('turned light off')
            else:
                pass     
    except:
        pass
def on_release(key):
    global currentspeed
    try:
        if key.char == 'a':
            GPIO.output(left,GPIO.LOW)
            GPIO.output(right,GPIO.LOW)
            
        elif key.char == 'd':
            GPIO.output(left,GPIO.LOW)
            GPIO.output(right,GPIO.LOW)
        elif key.char == 'w':
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            
        elif key.char == 's':
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            
        elif key.char == 'h':
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
        else:
            pass
            
    except:
        pass
#GUI


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()