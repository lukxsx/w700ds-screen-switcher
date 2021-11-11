# w700ds-screen-switcher
Thinkpad W700ds is a special laptop with two screens. This Python script will turn the second monitor of Thinkpad W700ds on and off. This is very dirty script,
it only reads xrandr output and runs xrands-commands according to them. If only main display is on, it will start the second display, if both displays are on,
it will shut down the second display.

When the second display is opened or closed, the laptop sends "XF86Display" keypress. You can bind this script to "XF86Display" keypress. 

For example in i3
```
bindsym XF86Display exec python /location/to/script/screenchange.py
```
