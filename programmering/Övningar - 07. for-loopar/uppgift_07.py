# Uppgift 7 7. Skriva ut bokstäver
# Be användaren skriva in en mening. Loopa sedan igenom varje tecken i meningen och skriv ut detta med en ’*’ mellan varje tecken.
m = str(input("vad är ditt mening david din jävla idiot!!!!!!!!!!!!"))
tm = ""
for x in m:
    tm += x+ "*"
print(tm[:-1])
