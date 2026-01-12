#1

import random
enpont = 0
szgpont = 0
for i in range(5):
    entipp = input("kő, papír, olló?").lower()
    szgtipp = random.choice(("kő", "papír", "olló"))
    if entipp == szgtipp:
        print("Mindkettőtök tippje a(z) {entipp}")
    elif entipp == "kő" and szgtipp == "olló" or entipp == "olló" and szgtipp == "papír" or entipp == "papír" and szgtipp == "kő":
        print("Megnyerted a kört")
        enpont += 1
    else:
        print("Elveszítetted a kört")
        szgpont += 1
if enpont > szgpont:
    print("Nyertél")
elif enpont < szgpont:
    print("Vesztettél")
else:
    print("Döntetlen")

#2

szoveg = input("Írj be egy mondatot:").lower()
ujszoveg =""
for karakter in szoveg:
    if karakter == "a": ujszoveg += "4"
    elif karakter == "e": ujszoveg += "3"
    elif karakter == "i"or karakter == "í": ujszoveg += "1"
    elif karakter == "o": ujszoveg += "0"
    else: ujszoveg += karakter
print(ujszoveg.capitalize())

#3

prim = True
szam = int(input("Adj meg egy egész szamot:"))
if szam < 0:
    print("A szám negatív")
elif szam == 0:
    print("A szám nulla, nem prím")
elif szam == 1:
    print("A szám egy, nem prím")
elif szam == 2:
    print("A szám kettő, prím")
else:
    for oszto in range(2, szam // 2 + 1):
        if szam % oszto == 0:
            prim = False
            break
if prim:
    print(f"A {szam} prím")
else:
    print(f"A {szam} nem prím")
    
#4

szamlalo = 0
for perc in range(1,13):
    pulzus = random.randint(110,190)
    if pulzus < 140:
        zona = "Bemelegítő zóna"
    elif 140 <= pulzus <= 165:
        zona = "Zsírégető zóna"
    else:
        szamlalo += 1
        zona = "Anaerob zóna"
    print(f"{perc}. perc: {pulzus} bpm - {zona}")
print(f"Veszélyes zónába léptél {szamlalo} alkalommal")

#5

sárkány = 300
for kor in range(1,6):
    print(f"{kor} kör")
    asebzes = random.randint(20,100)
    seb = random.randint(1,5)
    if seb == 5:
        asebzes*=2
        print("Kritikus")
    elif seb == 1:
        print("Mellé")
        asebzes = 0
    else:
        print({asebzes})
        sárkány -= asebzes
    if sárkány < 0:
        print(f"győzelem")
        break


    
    