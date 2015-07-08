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
	'Setze dich neben die Person, die dir hier im am ähnlichsten ist, oder in ihre Nähe, und gebe ihr dann diesen Zettel.',
	'Gib diesen Zettel weiter an die Person, die am glücklichsten aussieht.',
	'Gib diesen Zettel der Person, der du am ehesten zutraust ein politisches Amt übernehmen zu können.',
	'Gib diesen Zettel weiter an die Person, von der du denkst, dass sie am meisten Freunde hat.',
	'Gib diesen Zettel jemandem, den du für verdächtig hälst.',
	'Gib diesen Zettel einer Person, die du nicht kennst, aber gerne kennenlernen möchtest.',
	'Gehe in die Nähe einer Person die dir sehr sympathisch ist und gebe diesen Zettel dann weiter an eine andere Person in eurer Nähe.',
	'Wenn Du mehr als 50 Euro Bargeld dabei hast, gib jemandem einen Drink aus',
	'Wenn Du v. a. aus beruflichen Gründen hier sind, frage Dich warum Du hier bist',
	'Willst Du heute noch jemanden kennen lernen dann halte Dich an der Bar auf!',
    'Mit wem auf  würdest Du gerne mal zusammen arbeiten? Gib ihm den Zettel.',
    'Wer in Deiner Nähe hat den größten Dispo?',
    'Schau Dich um - wen kennst Du nicht? Rede mit ihm!',
    'Wer um Dich herum, hat ein Problem damit, sich einer Gruppe zuzuordnen? Rede mit ihm!'
    ]

wisewords = [
    'Das Gras wächst nicht schneller, wenn man daran zieht!',
    'Die Menschen stolpern nicht über Berge, sondern über Maulwurfshügel. Begradige einen!',
    'Stille Wasser sind auch nass. Hol Dir eins an der Bar',
    'Heute schon gespendet?'
]

advertising =[
    'Paczka 2015',
    'brainslug.me',
    'Feldversuch 2015'
]

lengthoftaglines = len(taglines)
running = True


while running:

    #os.system("stty -echo")
    diary = int(raw_input())
    #os.system("stty echo")

    if (diary <= lengthoftaglines):
        print taglines[diary]
    else:
        print 'Not yet here'
else:
    print 'The while loop is over.'
print 'Done'
