# Uppgift 1
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
    
    if li.count(current_word) > 1 and current_word not in checked_words:
        checked_words.append(current_word)
        
        positions = []
        for j in range(len(li)):
            if li[j] == current_word:
                positions.append(j)
            #end if
        #end for
        
        print(f"Ordet {current_word} förekommer i index: {positions}")
    #end if
    
#end for