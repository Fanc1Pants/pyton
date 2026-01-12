#1

for szam in range (100,201):
    if szam % 2 == 0:
        print(f"{szam} páros")
    else:
        print(f"{szam} páratlan")

#2

import random 
veletlen = random.randint (1,20)
print(f"A véletlen szám {veletlen}")
print(f"Az osztói:")
for oszto in range(1,veletlen+1):
    if veletlen % oszto == 0:
        print(oszto, end=" ")

#3

harom = 0; ot = 0; egyikse = 0
for szam in range(1,51):
    if szam % 3 == 0:
        harom += 1
    if szam % 5 == 0:
        ot += 1
    if szam % 3 != 0 and szam % 5 != 0:
        egyikse += 1

print("\nHárommal osztható")
print("Öttel osztható")
print("Egyikkel sem osztható")


#4 2**2 négyzetre emelés

for szam in range(10,26):
    print(f"szám: {szam}, négyzete {szam**2}, köbe {szam**3}")

#5

for csillagszam in range(1,11):
    print(csillagszam * "*")

for szam in range(5,51):
    if szam < 10:
        print(f"{szam} egyjegyű")
    else:
        print(f"{szam} kétjegyű")

#6

for szam in range(50,9,-1):
    if szam % 7 == 0:
        print(f"hetes szám")
    if szam % 2 == 0:
        print(f"páros szám")
    if szam % 7 != 0 and szam % 2 != 0:
        print(szam)
