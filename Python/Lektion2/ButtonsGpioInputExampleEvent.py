#!/usr/bin/env python3
#
#  ButtonsGpioInputExampleEvent.py
#  
#  Copyright (C) 2022 by GBS St. Gallen, Inc. All rights reserved.
#  Released under the therms of the GNU General Public License version 3
#  or later.
#
import RPi.GPIO as GPIO
import time

BUZZER_GPIO_BOARD_PIN = 12
BUTTON_UP_GPIO_BOARD_PIN = 37

def initGPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUZZER_GPIO_BOARD_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_UP_GPIO_BOARD_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(
        BUTTON_UP_GPIO_BOARD_PIN, GPIO.BOTH, 
        callback=isButtonUpPressed
    )

def switchBuzzerOn():
    GPIO.output(BUZZER_GPIO_BOARD_PIN, GPIO.HIGH)
    
def switchBuzzerOff():
    GPIO.output(BUZZER_GPIO_BOARD_PIN, GPIO.LOW)

def isButtonUpPressed(pin):
    if (GPIO.input(pin) == 0):
        switchBuzzerOn()
    else:
        switchBuzzerOff()

def cleanupGPIO():
    GPIO.cleanup()

def main():
    print("Buzzer- Warnton mit grüner UP- Taste auslösen!")
    print("Zum Beenden CTRL+C drücken, um den Keyboard- Interrupt auszulösen")
    initGPIO()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("Das Programm wird beendet.")
        cleanupGPIO()

if __name__ == '__main__':
    main()