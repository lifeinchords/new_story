#!/usr/bin/env python2.7
# script by Steven J. Dale
# adapted from GPIO Rpi articles, by Alex Eames/ http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-2
# http://raspi.tv/tag/multiple-threaded-callbacks-in-rpi-gpio-with-python-on-the-raspberry-pi


def play_sound( message ):
	print "* enter playing sound ... "

   return


def record_sound:
	print "* enter recording sound ... "
	return



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
# each button has corresponding LED 
PLAY_SWITCH_1 = 17
# PLAY_LED_1	= 18

PLAY_SWITCH_2 = 22
# PLAY_LED_2	= 23

PLAY_SWITCH_3 = 25  
# PLAY_LED_3	= 9

# 1 momentary button for triggering a sound recording
# with corresponding LED
RECORD_SWITCH = 8
# RECORD_LED	= 11



# set up pins for switches, as inputs with pull up resistors
# prevents having to do them in hardware
# more: http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/
GPIO.setup(PLAY_SWITCH_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PLAY_SWITCH_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PLAY_SWITCH_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RECORD_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)



# for LEDs
# GPIO.setup(PLAY_LED_1, GPIO.OUT)
# GPIO.setup(PLAY_LED_2, GPIO.OUT)
# GPIO.setup(PLAY_LED_3, GPIO.OUT)
# GPIO.setup(RECORD_LED, GPIO.OUT)



# TODO: remove hardcoding
# most recent bit, 2nd more recent, etc

NEW_BIT				= "new_bit.wav"
FIRST_SOUND_BIT		= "bit_1.wav"
SECOND_MR_SOUND_BIT	= "bit_2.wav"
THIRD_MR_SOUND_BIT	= "bit_3.wav"


# get story size
# TODO: 
# if local: read number of files in designated directory 
# if remote: request count
bit_count = 0



try:
    GPIO.wait_for_edge(PIN, GPIO.FALLING) # Falling edge detected. script continues
    
    # determine to play or record
    # TODO: 

    if 
    	play_sound(PIN);

    	# TODO: move internally
    	# from subprocess import call
    	# call (["aplay", "-f", "S16_LE", "-D", "plughw:0,0", "-r", "8000", PROJECT_PATH + "/" + SOUND_BITS_PATH + "/" + CURRENT_SOUND_BIT])

    	# TODO: flash led
    	# GPIO.output(PLAY_LED_2,GPIO.LOW)
    	# time.sleep(0.05)

    else
    	# call (["arecord", "-vv", "-f S16_LE", "-c 1", "-r 8000", "--buffer-size=5000", "-D plughw:0,0", "new_recording.wav"])
    end

    


except KeyboardInterrupt:
    
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit



GPIO.cleanup()           # clean up GPIO on normal exit



	








