#!/usr/bin/env python3
#
#  ButtonsExercise1.py
#  
#  Copyright (C) 2020 by GBS St. Gallen, Inc. All rights reserved.
#  Released under the therms of the GNU General Public License version 3
#  or later.
#
import RPi.GPIO as GPIO

BUZZER_GPIO_BOARD_PIN = 12
BUTTON_UP_GPIO_BOARD_PIN = 37
BUTTON_RIGHT_GPIO_BOARD_PIN = 35
RELAY_GPIO_BOARD_PIN = 40

def initGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUZZER_GPIO_BOARD_PIN, GPIO.OUT)
    GPIO.setup(RELAY_GPIO_BOARD_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_UP_GPIO_BOARD_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BUTTON_RIGHT_GPIO_BOARD_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def switchBuzzerOn():
    GPIO.output(BUZZER_GPIO_BOARD_PIN, GPIO.HIGH)
    
def switchBuzzerOff():
    GPIO.output(BUZZER_GPIO_BOARD_PIN, GPIO.LOW)

def switchRelayOn():
    GPIO.output(RELAY_GPIO_BOARD_PIN, GPIO.LOW)
    
def switchRelayOff():
    GPIO.output(RELAY_GPIO_BOARD_PIN, GPIO.HIGH)

def isButtonPressed(boardPinNumber):
    if (GPIO.input(boardPinNumber) == 0):
        return True
    else:
        return False
    
def isButtonUpPressed():
    return isButtonPressed(BUTTON_UP_GPIO_BOARD_PIN)

def isButtonRightPressed():
    return isButtonPressed(BUTTON_RIGHT_GPIO_BOARD_PIN)

def cleanupGPIO():
    GPIO.cleanup()

def main():
    print("Buzzer- Warnton mit grüner UP- Taste auslösen!")
    print("Relais mit grüner RIGHT- Taste einschalten!")
    print("Zum Beenden CTRL+C drücken, um den Keyboard- Interrupt auszulösen")
    initGPIO()
    try:
        while True:
            if(isButtonUpPressed()):
                switchBuzzerOn()
            else:
                switchBuzzerOff()
            
            if(isButtonRightPressed()):
                switchRelayOn()
            else:
                switchRelayOff()
    except KeyboardInterrupt:
        print("Das Programm wird beendet.")
        cleanupGPIO()

if __name__ == '__main__':
    main()