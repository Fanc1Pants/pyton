import random
kocka1 = random.randint(1,6)
lehetőségek = (1,2,3,4,5,6)
kocka2 = random.choice(lehetőségek)
print(f"At első kocka értéke {kocka1}")
print(f"A második kocka értéke {kocka2}")
if (kocka1 + kocka2) % 2 == 0:
    print("Páros a dobás eredménye")
else:
    print("páratlan a dobás eredménye")

tipp = input("Fej vagy írás?").lower()
# fej, írás, Fej, Írás, FEJ, ÍRÁS
oldalak = ("fej", "írás")
erme = random.choice(oldalak)
if tipp == erme:
    print("nyertél")
else:
    print("vesztettél")

jegy = random.randint(1,5)
szoveges = ("elégtelen","elégséges","közepes","Jó","jeles")
print(f"Az osztályzatod {jegy} ({szoveges[jegy-1]})")

meseszam = random.randint(1,10)
if meseszam in (3,7,9):
    print(f"A véletlen egy meseszámot sodort eléd")
else:
    print(f"A mesék a gyerekeknek valók")

allatok = ("kutya","macska","ló","tehén")
valasztas = random.choice(allatok)
if valasztas == "kutya" or "macska":
    print(f"A {valasztas} háziállat")

szam = random.randint(1,100)

