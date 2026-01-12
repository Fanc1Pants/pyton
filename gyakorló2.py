#1

import random
x = 0
y = 0
for i in range(20):
    iranyok = ("Észak","Dél","Kelet","Nyugat")
    irany = random.choice(iranyok)
    if irany == "Észak":
        y += 1 # y++ # y--
    elif irany == "Dél":
        y -= 1 
    elif irany == "Kelet":
        x += 1
    else:
        x -= 1
print(f"x,y: {x}, {y}")
print(f"Távolság: {abs(x) + abs(y)}")

#2

osszeg = 0
import random
for nap in range(1,11):
    talalt_penz = random.randint(100,500)
    osszeg += talalt_penz
    print(f"{nap}. nap. Találtam {talalt_penz} Ft-ot. Összesen {osszeg} Ft")
    if osszeg > 2500:
        print("Vehetek egy pizzát")
        osszeg -= 2500

#3

szokoz = 10
for szorzo in range(1,11):
    print(" "*szokoz, end="")
    print("*"*szorzo*2)
    szokoz -= 1

#4

a = 0; e = 0; i = 0; o = 0; u = 0
mondat = "Merry christmas and Happy New Year"
for betu in mondat.lower():
    if betu == "a": a += 1
    elif betu == "e" : e += 1
    elif betu == "i" : i += 1
    elif betu == "o" : o += 1
    elif betu == "u" : u += 1
print(a, e, i, o, u)

#5

nojogsi = 0
for auto in range(15):
    sebesseg = random.randint(30,100)
    if sebesseg <= 50:
        print(f" {auto}. Szabályos")
    elif 51 <= sebesseg <= 65:
        print(f" {auto}. Gyorshajtás - Csekk:20.000Ft")
    else:
        print(f" {auto}. Durva szabályszegés - Jogosítvány elvétele!")
        nojogsi += 1
print(f"{nojogsi} embernek vették el a jogosítványát.")

#6

talalt = False
for i in range(3):
    pin_kod = int(input("Add meg a PIN-kódod:"))
    if pin_kod == 1234:
        print("Belépés engedélyezve")
        talalt = True
        break
if talalt == False:
    print("Kártya zárolva")

#7

gyartosor = list()
for i in range(20):
    csoki = random.randint(90,110)
    gyartosor.append(csoki)

for csoki_suly in gyartosor: #egyesével végigmegy a listaelemeken
    if csoki_suly < 94 or csoki_suly > 106:
        print(f"{csoki_suly} SELELYT")
        selejt += 1
    else:
        print(f"{csoki_suly} OK")
print(f"selejtek száma {selejt}")

#8

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


