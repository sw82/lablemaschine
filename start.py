#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys

# TODO
# Umlaute
# Send to printer

taglines = [
    'Gib diesn Zettel jemanden, der besonders gut aussieht',
    'Gib dien Zettel jemanden, der aussieht als wuerde er die AfD waehlen.',
    'Gib diesen Zettel weiter an eine Person, der du deine Wohnung untervermieten würdest, so lange du im Urlaub bist.',
	'Gib diesen Zettel weiter an eine Person, der du 1000 Euro leihen würdest.',
	'Gib diesen Zettel weiter an jemanden, den du überhaupt nicht einschätzen kannst.',
	'Setze dich neben die Person, die dir hier im  Raum am ähnlichsten ist, oder in ihre Nähe, und gebe ihr dann diesen Zettel.',
	'Gib diesen Zettel weiter an die Person, die am glücklichsten aussieht.',
	'Gib diesen Zettel der Person, der du am ehesten zutraust ein politisches Amt übernehmen zu können.',
	'Gib diesen Zettel weiter an die Person, von der du denkst, dass sie am meisten Freunde hat.',
	'Gib diesen Zettel jemandem, den du für verdächtig hälst.',
	'Gib diesen Zettel einer Person, die du nicht kennst, aber gerne kennenlernen möchtest.',
	'Gehe in die Nähe einer Person die dir sehr sympathisch ist und gebe diesen Zettel dann weiter an eine andere Person in eurer Nähe.',
	'Wenn Sie mehr als 50 Euro Bargeld dabei haben, geben Sie jemandem einen Drink aus',
	'Wenn Sie v. a. aus beruflichen Gründen hier sind, finden sie jemanden der Sie herumführt',
	'Willst Du heute noch jemanden kennen lernen dann halte Dich an der Bar auf!'
    ]

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
