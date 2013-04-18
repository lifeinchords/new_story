def play_sound( message ):
   # print "inside play_sound"
   # print message
   return




#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

PIN=7

# GPIO set up as input. It is pulled up to stop false signals
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "Make sure you have a button connected so that when pressed"
print "it will connect GPIO port to GND \n"
raw_input("Press Enter when ready\n>")

print "Waiting for falling edge on port "
# now the program will do nothing until the signal on port 
# starts to fall towards zero. This is why we used the pullup
# to keep the signal high and prevent a false interrupt

print "During this waiting time, your computer is not" 
print "wasting resources by polling for a button press.\n"
print "Press your button when ready to initiate a falling edge interrupt."
try:
    GPIO.wait_for_edge(PIN, GPIO.FALLING)
    
    play_sound(PIN);

    print "\nFalling edge detected. Now your program can continue with"
    print "whatever was waiting for a button press."
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit

