import RPi.GPIO as GPIO
import time

# set numbering scheme, it can get a bit confusing between the actual pin numbers, and the labels 
# http://elinux.org/RPi_Low-level_peripherals#General_Purpose_Input.2FOutput_.28GPIO.29

# see : 
GPIO.setmode(GPIO.BCM)

# 3 momentary buttons, for playing separate audio files
# using Raspberry Pi built in pullup resistors

# note, while you can use any I/O pins on the Pi,
# only some of the have a built in pull-up resistor, which is needed for the switches to work properly
# if you use other pins, you'll have to implement your own

# see:
# http://cl.ly/image/033W1o162I3M
# http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/

GPIO_PLAY_SWITCH_1 = 24
GPIO_PLAY_SWITCH_3 = 2
GPIO_PLAY_SWITCH_2 = 3

# 1 momentary button for triggering a sound recording
GPIO_RECORD = 1


# set up pins for switches
GPIO.setup(GPIO_PLAY_SWITCH_1, GPIO.IN)
GPIO.setup(GPIO_PLAY_SWITCH_2, GPIO.IN)
GPIO.setup(GPIO_PLAY_SWITCH_3, GPIO.IN)
GPIO.setup(GPIO_RECORD, GPIO.IN)

# set up pins for LED's (feedback when files are playing/recording)
# TODO:


# TODO: remove hardcoding
SOUND_BIT_1 = "b1.wav"
SOUND_BIT_2 = "b2.wav"
SOUND_BIT_3 = "b3.wav"


count = 0
last_reading = 0

while True:
	
	this_reading = GPIO.input(pin)

	if ((not last_reading) and this_reading):
		print (str(pin) + " : pressed")
		
		from subprocess import call
		# call(["ls", "-l"])

		# play
		call (["aplay", "-f", "S16_LE", "-D", "plughw:0,0", "-r", "8000", SOUND_BIT_1)

		# record
		# call (["arecord", "-vv", "-f S16_LE", "-c 1", "-r 8000", "--buffer-size=5000", "-D plughw:0,0", "t52.wav"])

	last_reading = this_reading

	time.sleep(0.05)










