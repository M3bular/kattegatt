# Uppgift 9
hittade_faktor = False

for i in range(2, 96):
    if 97 % i == 0:
        hittade_faktor = True
        break

if hittade_faktor:
    print("97 är inte ett primtal.")
else:
    print("97 är ett primtal.")
