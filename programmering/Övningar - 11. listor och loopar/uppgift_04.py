# Uppgift 4
pos=0
neg=0
tal=1337
while True:
    tal=int(input("vad tal tills 0?"))
    if tal==0:
        break
    if tal >0:
        pos+=1
    else:
        neg+=1
print(f"{pos}, antal positiva")
print(f"{neg}, antal negativa")