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

#Main function:
def main(args):
    print("Buzzer- Beispiel")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUZZER_GPIO_BOARD_PIN, GPIO.OUT)
    GPIO.output(BUZZER_GPIO_BOARD_PIN, GPIO.HIGH)
    time.sleep(0.5) 
    GPIO.output(BUZZER_GPIO_BOARD_PIN, GPIO.LOW) 
    GPIO.cleanup()
    return 0
 
#Checks whether this file has been executed directly or imported from 
#another file. Only if the file is executed directly, the main function 
#is called.
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
