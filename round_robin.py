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
import glob
import os

# get story size
# TODO: 
# if local: read number of files in designated directory 
# if remote: request count
bit_count = 0
file_array = glob.glob("/home/pi/code/new_story/sounds/b_*.wav")
bit_array = []

for bit in file_array:
  head, tail = os.path.split(bit)
  bit_array.append(int(tail.split('.')[0].split('_')[1]))

bit_array.sort()
bit_count = len(bit_array)
next_recording_number = bit_count + 1



PROJECT_PATH = "/home/pi/code/new_story"
SOUND_BITS_PATH = "sounds"
FULL_PATH = PROJECT_PATH + "/" + SOUND_BITS_PATH




# ******************************************
#           FUNCTION DEFS
# ******************************************

def play_sound( filename ):

  subprocess.call (["aplay", "-f", "S16_LE", "-D", "plughw:0,0", "-r", "8000", "sounds/" + filename ])
  return


def record_sound():

  # 1. play countdown tone
  # 2. record
  # 3. normalize

  # call by chaining, as we *want* blocking, or else other button presses would mess things up by running
  subprocess.call ([ "aplay -f S16_LE -D plughw:0,0 -r 8000 countdown-v2.wav && \
                      arecord -vv -f S16_LE -c 1 -r 8000 --buffer-size=5000 -d 20 -D plughw:0,0 sounds/b_" + str(next_recording) + ".wav && \
                      normalize-audio sounds/b_" + str(next_recording) + ".wav && \
                      ln -s " + FULL_PATH + "/b_" + str("{0:03d}".format(next_recording_number)) + ".wav " + FULL_PATH + "/3.wav && \
                      ln -s " + FULL_PATH + "/b_" + str("{0:03d}".format(next_recording_number - 1 ))+ ".wav " + PFULL_PATH + "/2.wav && \
                      ln -s " + FULL_PATH + "/b_" + str("{0:03d}".format(next_recording_number - 2))+ ".wav " + FULL_PATH + "/1.wav"

                    ], shell=True)

  next_recording += 1

  return



def button_callback( channel ):  

  print
  print("callback: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())  + ' : pin %s'%channel)

  # filenames passed are symbolic links: 1, 2, 3
  # which are always pointing to the 3 most recent sound bits
  # 3 is the newest/latest
  if channel == PLAY_SWITCH_1:
    press = "registered play button 1 hit"
    play_sound("1.wav")

  elif channel == PLAY_SWITCH_2:
    press = "registered play button 2 hit"
    play_sound("2.wav")

  elif channel == PLAY_SWITCH_3:
    press = "registered play button 3 hit"
    play_sound("3.wav")

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


# 0 : local
# 1: remote
# TODO: implement logic
RUN_TYPE = 0

# set numbering scheme, it can get a bit confusing between the actual pin numbers, and the labels 
# see : http://log.liminastudio.com/writing/tutorials/tutorial-how-to-use-your-raspberry-pi-like-an-arduino
GPIO.setmode(GPIO.BCM)

# stub, not in use in hardware
#  serves as a way to call wait for event for main script
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





GPIO.add_event_detect(PLAY_SWITCH_1, GPIO.BOTH, callback=button_callback, bouncetime=300) 
GPIO.add_event_detect(PLAY_SWITCH_2, GPIO.BOTH, callback=button_callback, bouncetime=300) 
GPIO.add_event_detect(PLAY_SWITCH_3, GPIO.BOTH, callback=button_callback, bouncetime=300) 
GPIO.add_event_detect(RECORD_SWITCH, GPIO.BOTH, callback=button_callback, bouncetime=300) 


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



    
