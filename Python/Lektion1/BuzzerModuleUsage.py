#!/usr/bin/env python3
import BuzzerGpioOutputExample as Buzzer

Buzzer.initGPIO()
Buzzer.switchOn()
Buzzer.time.sleep(1)
Buzzer.switchOff()
Buzzer.cleanupGPIO()
