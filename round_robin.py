import RPi.GPIO as GPIO
import time

PROJECT_PATH = "/home/pi/code/new_story"
SOUND_BITS_PATH = "sounds"

# 0 : local
# 1: remote
# TODO: implement logic
RUN_TYPE = 0

# set numbering scheme, it can get a bit confusing between the actual pin numbers, and the labels 
# see : http://log.liminastudio.com/writing/tutorials/tutorial-how-to-use-your-raspberry-pi-like-an-arduino
GPIO.setmode(GPIO.BCM)

# 3 momentary buttons, for playing separate audio files
GPIO_PLAY_SWITCH_1 = 0  
GPIO_PLAY_SWITCH_2 = 1 	
GPIO_PLAY_SWITCH_3 = 24  

# 1 momentary button for triggering a sound recording
GPIO_RECORD = 1


# set up pins for switches, as inputs with pull up resistors
# prevents having to do them in hardware
# more: http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/
GPIO.setup(GPIO_PLAY_SWITCH_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_PLAY_SWITCH_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_PLAY_SWITCH_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(GPIO_RECORD, GPIO.IN)

# set up pins for LED's (feedback when files are playing/recording)
# TODO:


# TODO: remove hardcoding
# most recent bit, 2nd more recent, etc
CURRENT_SOUND_BIT		= "b1.wav"
SECOND_MR_SOUND_BIT	 	= "b2.wav"
THIRD_MR_SOUND_BIT		= "b3.wav"


# get story size
# TODO: 
# if local: read number of files in designated directory 
# if remote: request count
bit_count = 0


last_reading = 0

while True:
	
	this_reading = GPIO.input(GPIO_PLAY_SWITCH_3)

	if ((not last_reading) and this_reading):
		print (str(GPIO_PLAY_SWITCH_3) + " : pressed")
		
		from subprocess import call
		# call(["ls", "-l"])

		# play
		call (["aplay", "-f", "S16_LE", "-D", "plughw:0,0", "-r", "8000", PROJECT_PATH + "/" + SOUND_BITS_PATH + "/" + CURRENT_SOUND_BIT])

		# record
		# call (["arecord", "-vv", "-f S16_LE", "-c 1", "-r 8000", "--buffer-size=5000", "-D plughw:0,0", "t52.wav"])

	last_reading = this_reading

	time.sleep(0.05)










