# Uppgift 5
medel=0
counter=0
tal=1337
while tal != 0:
    tal = int(input("Skriv ett heltal (0 för att avsluta): "))
    if tal==0:
        break
    medel+=tal
    counter+=1
    
print(medel / counter)