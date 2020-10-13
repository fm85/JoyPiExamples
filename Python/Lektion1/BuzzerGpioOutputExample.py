#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  BuzzerGpioOutputExample.py
#  
#  Copyright (C) 2020 by GBS St. Gallen, Inc. All rights reserved.
#  Released under the therms of the GNU General Public License version 3
#  or later.
#  

import RPi.GPIO as GPIO
import time

BUZZER_GPIO_BOARD_PIN = 12

def initGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUZZER_GPIO_BOARD_PIN, GPIO.OUT)

def switchOn():
    GPIO.output(BUZZER_GPIO_BOARD_PIN, GPIO.HIGH)
    
def switchOff():
    GPIO.output(BUZZER_GPIO_BOARD_PIN, GPIO.LOW)

def cleanupGPIO():
    GPIO.cleanup()

#Main function:
def main():
    print("Buzzer- Beispiel")
    initGPIO()
    switchOn()
    time.sleep(0.5) 
    switchOff()
    cleanupGPIO()
    
#Checks whether this file has been executed directly or imported from 
#another file. Only if the file is executed directly, the main function 
#is called.
if __name__ == '__main__':
    main()