# Uppgift 9

ord = []
ord1 = []
while True:
    var = input("Skriv ett ord (eller STOP för att avsluta): ")
    if var == "STOP":
        break
    ord.append(var)

for i in ord:
    if ord.count(i) == 1:
        ord1.append(i)
print(ord1)
