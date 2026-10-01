li = []

while True:
    ord = input("Mata in ett ord (STOP för att avsluta): ")
    if ord == "STOP":
        break
    li.append(ord)

sokt_ord = input("Skriv ett ord: ")
print(li.count(sokt_ord))