************************************************************


CONCEPT:


New Story is a prototype for a sound installation based on the Raspberry Pi. 
Users collaboratively stitch a new story together through sound recordings, using a custom designed intercom-like interface.
Imagine exquisite corpse, but through sound.

People interact with the installation on site by pressing buttons on the interface to play each of the 3 most recent recordings.
If they chose, they can press a fourth button, which allows them X number of seconds to record.

On completeion, the recorded audio file is : 

- encoded to mp3 format
- pushed to a server, and onto a stack. No limit to the number of recordings in the story.
- on the interface itself, only the 3 most recent recordings can be played, removing the full context of the story that was developed.

A web application running on Heroku will allow visitors to listen to the full story (all recordings)

************************************************************


CIRCUIT SCHEMATIC:



************************************************************


ITEM LIST 

1 Raspberry Pi, Rev 2 board
4 switches
1 breadboard




************************************************************


TODO: 

- local mode ( all files are stored and played locally)
- remote (all recordings are pushed to web server, streamed during play)
- encode file
- more efficient switch debouncer, instead of using loops
  adapt from Arudio code: http://www.adafruit.com/blog/2009/10/20/example-code-for-multi-button-checker-with-debouncing/
- add interrupt capability, so hitting buttons 1-3 button stops playback of other playing files, and triggers selected 
  http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio



