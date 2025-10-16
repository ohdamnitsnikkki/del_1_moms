import pandas as pd # ger tillgång till excel´

# Gör lista för resultat
data = []

# Loop som kontrollerar att användare endast fyller i siffror 
while True:
    belopp_input = input("Skriv belopp i siffror: ")

    try:
        belopp = float(belopp_input)
        break
    except ValueError:
        # Ger felmeddelande till användaren
        print("Ogiltigt belopp, använd endast siffror. Försök igen.\n")


#Beräkna belopp med 25 % moms
belopp_med_moms = belopp * 1.25

# Visa resultat med max två decimaler
print(f"\nBelopp utan moms: {belopp:.2f} kr")
print(f"\nBelopp med 25% moms: {belopp_med_moms:.2f} kr")

# Lägg till i listan för att kunna spara det i excel
data.append({"Belopp utan moms": belopp, "Belopp med moms": round(belopp_med_moms, 2)})

#Skapa datum till beloppen
df = pd.DataFrame(data)


# Spara till excel
filnamn = "moms.xlsx"
df.to_excel(filnamn, index=False)

print(f"\n Priset har sparats i '{filnamn}'.")