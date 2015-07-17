# USB  Button interface code
# Copyright 2015 Sebastian Winkler
# based on http://files.righto.com/files/PanicButton.py
# http://sbstnwnklr.com
#
""" Button - interface to USB Button

This code requires PyUSB.
"""

import usb.core

class Button:
  def __init__(self):
    # Device is: Bus 001 Device 008: ID 0d50:0141 Cleware GmbH

    self.dev = usb.core.find(idVendor=0x0d50, idProduct=0x0141)
    if not self.dev:
      raise ValueError("Button not found")

    try:
      self.dev.detach_kernel_driver(0) # Get rid of hidraw
    except Exception, e:
      pass # already unregistered

  def read(self):
    # Read the USB port. Return 1 if pressed and released, 0 otherwise.

    #Magic numbers are from http://search.cpan.org/~bkendi/Device-USB-PanicButton-0.04/lib/Device/USB/PanicButton.pm
    return self.dev.ctrl_transfer(bmRequestType=0xA1, bRequest=1, wValue=0x300, data_or_wLength=8, timeout=500)[0]

if __name__ == "__main__":
  import time
  button = PanicButton()
  while 1:
    if button.read():
      print "Pressed"
    time.sleep(.5)
