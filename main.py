import pandas as pd # ger tillgång till excel´

# Gör lista för resultat
data = []

while True:
    belopp_input = input("Skriv belopp i siffror: ")

    try:
        belopp = float(belopp_input)
        break
    except ValueError:
        print("Ogiltigt belopp, använd endast siffror. Försök igen.\n")