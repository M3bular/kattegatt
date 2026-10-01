# Uppgift 10
udda = []
li = []
while True:
    heltal = int(input("Skriv ett heltal (0 för att avsluta): "))
    if heltal == 0:
        break
    elif heltal % 2 == 0:
        li.append(heltal)
    elif heltal % 2 == 1:
        udda.append(heltal)
    else:
        continue
print(sum(li))
print(sum(udda))
print(li)
print(udda)
