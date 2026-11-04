# Sortera utan inbyggda funktioner (Bubble Sort)

li = []

while True:
    ordet = input("Skriv ett tal (eller STOP för att avsluta): ")
    if ordet == "STOP":
        break
    li.append(ordet)
for grej in li:
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            temp = li[i]
            li[i] = li[i + 1]
            li[i + 1] = temp
print(li)


li.sort()