#1
import random
fejek = random.randint(1,9)
szinek = ("zöld","piros","fekete")
szin = random.choice(szinek)
if fejek == 1 and szin == "zöld":
    print("Szia Süsü")
elif fejek in (1,2,3,4):
    print(f"A {szin} sárkány gyenge")
elif fejek in (5,6,7):
    print(f"A {szin} sárkány közepes erejű")
else:
    print(f"A {szin} sárkány félelmetes")

#2
import random
kincsek = ("arany","ezüst","semmI")
kincs = random.choice(kincsek)
ero = random.randint(1,5)
if ero < 3:
    print("A kulcs túl gyenge, a láda zárva maradt")
elif ero == "semmi":
    print("A láda üres")
else: 
    print(f"A láda tartalma {kincs}")

#3
karakterek = ("lovag","kereskedő","paraszt")
karakter = random.choice(karakterek)
hid = random.randint(50,200)
suly = random.randint(70,120)
if hid < suly:
    print("A híd leszakadt, nem tudsz úszni és megfulladsz")
elif hid >= suly and (hid-suly) <= 10:
    print(f"A híd recseg, de a {karakter} átér")
else:
    print(f"A {karakter} gond nélkül átjut a hídom")

#4
meseszamok = (3,7,9,12)
meseszam = random.choice(meseszamok)
jutalmak = ("drágakő","arany","ezüst")
jutalom = random.choice(jutalmak)
if meseszam % 2 == 0:
    print(f"Oof, a jutalmad {jutalom}")
elif meseszam in (3,9):
    print(f"Kis próba vár rád, de {jutalom} a jutalom")
else:
    print(f"Hét próban kell keresztülmenned az áletedért")

#5
specialitasok = ("tűz","víz","föld")
varazslo1 = random.choice(specialitasok)
varazslo2= random.choice(specialitasok)
if varazslo1 == "tűz" and varazslo2 == "föld" or varazslo1 == "víz" and varazslo2 == "tűz" or varazslo1 == "föld"and varazslo2 == "víz":
    print("AZ első varazsló győzött")
elif varazslo1 == varazslo2:
    print("Döntetlen")
else:
    print("A második varázsló győzött")
    