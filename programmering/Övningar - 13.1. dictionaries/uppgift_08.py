# Uppgift 8
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
mydic = {}
for i in b:
    print(i)
    if i not in mydic:
        mydic.update({i: b[i]})
for i in a:
    print(i)
    if i not in mydic:
        mydic.update({i: a[i]})
print(mydic)
