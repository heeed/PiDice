#!/usr/bin/python 
# PiDice
#
# Simple dice program for the 4tronix PartyHat
# 

import random
from neopixel import *
from time import sleep
import RPi.GPIO as GPIO

#setup gpio to use bcm numbering
GPIO.setmode(GPIO.BCM)

#set gpio pin states
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(04,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_UP)


# LED strip configuration:
LED_COUNT      = 9      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 50     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


#LED patterns for numbers

dice = {'0':'000010000','1':'100000001','2':'100010001','3':'101000101','4':'101010101','5':'111000111'}

def diceRoll():
	min = 0
	max = 5
	return random.randint(min,max)

def clearArray(strip):
	#print("in clearing function")
	for i in range(strip.numPixels()):
		strip.setPixelColor(i,Color(0,0,0))
	strip.show()

def testArray(strip):
        #print("in test function")
        for i in range(strip.numPixels()):
                strip.setPixelColor(i,Color(255,255,255))
       	strip.show()

def displayNumber(number,strip):
	clearArray(strip)
        sleep(0.5)
	print("The dice rolled: "+str(number+1))
	num=dice[str(number)]
	numlen=len(num)
	for x in range(numlen):
		if num[x] == '1':
			strip.setPixelColor(x,Color(255, 0, 0))	



# Main program logic follows:
if __name__ == '__main__':

	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	print("PiDice")
 	clearArray(strip)
	strip.show()
	while True:
		#print(str(inputPin))
		if not GPIO.input(04):
			#print("Red Button Pressed")
			sleep(0.5)
		        displayNumber(diceRoll(),strip)
	                strip.show()
        	        

		if not GPIO.input(17):
                        print("Green Button Pressed")
                        sleep(0.5)
		if not GPIO.input(27):
                        print("Blue Button Pressed")
                        sleep(0.5)
		if not GPIO.input(22):
                        print("Yellow Button Pressed")
                        sleep(0.5)
			for z in range(0,6):
				print(z)
				clearArray(strip)
				sleep(2)
				displayNumber(z,strip)	
				strip.show()
				sleep(2)
				clearArray(strip)
			sleep(2)
			testArray(strip)
			sleep(0.5)
			clearArray(strip)
