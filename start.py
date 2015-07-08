#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys

# TODO
# Umlaute
# Send to printer

taglines = [
    'Gebe diese note jemanden, der besonders gut aussieht',
    'Gebe diesen Zettel jämander, der aussieht als wuerde er die AfD waehlen.',
    's gibt nichts Gutes, ausser man tut es.', 'pups']

lengthoftaglines = len(taglines)
running = True
 

while running:

    os.system("stty -echo")
    diary = int(raw_input())
    os.system("stty echo")

    if (diary <= lengthoftaglines):
        print taglines[diary]
    else:
        print 'Not yet here'
else:
    print 'The while loop is over.'
print 'Done'
