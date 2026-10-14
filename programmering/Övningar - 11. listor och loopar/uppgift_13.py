# Uppgift 13

temperaturer = []
minus=0
counter = 0
while True:
    temperatur = int(input("Mata in dagens temperatur (999 för att avsluta): "))
    if temperatur == 999:
        break
    temperaturer.append(temperatur)
    if temperatur<0: minus=+1
    counter = +1
temperaturer.sort()    
print(temperaturer)
print(sum(temperaturer) / counter)
print(minus)
print(f"Högsta: {temperaturer[-1]} Lägsta: {temperaturer[0]}")

