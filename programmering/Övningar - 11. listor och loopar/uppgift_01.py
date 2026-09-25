# Uppgift 1
lista=[]
ord="david"
while True:
    ord=(str(input('vad är ditt ord?')))
    if ord =="STOP":
        break
    else:
        lista.append(ord)
print(lista)