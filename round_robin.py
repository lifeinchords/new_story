#!/usr/bin/env python2.7
# script by Steven J. Dale
# adapted from GPIO Rpi articles, by Alex Eames/ http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-2
# http://raspi.tv/tag/multiple-threaded-callbacks-in-rpi-gpio-with-python-on-the-raspberry-pi



import RPi.GPIO as GPIO
from time import gmtime, strftime
import time



# ******************************************
#           FUNCTION DEFS
# ******************************************

def play_sound( filename ):

  print "playing : " + filename

  from subprocess import call
  call (["aplay", "-f", "S16_LE", "-D", "plughw:0,0", "-r", "8000", PROJECT_PATH + "/" + SOUND_BITS_PATH + "/" + filename ])

  return


def record_sound(  ):

  # from subprocess import call
  # record routine here

  print "recording : "
  # from subprocess import call
  # call (["aplay", "-f", "S16_LE", "-D", "plughw:0,0", "-r", "8000", PROJECT_PATH + "/countdown-v2.wav"])
  
  from subprocess import call
  call (["arecord -vv -f S16_LE -c 1 -r 8000 --buffer-size=5000 -d 5 -D plughw:0,0 sounds/new_recording.wav && normalize-audio sounds/new_recording.wav"], shell=True)
  
  # from subprocess import call
  # call (["normalize-audio", "sounds/new_recording" ])
  
  return



def button_callback( channel ):  

    if channel == PLAY_SWITCH_1:
      play_sound("b1.wav")
      press = "play 1"

    elif channel == PLAY_SWITCH_2:
      play_sound("b2.wav")
      press = "play 2"

    elif channel == PLAY_SWITCH_3:
      play_sound("b3.wav")
      press = "play 3"

    elif channel == RECORD_SWITCH:
      press = "record"
      record_sound()

    else:
      press = " not wired"

    print(strftime("%Y-%m-%d %H:%M:%S", gmtime())  + ' : pin %s'%channel + " : " + press) 
    print

    return

# ******************************************
#           INITIALIZE
# ******************************************

# raw_input('stop for now')


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
PLAY_SWITCH_1 = 23
# PLAY_LED_1    = 17

PLAY_SWITCH_2 = 24
# PLAY_LED_2    = 22

PLAY_SWITCH_3 = 25  
# PLAY_LED_3    = 9

# 1 momentary button for triggering a sound recording
# with corresponding LED
RECORD_SWITCH = 27
# RECORD_LED    = 11



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



# get story size
# TODO: 
# if local: read number of files in designated directory 
# if remote: request count
bit_count = 0


GPIO.add_event_detect(PLAY_SWITCH_1, GPIO.BOTH, callback=button_callback, bouncetime=200) 
GPIO.add_event_detect(PLAY_SWITCH_2, GPIO.BOTH, callback=button_callback, bouncetime=200) 
GPIO.add_event_detect(PLAY_SWITCH_3, GPIO.BOTH, callback=button_callback, bouncetime=200) 
GPIO.add_event_detect(RECORD_SWITCH, GPIO.BOTH, callback=button_callback, bouncetime=200) 


# ******************************************
#           MAIN
# ******************************************

try: 
  raw_input('chillin .. . .')

except KeyboardInterrupt:
  GPIO.cleanup()       # clean up GPIO on CTRL+C exit



# ******************************************
#           CLEANUP
# ******************************************

GPIO.cleanup()           # clean up GPIO on normal exit



    








