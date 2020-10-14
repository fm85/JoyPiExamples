#!/usr/bin/env python3
import BuzzerGpioOutputExample as Buzzer
import time

Buzzer.initGPIO()
Buzzer.switchOn()
time.sleep(1)
Buzzer.switchOff()
Buzzer.cleanupGPIO()
