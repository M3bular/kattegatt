# Uppgift 12
li = []
stor = ""
liten = ""
while True:
    ordet = input("Skriv in ett ord (tryck Enter för att avsluta): ")
    if ordet == "":
        break
    li.append(ordet)
    li.sort()
print(f"stora ordet: {li[-1]} lilla ordet: {li[0]}")
