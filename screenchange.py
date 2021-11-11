import subprocess
import os
import time

# get current display status with xrandr
result = subprocess.run(['xrandr'], stdout=subprocess.PIPE)

# if only main screen is on, turn on the second screen
if result.stdout == b'Screen 0: minimum 8 x 8, current 1920 x 1200, maximum 8192 x 8192\nVGA-0 disconnected primary ' \
					b'(normal left inverted right x axis y axis)\nLVDS-0 connected 1920x1200+0+0 (normal left ' \
					b'inverted right x axis y axis) 367mm x 230mm\n   1920x1200     60.00*+  50.00  \nDVI-D-0 ' \
					b'disconnected (normal left inverted right x axis y axis)\nDVI-D-1 connected (normal left ' \
					b'inverted right x axis y axis)\n   1280x768      60.00 +\nDP-0 disconnected (normal left ' \
					b'inverted right x axis y axis)\nDP-1 disconnected (normal left inverted right x axis y axis)\n':
	os.system("xrandr --output VGA-0 --off --output LVDS-0 --mode 1920x1200 --pos 0x80 --rotate normal --output "
			  "DVI-D-0 --off --output DVI-D-1 --mode 1280x768 --pos 1920x0 --rotate left --output DP-0 --off "
			  "--output DP-1 --off")
	time.sleep(1) # wait a moment for the display settings to update
	os.system("nitrogen --restore") # set up wallpaper(s)

# if both screens are on, turn off the second screen
if result.stdout == b'Screen 0: minimum 8 x 8, current 2688 x 1280, maximum 8192 x 8192\nVGA-0 disconnected primary ' \
					b'(normal left inverted right x axis y axis)\nLVDS-0 connected 1920x1200+0+80 (normal left ' \
					b'inverted right x axis y axis) 367mm x 230mm\n   1920x1200     60.00*+  50.00  \nDVI-D-0 ' \
					b'disconnected (normal left inverted right x axis y axis)\nDVI-D-1 connected 768x1280+1920+0 ' \
					b'left (normal left inverted right x axis y axis) 230mm x 140mm\n   1280x768      ' \
					b'60.00*+\nDP-0 disconnected (normal left inverted right x axis y axis)\nDP-1 disconnected ' \
					b'(normal left inverted right x axis y axis)\n':
	os.system("xrandr --output VGA-0 --off --output LVDS-0 --mode 1920x1200 --pos 0x80 --rotate normal --output "
			  "DVI-D-0 --off --output DVI-D-1 --off --output DP-0 --off --output DP-1 --off")
	time.sleep(1) # wait a moment for the display settings to update
	os.system("nitrogen --restore") # set up wallpaper(s)
