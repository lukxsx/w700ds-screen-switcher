import subprocess
import os
import time

# get current display status with xrandr
xrandr_output = subprocess.run(['xrandr'], stdout=subprocess.PIPE).stdout.decode("UTF-8")

# if both screens are on, turn off the second screen
if "DVI-D-1 connected 768x1280+1920+0 left" in xrandr_output:
	os.system("xrandr  --output DVI-D-1 --off")
	time.sleep(1) # wait a moment for the display settings to update
	os.system("nitrogen --restore") # set up wallpaper(s)
else:
	# if only main screen is on, turn on the second screen
	os.system("xrandr --output DVI-D-1 --mode 1280x768 --pos 1920x0 --rotate left")
	time.sleep(1) # wait a moment for the display settings to update
	os.system("nitrogen --restore") # set up wallpaper(s)
