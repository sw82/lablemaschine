# USB  Button test file
# Copyright 2015 Sebastian Winkler
# http://sbstnwnklr.com
#

import usb.core, sys, usb.util

dev = usb.core.find(idVendor=0x0d50, idProduct=0x0141)

if dev is None:
    raise ValueError('Our device is not connected')

for cfg in dev:
    sys.stdout.write(str(cfg.bConfigurationValue) + '\n')
