#!/usr/bin/env python3
#
#  FsWebcam.py
#  
#  Copyright (C) 2020 by GBS St. Gallen, Inc. All rights reserved.
#  Released under the therms of the GNU General Public License version 3
#  or later.
#
import RPi.GPIO as GPIO
import os
from datetime import datetime

BUTTON_UP_GPIO_BOARD_PIN = 37

def takeAPicture():
    actualTime = datetime.now()
    path = '/home/pi/Pictures/'
    filename = 'Aufnahme_' + actualTime.strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'
    command = 'fswebcam -r 1280-1024 ' + path + filename
    print(command)
    os.system(command)

def initGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTON_UP_GPIO_BOARD_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def isButtonPressed(boardPinNumber):
    if (GPIO.input(boardPinNumber) == 0):
        return True
    else:
        return False
    
def isButtonUpPressed():
    return isButtonPressed(BUTTON_UP_GPIO_BOARD_PIN)

def cleanupGPIO():
    GPIO.cleanup()

def main():
    print("Foto aufnehmen mit grüner UP- Taste!")
    initGPIO()
    try:
        while True:
            if(isButtonUpPressed()):
                takeAPicture()
    except KeyboardInterrupt:
        print("Das Programm wird beendet.")
        cleanupGPIO()

if __name__ == '__main__':
    main()