# Uppgift 6
mydic = {}
text = "python är roligt och python är populärt"
for i in text.split():
    check = text.split()
    if i not in mydic:
        mydic.update({i: check.count(i)})
print(mydic)
