# Uppgift 12
li = []
stor = ""
liten = ""
while True:
    ordet = input("Skriv in ett ord (tryck Enter för att avsluta): ")
    if ordet == "":
        break
    li.append(ordet)
    for i in ordet:
        if len(i) < len(stor):
            stor = ordet
        elif len(i) > len(liten):
            liten = ordet
print(f"stora ordet: {stor} lilla ordet: {liten}")
#wip