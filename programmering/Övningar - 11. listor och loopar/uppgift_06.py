# Uppgift 6
li=[]
var=1337
while var!=0:
    var=int(input('vad vill du säger????'))
    if var==0:
        break
    li.append(var)
li.sort()
print(li[0],li[-1])
    