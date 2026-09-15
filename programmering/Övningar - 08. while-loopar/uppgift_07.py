# Uppgift 7
userinput=0
hemligt=1
försök=0
while userinput != hemligt:
    userinput=int(input('vad är talet?'))
    försök+=1  
print('det tog', försök, 'försök att få rätt')