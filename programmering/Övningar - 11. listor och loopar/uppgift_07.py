# Uppgift 7
li = []
tal = 1337
while tal != 0:
    tal = int(input("Skriv ett heltal (0 för att avsluta): "))
    if tal == 0:
        break
    if tal % 2 == 0:
        li.append(tal)
print(li)
