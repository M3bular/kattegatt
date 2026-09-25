# Uppgift 15
import random

slumpmässiga_tal = [random.randint(1, 100) for i in range(5)]
slumpmässiga_tal.sort()

print(slumpmässiga_tal[0], slumpmässiga_tal[-1])
