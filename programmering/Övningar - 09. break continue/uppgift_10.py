# Uppgift 10
i = 5
while i in range(5, 50):
    if i % 2 == 0 and i % 3 == 0:
        i += 2
        continue
    elif i >= 45:
        break
    else:
        print(i)
        i+=1