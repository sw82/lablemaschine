# lablemaschine

# About

Fun thingy to print via button pressed to a label printer.
From an array of quotes the user picks an items which will be printed.

# Libraries
os
sys
time
datetime
subprocess
usb.core
usb.util
Button (included)
# Setup

## Output folder
All files are stored within this repositories specified output folder. If you change the name, also change .gitignore

## Printer
Figure out your printer and set it as variable.

Linux
> lpstat -p -d

Set the default printer
> lpoptions -d printer

## USB Device

Figure out which is your USB input
>lsusb
