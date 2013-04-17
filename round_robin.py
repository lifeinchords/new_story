import RPi.GPIO as GPIO
import time

# set numbering scheme, it can get a bit confusing between the actual pin numbers, and the labels 
# see : http://log.liminastudio.com/writing/tutorials/tutorial-how-to-use-your-raspberry-pi-like-an-arduino
GPIO.setmode(GPIO.BCM)

# 3 momentary buttons, for playing separate audio files
# using Raspberry Pi built in pullup resistors

# note, while you can use any I/O pins on the Pi,
# only some of the have a built in pull-up resistor, which is needed for the switches to work properly
# if you use other pins, you'll have to implement your own

# see:
# http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/

GPIO_PLAY_SWITCH_1 = 0  # this pin has an internal pullup resistor
GPIO_PLAY_SWITCH_2 = 1 	# this pin has an internal pullup resistor
GPIO_PLAY_SWITCH_3 = 24  # no more, wire up a pull up resistor to any pin you use..

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
# most recent bit, 2nd more recent, etc
MR_BIT 		= "b1.wav"
2ND_MR_2 	= "b2.wav"
3RD_MR_3 	= "b3.wav"


# get story size
# TODO: 
# if local: read number of files in designated directory 
# if remote: request count
bit_count = 0


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










