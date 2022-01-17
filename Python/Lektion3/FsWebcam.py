#!/usr/bin/env python3
#
#  FsWebcam.py
#  
#  Copyright (C) 2022 by GBS St. Gallen, Inc. All rights reserved.
#  Released under the therms of the GNU General Public License version 3
#  or later.
#
import RPi.GPIO as GPIO
from subprocess import run
import time
from datetime import datetime

BUTTON_UP_GPIO_BOARD_PIN = 37

def takeAPicture():
    actualTime = datetime.now()
    path = '/home/pi/Pictures/'
    filename = 'Aufnahme_' + actualTime.strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'
    run(['fswebcam','-r','1280-1024', path + filename], shell=False)
    
def initGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTON_UP_GPIO_BOARD_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(
        BUTTON_UP_GPIO_BOARD_PIN, GPIO.FALLING, 
        callback=isButtonUpPressed,
        bouncetime = 3000 
    )

def isButtonUpPressed(boardPinNumber):
    takeAPicture()

def cleanupGPIO():
    GPIO.cleanup()

def main():
    print("Foto aufnehmen mit grüner UP- Taste!")
    initGPIO()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("Das Programm wird beendet.")
        cleanupGPIO()

if __name__ == '__main__':
    main()