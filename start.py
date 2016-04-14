#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# USB  Button interface code
# Copyright 2015 Sebastian Winkler
# http://sbstnwnklr.com

import os, sys, time, datetime, subprocess, Button
#usb.core, usb.util
from PIL import Image, ImageFont, ImageDraw
#to load a file
from ast import literal_eval
from random import randint
# TODO
# [x] Umlaute
# [x] Send to printer
# [ ] Print via Button pressed
# [ ] get lable printer installed
# [ ] create nice putput image
# [ ] make skript start after boot
# [x] taglines moved to file

imgsize_a       = 256
imgsize_b       = 128
printer_name    = "Brother_HL-2150N_series"
fontt           = ImageFont.truetype("assets/Arizonia.ttf", 12)
#button          = Button.Button(); # USB Device
folder          = "out"
if not os.path.exists(folder):
    os.makedirs(folder)

def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"

def image(num):

    im = Image.new('RGB', (imgsize_a, imgsize_b), "white") 
    draw = ImageDraw.Draw(im) 
    # draw.line((100,200, 150,300), fill=128)

    #Add text
    # draw = ImageDraw.Draw(im)

    # draw.polygon([(60,60), (90,60), (90,90), (60,90)], fill="red", outline="green")
    #ImageFont.ImageFont.getsize(taglines[num])
    draw.text((0, 0), str(taglines[num]), font=fontt ) #color="black"

    ts = time.time()
    # 2012-12-15 01:21:05
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    imagefile = folder +'/' + st + '.bmp'
    im.save(imagefile,"BMP")
    return imagefile

#read taglines from file
with open('taglines.txt') as f:
    taglines = [list(literal_eval(line)) for line in f]

while True:
    #if button.read():
    #print "Pressed"
    time.sleep(3.9)
    
    num = randint(0,len(taglines))
    #TODO input from button pressed
    
    print taglines[num]
    imagefile = image(num)
    

    #     # os.system("lpr -P " + printer_name + " " + shellquote(imagefile))
    
    # else:
    #     print 'Not yet here'
else:
    print 'The while loop is over.'
print 'Done'
