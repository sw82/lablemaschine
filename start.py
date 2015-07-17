#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys, time, datetime, subprocess
from PIL import Image, ImageFont, ImageDraw

# TODO
# [x] Umlaute
# [ ] Send to printer
# [ ]

# create folder
folder = "out"
if not os.path.exists(folder):
    os.makedirs(folder)

imgsize = 512

lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)

taglines = ['Gib diesen Zettel weiter an eine Person, der du 200 Euro leihen würdest.',
    'Gib diesen Zettel weiter an jemanden, den du überhaupt nicht einschätzen kannst.',
    'Gib diesen Zettel der Person, der du zutraust ein politisches Amt übernehmen zu können.',
    'Gib diesen Zettel jemandem, den du für verdächtig hältst.',
    'Gib diesen Zettel einer Person, die möglicherweise in der Zukunft die Religion wechselt.',
    'Gib diesen Zettel einer Person, die zur Gruppe der Urbanen-nonkonformen gehört.',
    'Gib diesen Zettel jemandem, den du für einen „Vielversprechenden Mittellosen“ hältst.',
    'Gib diesen Zettel an eine Person weiter, von der du glaubst, dass sie die gleiche Partei wählt wie du.',
    'Gib diesen Zettel jemandem weiter, von dem du vermutest, dass er zwei oder mehr Kinder hat und gut organisiert ist.',
    'Gib diesen Zettel einer Person, die dir vielversprechend erscheint.',
    'Gib diesen Zettel jemanden der dir heute Abend noch nicht aufgefallen ist.',
    'Gib diesen Zettel jemandem aus der bürgerlichen Mitte.',
    'Setze dich neben eine Person, die sich von dir sehr unterscheidet. Gib ihr diesen Zettel weiter.',
    'Gib diesen Zettel einer Person, die du gerne kennenlernen würdest.',
    'Gib diesen Zettel einer Person, die du bei dir zu Hause verstecken würdest, wenn sie gesucht wird.',
    'Gib diesen Zettel einer Person aus der spaßorientierten Unterschicht.',
    'Gib diesen Zettel einer Person, von der du glaubst, dass sie die gleiche Partei wählt wie du.',
    'Gib diesen Zettel einer Person, die nicht eindeutig nur weiblich oder nur männlich ist.',
    'Gib diesen Zettel einer Person, von der du glaubst, dass sie ähnliche Musik mag wie du.',
    'Gib diesen Zettel einer Person, von der du glaubst, dass sie ähnliche Bücher im Regal stehen hat wie du.',
    'Gib diesen Zettel einer Person, die möglicherweise nicht in Deutschland geboren wurde.',
    'Gib diesen Zettel an einen Menschen weiter, die/der in deinem Stadtbezirk/Kiez wohnen könnte.',
    'Gib diesen Zettel einer Person, die möglicherweise keine sozialen Netzwerke nutzt.',
    'Gib diesen Zettel einer Person, von der du glaubst, dass sie etwas verheimlicht.',
    'Gib diesen Zettel einer Person, die du möglicherweise wiedersehen willst.',
    'Gib diesen Zettel einer Person, die du schon mal irgendwo gesehen hast, aber nicht mehr sagen kannst, wann und wo.',
    'Gib den Zettel einer Person weiter, die dir gefällt.',
    'Gib diesen Zettel einer Person weiter, die dir schon den ganzen Abend aufgefallen ist.',
    'Gib diesen Zettel einer Person, mit der du gerne eine Gruppe bilden würdest, ohne diese Gruppe klar definieren zu müssen. ',
    'Nach welchen Kriterien könnte man die Menschen im Raum noch sortieren? Geh zum Feuer und stell dir vor, wie das aussehen könnte.',
    'Gib diesen Zettel einer Person, die dir heute Abend noch nicht aufgefallen ist.',
    'Fotografiere jemanden, den du nicht kennst und veröffentliche das Bild.',
    'Gib den Zettel an eine Person in deiner Nähe weiter, die aussieht als könnte sie eine Bedrohung darstellen.',
    'Was ist unberechenbar an Dir? Gib den Zettel an eine Person in deiner Nähe weiter, die unberechnbar wirkt.',
    'Gib diesen Zettel einer Person weiter, die du bei einer Lebensentscheidung um Rat fragen würdest.',
    'Welche Entscheidung würdest du gerne an einen Computer abgeben? Geh zu einer Person deiner Wahl und tausche dich darüber aus.',
    'Gib diesen Zettel einer Person weiter, die dich irritiert.',
    'Gib diesen Zettel einer Person, die aussieht als würde sie eine Programmiersprache verstehen. Lass dir den Vorgang des Programmierens erklären.',
    'Such dir zwei Personen, mit der gleichen Haarfarbe wie du. Macht ein Gruppenfoto.',
    'Such dir zwei Personen, mit dem gleichen Kleidungsstil wie du. Macht ein Gruppenfoto.',
    'Such dir zwei Personen, die im gleichen Stadtteil / in der gleichen Stadt wohnen wie du und macht ein Gruppenfoto.',
    'Such dir zwei Personen mit denen du etwas gemeinsam hast. Macht ein Gruppenfoto.',
    'Gib diesen Zettel einer Person, die so aussieht als wäre es gut wenn sie das Thema Datenshcutz ernster nehmen würde.',
    'Gib diesen Zettel einer Person, von der glaubst, dass sie bewusst Daten verschlüsselt oder falsche Namen und Mailadressen angibt.',
    'Gib den Zettel weiter an eine Person, der du zutraust, dass sie heute mal geschummelt oder falsche Antworten gegeben hat.',
    'Gib den Zettel an einen Menschen, der in kein Raster passt.',
    'Gib den Zettel einer Person weiter und lass die Person raten, in welchem Stadtviertel du wohnst.',
    'Gib den zettel weiter an eine Person, von der du glaubst, dass sie sich nicht gern in Kategorien einordnen lässt.',
    'Gib den Zettel an eine Person weiter, die du einer Minderheit zuordnen würdest.',
    'Gib den Zettel an eine Person weiter und bitte diese Person, dich in drei Sätzen zu beschreiben.',
    'Mach mal nen bisschen Rabatz.',
    'Ab an die Bar und jemanden auf nen Schnäpperken einladen. Vorher dafür jemanden vom Feuer holen.',
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
    'Wer um Dich herum, hat ein Problem damit, sich einer Gruppe zuzuordnen? Rede mit ihm!',
    'Das Gras wächst nicht schneller, wenn man daran zieht!',
    'Die Menschen stolpern nicht über Berge, sondern über Maulwurfshügel. Begradige einen!',
    'Stille Wasser sind auch nass. Hol Dir eins an der Bar',
    'Heute schon gespendet?',
    'Paczka 2015',
    'brainslug.me',
    'Feldversuch 2015'
    ]

# Image stuff
# use a truetype font
fontt = ImageFont.truetype("assets/Arizonia.ttf", 15)

lengthoftaglines = len(taglines)
running = True

while running:

    #os.system("stty -echo")
    diary = int(raw_input())
    #os.system("stty echo")



    if (diary <= lengthoftaglines):

        lenghtofcurrenttagline = len(taglines[diary])
        print taglines[diary]

        img = Image.new( 'RGB', (imgsize,imgsize), "black") # create a new black image
        pixels = img.load() # create the pixel map

        for i in range(img.size[0]):    # for every pixel:
            for j in range(img.size[1]):
                pixels[i,j] = (i, j, 100) # set the colour accordingly

        #Add text
        draw = ImageDraw.Draw(img)
        #ImageFont.ImageFont.getsize(taglines[diary])
        draw.text((10, 50), taglines[diary], font=fontt )


        ts = time.time()
        # 2012-12-15 01:21:05
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        imagefile = folder +'/' + st + '.bmp'
        img.save(imagefile,"BMP")

        #print
        lpr.stdin.write(imagefile)
        #os.system("lpr -P printer_name file_name.txt")

    else:
        print 'Not yet here'
else:
    print 'The while loop is over.'
print 'Done'
