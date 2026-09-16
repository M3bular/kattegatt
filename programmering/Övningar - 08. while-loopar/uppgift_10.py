# Uppgift 10
import random
tal = random.randint(1, 100)
gissning = 0

while gissning != tal:
	gissning = int(input("Gissa ett tal mellan 1 och 100: "))

	if gissning < tal:
		print("Talet är för litet.")
	elif gissning > tal:
		print("Talet är för stort.")
	else:
		print("Rätt gissat!")