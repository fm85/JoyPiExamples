#!/usr/bin/env python3
#
#  LightSensor.py
#  
#  Copyright (C) 2020 by GBS St. Gallen, Inc. All rights reserved.
#  Released under the therms of the GNU General Public License version 3
#  or later.
#
import RPi.GPIO as GPIO
import smbus
import time

class LightSensorBH1750():
    def __init__(self):
        self.ADDRESS = 0x5C #i2c address of light sensor bh1750
        self.POWER_DOWN = 0x00 
        self.POWER_ON = 0x01
        self.RESET = 0x07
        self.BUS = smbus.SMBus(self.getChannel())
        self.BUS.write_byte(self.ADDRESS, self.POWER_ON)
        self.BUS.write_byte(self.ADDRESS, self.RESET)
        
        #continuous modes:
        self.CONTINOUS_LOW_RES_MODE = 0x13 #16ms measurement time, resolution 4 lux
        self.CONTINOUS_HIGH_RES_MODE_1 = 0x13 #120ms measurement time, resolution 1 lux
        self.CONTINOUS_HIGH_RES_MODE_2 = 0x11 #120ms measurement time, resolution 0.5 lux
        
        #one-time modes:
        self.ONE_TIME_LOW_RES_MODE = 0x23 #16ms measurement time, resolution 4 lux
        self.ONE_TIME_HIGH_RES_MODE_1 = 0x20 #120ms measurement time, resolution 1 lux
        self.ONE_TIME_HIGH_RES_MODE_2 = 0x21 #120ms measurement time, resolution 0.5 lux
    
    def getChannel(self):
        if(GPIO.RPI_REVISION == 1):
            i2C_Channel = 0
        else:
            i2C_Channel = 1
        return i2C_Channel

    def convertToNumber(self, data):
        return ((data[1] + (256 * data[0])) / 1.2)
    
    def readLightIntensityLux(self):
        self.BUS.write_byte(self.ADDRESS, self.ONE_TIME_HIGH_RES_MODE_1)
        time.sleep(0.180) #max. 180ms measurement time
        data = [0,0]
        data[0] = self.BUS.read_byte(self.ADDRESS)
        data[1] = self.BUS.read_byte(self.ADDRESS)
        lightIntensity = self.convertToNumber(data)
        return lightIntensity

def main():
    lightSensor = LightSensorBH1750()
    lightIntensityLux = lightSensor.readLightIntensityLux()
    print(lightIntensityLux)
    
if __name__ == '__main__':
    main()
        