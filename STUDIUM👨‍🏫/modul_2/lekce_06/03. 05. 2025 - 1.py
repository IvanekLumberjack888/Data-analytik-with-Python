#zkouška, zda je heslo ve správném formátu
# Obsahuje minimálně 14 znaků
# A jedno malé a jedno velké písmeno
# číslo
# a speciální znak
print("---" * 3)
print("Generator 💪 silného 🛡️  hesla.")
print("---" * 3)
print("⁉️  Pokud heslo bude obsahovat: 1x malé písmeno a 1x VELKÉ písmeno a taky číslo a hlavně taky speciální znak (např: @&#|*?!)\n✅ Tak to bude OK 🆗")
print("......ok?....jdeme na to.")
print("""--->""")
heslo = input("Zadej silné heslo -> ")
#jedem bomby
male_pismeno = False
velke_pismeno = False
cislice = False
specialka = False
for znak in heslo:
    if znak.islower():
        male_pismeno = True
    elif znak.isupper():
        velke_pismeno = True
    elif znak.isdigit():
        cislice = True
    elif not znak.isalnum():
        specialka = True

if len(heslo) >= 14 and male_pismeno and velke_pismeno and specialka:
    print(""" 🫢  uaaauuuuu ..Heslo máš dostatečně silné 👍\nP""")
else:
    print("...jejda 🙀,\n...tak ješte není dostatěčně silné (jak silnice) 😆🤣\n...❓ Proč❔ ")   
    if len(heslo) < 14:
        print(" -> Má méně než 14 znaků. Zkus to ještě poladit.")
    if not male_pismeno:
        print(" -> Co takhle tam přidat malé pismeno? Alespoň jedno.")
    if not velke_pismeno:
        print(" -> Co takhle tam přidat VELKÉ písmeno? Alespoň jedno.")
    if not specialka:
        print(" -> A co speciální znak? 😉")
    if not cislice:
        print(" -> Že by chybělo číslo? Alespoň jedno?")