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
patience!



************************************************************


TODO: 

- pad digits of recordings 
- fix recordings get cut off
- push sound file to round robin
- record confirm 
- play all submissions
- trim sound file
- fade sound in and out


V2:

- transition to PyAudio to record, not through shell command. 
- fix up hack of chaining to block
- user defined end to recording
- flash LED when playing or recording
- recording: flash faster as time is running out
- confirm, rerecord mechanism
- dont attempt to play file if alsa is in use
- prevent simoultaneous button presses
- local mode ( all files are stored and played locally)
- remote (all recordings are pushed to web server, streamed during play)
- encode file with libshine after record
- encode on the fly 
- logging
- low pass filter
- set up wifi, vs LAN
- run Pi off solar
- 


