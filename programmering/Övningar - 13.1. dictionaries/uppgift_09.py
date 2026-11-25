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
    staddic = data[count][1]
    if staddic not in mydic:
        mydic.update({staddic: ""})
    print(mydic)
    """ 
    namndic=(data[count][0])
    print(data[count][0])
    print(data[count][1])
    count += 1 """
