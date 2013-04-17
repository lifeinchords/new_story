import RPi.GPIO as GPIO
import time



GPIO_PLAY_SWITCH_3 = 3
GPIO_PLAY_SWITCH_2 = 2
GPIO_PLAY_SWITCH_1 = 1

GPIO_RECORD = 1


GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)

count = 0
last_reading = 0

while True:
	
	pin = 24
	
	this_reading = GPIO.input(pin)

	if ((not last_reading) and this_reading):
		print (str(pin) + " : pressed")
		from subprocess import call
		call(["ls", "-l"])

	last_reading = this_reading

	time.sleep(0.05)


