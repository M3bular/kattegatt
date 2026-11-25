# Uppgift 7
mydic = {}
d = {"a": 1, "b": 2, "c": 3}
for i in d:
    mydic.update({d[i]: i})
print(mydic)
