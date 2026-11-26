# Uppgift 9
data = [
    ("Anna", "Stockholm"),
    ("Olle", "Göteborg"),
    ("Lisa", "Stockholm"),
    ("Per", "Malmö"),
]
mydic = {}
count = 0
for i in data:
    stad = i[1]
    namn = i[0]
    if stad in mydic:
        mydic[stad].append(namn)
    else:
        mydic[stad] = [namn]

print(mydic)
