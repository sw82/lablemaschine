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
    sys.stdout.write(str(cfg.bLength) + '\n')
    sys.stdout.write(str(cfg.bNumConfigurations) + '\n')
    sys.stdout.write(str(cfg.bDeviceClass) + '\n')

    # for intf in cfg:
    #     sys.stdout.write('\t' + \
    #                      str(intf.bInterfaceNumber) + \
    #                      ',' + \
    #                      str(intf.bAlternateSetting) + \
    #                      '\n')
    #     for ep in intf:
    #         sys.stdout.write('\t\t' + \
    #                          str(ep.bEndpointAddress) + \
    #                          '\n')
