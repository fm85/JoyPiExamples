#!/usr/bin/env python3
import BuzzerExercise1 as Buzzer

Buzzer.initGPIO()
Buzzer.beep(0.1)
Buzzer.cleanupGPIO()