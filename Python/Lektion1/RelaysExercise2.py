#!/usr/bin/env python3
#
#  RelaisExercise2.py
#  
#  Copyright (C) 2020 by GBS St. Gallen, Inc. All rights reserved.
#  Released under the therms of the GNU General Public License version 3
#  or later.
#  

import RPi.GPIO as GPIO
import time

RELAYS_GPIO_BOARD_PIN = 40

def initGPIO():
    GPIO.setmode(GPIO.BOARD)
    #Relay is low-active!
    GPIO.setup(RELAYS_GPIO_BOARD_PIN, GPIO.OUT, initial=GPIO.HIGH)

def switchOn():
    GPIO.output(RELAYS_GPIO_BOARD_PIN, GPIO.LOW)
    print("Relais wurde eingeschaltet")
    
def switchOff():
    GPIO.output(RELAYS_GPIO_BOARD_PIN, GPIO.HIGH)
    print("Relais wurde ausgeschaltet")

def cleanupGPIO():
    GPIO.cleanup()

#Main function:
def main():
    print("Relais- Beispiel")
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
