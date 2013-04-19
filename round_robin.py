#!/usr/bin/env python2.7
# script by Steven J. Dale
# adapted from GPIO Rpi articles, by Alex Eames/ http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-2
# http://raspi.tv/tag/multiple-threaded-callbacks-in-rpi-gpio-with-python-on-the-raspberry-pi



import RPi.GPIO as GPIO
from time import gmtime, strftime
import time
import subprocess


# ******************************************
#           FUNCTION DEFS
# ******************************************

def play_sound( filename ):

  subprocess.call (["aplay", "-f", "S16_LE", "-D", "plughw:0,0", "-r", "8000", PROJECT_PATH + "/" + SOUND_BITS_PATH + "/" + filename ])

  return


def record_sound(  ):

  # 1. play countdown tone
  # 2. record
  # 3. normalize
  # subprocess.call (["sh", "/home/pi/code/new_story/play_sound.sh"])

  # subprocess.call (["aplay -f S16_LE -D plughw:0,0 -r 8000 countdown-v2.wav && ls -al && normalize-audio sounds/new_recording.wav"], shell=True)



  #call (["aplay -f S16_LE -D plughw:0,0 -r 8000 " + PROJECT_PATH + "/countdown-v2.wav; arecord -vv -f S16_LE -c 1 -r 8000 --buffer-size=5000 -d 5 -D plughw:0,0 sounds/new_recording.wav; normalize-audio sounds/new_recording.wav"], shell=True)
  # call (["aplay -f S16_LE -D plughw:0,0 -r 8000 " + PROJECT_PATH + "/countdown-v2.wav; arecord -vv -f S16_LE -c 1 -r 8000 --buffer-size=5000 -d 5 -D plughw:0,0 sounds/new_recording.wav; normalize-audio sounds/new_recording.wav"], shell=True)
  
  return



def button_callback( channel ):  

  print
  print("callback: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())  + ' : pin %s'%channel)

  if channel == PLAY_SWITCH_1:
    press = "registered play button 1 hit"
    play_sound("b1.wav")

  elif channel == PLAY_SWITCH_2:
    press = "registered play button 2 hit"
    play_sound("b2.wav")

  elif channel == PLAY_SWITCH_3:
    press = "registered play button 3 hit"
    play_sound("b3.wav")

  elif channel == RECORD_SWITCH:
    press = "registered record hit"
    record_sound()

  else:
    press = " not wired"

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

# stub, not in use
STUB = 0

# 3 momentary buttons, for playing separate audio files
# each button has corresponding LED 
PLAY_SWITCH_1 = 18
# PLAY_LED_1    = 17

PLAY_SWITCH_2 = 23
# PLAY_LED_2    = 22

PLAY_SWITCH_3 = 25  
# PLAY_LED_3    = 9

# 1 momentary button for triggering a sound recording
# with corresponding LED
RECORD_SWITCH = 8
# RECORD_LED    = 11



# set up pins for switches, as inputs with pull up resistors
# prevents having to do them in hardware
# more: http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/
GPIO.setup(PLAY_SWITCH_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PLAY_SWITCH_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PLAY_SWITCH_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RECORD_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(STUB, GPIO.IN, pull_up_down=GPIO.PUD_UP)



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


GPIO.add_event_detect(PLAY_SWITCH_1, GPIO.PUD_UP, callback=button_callback, bouncetime=300) 
GPIO.add_event_detect(PLAY_SWITCH_2, GPIO.PUD_UP, callback=button_callback, bouncetime=300) 
GPIO.add_event_detect(PLAY_SWITCH_3, GPIO.PUD_UP, callback=button_callback, bouncetime=300) 
GPIO.add_event_detect(RECORD_SWITCH, GPIO.PUD_UP, callback=button_callback, bouncetime=300) 


# ******************************************
#           MAIN
# ******************************************

try: 
  raw_input('chillin .. . .')

  GPIO.wait_for_edge(7, GPIO.BOTH)  


except KeyboardInterrupt:
  GPIO.cleanup()       # clean up GPIO on CTRL+C exit



# ******************************************
#           CLEANUP
# ******************************************

GPIO.cleanup()           # clean up GPIO on normal exit



    
