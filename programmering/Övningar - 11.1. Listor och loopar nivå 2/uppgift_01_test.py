# Uppgift 1
def amountCheck(blatte):
    if li.count(blatte) > 1 and current_word not in checked_words:
        checked_words.append(current_word)
    positionCheck()
    #end if
#end def    
    
def positionCheck():
    positions = []
    for anes in range(len(li)):
        if li[anes] == current_word:
            positions.append(anes)
        #end if
    #end for
    print(f"Ordet {current_word} förekommer i index: {positions}")
#end def

test = []
li = []
while True:
    ord = input("Skriv ett ord (STOP för att avsluta): ")
    if ord == "STOP":
        break
    li.append(ord)

checked_words = []

for i in range(len(li)):
    current_word = li[i]
    amountCheck(current_word)
#end for