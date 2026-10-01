# Uppgift 11
var=0
langder = []

while True:
    langd = int(input("Ange elevens längd i cm (0 för att avsluta): "))
    if langd == 0:
        break
    langder.append(langd)
    var+=1
langder.sort()
print(langd/var)
print(langder[0],langder[-1])
