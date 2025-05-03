#destinatio
"""Program bude umět:

    1. Vybrat pouze z nabídky (1 - 6),
    2. Ppřepočítat cenu, pokud bude sleva,
    3. Pracovat pouze s křestním jménem,
    4. Zakázat uživatelům mladším 18 let nakupovat,
ověřovat mailové adresy."""

mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]

ceny = (150, 200, 120, 120, 100, 180)

slevy = ("Olomouc", "Svitavy", "Ostrava")

domeny = ("gmail.com", "seznam.cz", "email.cz")

dvojita_cara = "=" * 35
cara = "-" * 35

nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""

AKT_ROK = 2025

print("VITEJTE U NASI APLIKACE DESTINATIO!" )
print(dvojita_cara, end="")
print(nabidka, end="")
print(dvojita_cara)

cislo_destinace = int(input("Vyber cislo destinace: "))

if 1 <= cislo_destinace <= 6:
    destinace_nazev = mesta[cislo_destinace - 1]
    print("Vybral jsi: ", destinace_nazev)
else:
    print("Destinace cislo " , cislo_destinace, "NEEXISTUJE!")
    quit()
print(cara)

# pokud zadana destinace bude v seznamu slev:
if destinace_nazev in slevy:
    nova_cena = 0.75 * ceny[cislo_destinace - 1]
    print("Ziskavate 25% slevu! Nova cena: ",str(nova_cena)+",-")
    print(cara)
else:
    nova_cena = ceny[cislo_destinace - 1]
    print("Jizdenka bez slevy. Cena: "+ str(nova_cena)+",-")
    print(cara)

cele_jmeno = input("Vase cele jmeno: ")
krestni_jm = cele_jmeno.split()[0]
if krestni_jm.isalpha():
    print("Krestni jmeno: ", krestni_jm)  
else:
    print("Vase cele jmeno asi není: ", cele_jmeno, "\nNeplatne jmeno!")
    quit()
print(cara)

#Vas rok narozeni: 1989 # input
# Pristup povolen...
# -----------------------------------
# pokud uzivateli je pod 18 let
# Vas rok narozeni: 2010 input
# Jste prilis mlady na nakup jizdenek!
# Ukoncuji program

plnoletost = int(input("Vas rok narozeni je?: "))
AKT_ROK = 2025
if (AKT_ROK - plnoletost) >= 18:
    print("Pristup povolen...")
else:
    print("Vas rok narozeni: ", plnoletost)
    print("Jste prilis mlady na nakup jizdenek!\nUkoncuji program")
    quit()
print(cara)

# pokud je domena e-mailu v seznamu domen:
mailik = input("Zapiste Vasi e-mailovou adresu: ")
if "@" in mailik and mailik.split("@")[1] in domeny:
    print("Overeni e-mailu probehlo v poradku.")
else:
    print("Mate opravdu tuto adresu?: ", mailik)
    print("Tento e-mail je neplatny!" )
    print("Ukoncuji program")
    quit()
print(dvojita_cara)
print("Dekuji, "+ krestni_jm + " za objednavku jizdenky.")
print("Cilova destinace: " + destinace_nazev + ", cena jizdneho: " + str(nova_cena)+",-")
print("Na Vas e-mail: " + mailik + " jsme odeslali e-jizdenku.\nZkontrolujte svuj e-mail 📩") 
print(dvojita_cara)