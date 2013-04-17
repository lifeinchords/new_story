import RPi.GPIO as GPIO
import time


GPIO_PLAY_SWITCH_3 = 3
GPIO_PLAY_SWITCH_2 = 2
GPIO_PLAY_SWITCH_1 = 1

GPIO_RECORD = 1

SOUND_BIT_1 = "t6.wav"

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
		# call(["ls", "-l"])

		# play
		call (["aplay", "-f", "S16_LE", "-D", "plughw:0,0", "-r", "8000", SOUND_BIT_1, "&"])

		# record
		# call (["arecord", "-vv", "-f S16_LE", "-c 1", "-r 8000", "--buffer-size=5000", "-D plughw:0,0", "t52.wav"])

	last_reading = this_reading

	time.sleep(0.05)