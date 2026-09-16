# Uppgift 9

val=0
tal1 = int(0)
tal2 = int(0)
while val != 3:
    print("\n\n1. Addera två tal")
    print("2. Subtrahera två tal")
    print("3. Avsluta")
    val = int(input("Vad väljer du?"))
    if val == 1:
        tal1 = int(input("tal1 "))
        tal2 = int(input("tal2 "))
        print(tal1 + tal2)
        val=0
    elif val == 2:
        tal1 = int(input("tal1 "))
        tal2 = int(input("tal2 "))
        print(tal1 - tal2)
        val = 0
    elif val == 3:
        print("goodbaj")
    else:
        print("talet finns inte med yani")
