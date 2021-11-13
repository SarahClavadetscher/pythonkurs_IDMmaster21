#Artikel einlesen und aufbereiten
with open ("all_stories_temp_0_iso_short.txt", "r", encoding = "utf-8") as datei:
    content = datei.read()

zeichenliste = ['.', ',', ':', ';', '!', '?','«', '»']


for zeichen in zeichenliste:
    if zeichen in content:
            content = content.replace(zeichen, "")
            
content = content.lower().split()
print(content)

#Stopwortliste importieren
with open ("stopwords_german.txt", "r", encoding = "utf-8") as datei2:
    stopworte = datei2.read()
    
stopworte = stopworte.replace("\n", " ")
stopworte = stopworte.split()


#Stopworte aus Artikel entfernen
for stopwort in stopworte:
    if stopwort in content:
        content.remove(stopwort)

print(content)


#Sentimentlisten importieren und aufbereiten
with open ("SentiWS_v2.0_Negative.txt", "r", encoding = "utf-8") as datei3:
    negSent = datei3.readlines()


sentListe = []

for line in negSent:
    datatuple = line.lower().split()
    datatuple[0] = datatuple[0].split("|")[0]
    if len(datatuple) > 2:
        datatuple[2] = datatuple[2].split(",")
    
    sentListe.append(datatuple)

print(sentListe)


with open ("SentiWS_v2.0_Positive.txt", "r", encoding = "utf-8") as datei4:
    posSent = datei4.readlines()


for line in posSent:
    datatuple = line.lower().split()
    datatuple[0] = datatuple[0].split("|")[0]
    if len(datatuple) > 2:
        datatuple[2] = datatuple[2].split(",")
    
    sentListe.append(datatuple)

#Ergebnis: eine Liste mit positiven und negativen Wörtern
print(sentListe)

#Berechnung des Sentimentwerts für den Artikel
sentWert = 0
contentsentdict = {}

for datatuple in sentListe:
    if datatuple[0] in content:
        sentWert = sentWert + float(datatuple[1])
        contentsentdict[datatuple[0]] = float(datatuple[1])
    elif len(datatuple) > 2:
        for element in datatuple[2]:
            if element in content:
              sentWert = sentWert + float(datatuple[1])
              contentsentdict[datatuple[0]] = float(datatuple[1])

print(contentsentdict)

sentwortmax = max([n for n in contentsentdict.values() if n>0])
sentwortmin = min([n for n in contentsentdict.values() if n<0])

print("Sentimentwert:", sentWert)

for key, value in contentsentdict.items():
    if value == sentwortmax:
        print(key, value)

for key, value in contentsentdict.items():
    if value == sentwortmin:
        print(key, value)