<<<<<<< HEAD
from itertools import zip_longest

jmena = ["Anna", "Petr", "Eva", "Karel", "Josef"]
vek = [25, 30, 35 , (40, "už není mezi námi"), 45]

for jmeno, vek_osoby in zip(jmena, vek):
    if isinstance(vek_osoby, tuple) and "už není mezi námi" in vek_osoby:
        print(f"{jmeno} už není")
        # Přeskočíme Karla
        continue
    print(f"{jmeno} má {vek_osoby} let")
# Výstup:
# Anna má 25 let
# Petr má 30 let
# Eva má 35 let
# Karel už není

# Příklad použití zip pro spojení dvou seznamů
# Pokud jsou seznamy různé délky, zip zastaví na nejkratším seznamu.
# Pokud chci spojit všechny položky, můžu použít itertools.zip_longest.
kratky = ["a", "b"]
dlouhy = [1, 2, 3, 4, 5]

list(zip(kratky, dlouhy))  # [('a', 1), ('b', 2)]
print("Tohle je výstup z zip:   ", list(zip(kratky, dlouhy)))
# Výstup: [('a', 1), ('b', 2)]
# Pokud jsou seznamy různé délky, zip zastaví na nejkratším seznamu.
# --
# nebo
# --
print("Tohle je výstup z zip_longest: ", end="")
print(list(zip_longest(kratky, dlouhy)))
print("Tohle je výstup z zip_longest: ", end="")
print(list(zip_longest(kratky, dlouhy)))

# Výstup: [('a', 1), ('b', 2), (None, 3), (None, 4), (None, 5)]

# Příklad použití enumerate pro získání indexu a položky
# Použití enumerate pro získání indexu a položky
seznam1 = ["a", "b", "c"]
seznam2 = [1, 2, 3]

for i, (x, y) in enumerate(zip(seznam1, seznam2)):
    print(f"Index {i}: {x} -> {y}")
# Výstup:
# Index 0: a -> 1
# Index 1: b -> 2
# Index 2: c -> 3
# Použití enumerate pro získání indexu a položky
seznam = ["a", "b", "c", "d", "e"]
seznam_s_indexy = enumerate(seznam, start=1)  # Začínáme od 1
for i, x in seznam_s_indexy:
    print(f"Index {i}: {x}")

seznam_psu = ["čivava", "husky", "labrador, světlý"]
hadi = ["krajta - královská","krajta - zelená", "kobra - čínská", "zmije jedovatá", "užovka - obojková"]
kdo_koho_sezral = zip(seznam_psu, hadi)
for pes, had in kdo_koho_sezral:
    print(f"{pes.upper()} sežral -----> {had.capitalize()}")
    print("co", "??? nebo takto ? 😉")
    print(f"{had.upper()} sežral -----> {pes.capitalize()}")
# Příklad použití zip a enumerate pro spojení dvou seznamů
# Použití zip pro spojení dvou seznamů
# Použití zip_longest pro spojení dvou seznamů s různými délkami
hadi = ["krajta - královská","krajta - zelená", "kobra - čínská", "zmije jedovatá", "užovka - obojková"]
seznam_psu = ["čivava", "husky", "labrador, světlý"]
kolik_hadů = len(hadi)
kolik_psů = len(seznam_psu)
# Výpis počtu hadů a psů
if kolik_hadů > kolik_psů:
    print("Je více hadů než psů.")
elif kolik_hadů < kolik_psů:
    print("Je více psů než hadů.")
else:
    print("Počet hadů a psů je stejný.")

print(f"Počet hadů: {kolik_hadů}, počet psů: {kolik_psů}")
print("Tohle je výstup z zip_longest: ", end="")
print(list(zip_longest(seznam_psu, hadi, fillvalue="nic")))
print("=" * 50 + "\nKdo myslíte, že by takhle mohl žrát? 😄😄😄😄😄\n" + "=" * 50)
kdo_koho_sezral_longest = zip_longest(seznam_psu, hadi, fillvalue="nic")
for pes, had in kdo_koho_sezral_longest:
    if pes == "nic":
        print(f"{had.capitalize()} už se nežrala, protože není pes.")
        continue
    if had == "nic":
        print(f"{pes.capitalize()} už se nežral, protože není had.")
        continue
    print(f"{pes.upper()} sežral -----> {had.capitalize()}")
    print("co", "??? nebo takto ? 😉")
    print(f"{had.upper()} sežral -----> {pes.capitalize()}")
print("Tohle je výstup z zip_longest: ", end="")
print(list(zip_longest(seznam_psu, hadi, fillvalue="nic")))
print("=" * 50 + "\nKdo myslíte, že by takhle mohl žrát? 😄😄😄😄😄\n" + "=" * 50)
# Příklad použití zip a enumerate pro spojení dvou seznamů
=======
from itertools import zip_longest

jmena = ["Anna", "Petr", "Eva", "Karel", "Josef"]
vek = [25, 30, 35 , (40, "už není mezi námi"), 45]

for jmeno, vek_osoby in zip(jmena, vek):
    if isinstance(vek_osoby, tuple) and "už není mezi námi" in vek_osoby:
        print(f"{jmeno} už není")
        # Přeskočíme Karla
        continue
    print(f"{jmeno} má {vek_osoby} let")
# Výstup:
# Anna má 25 let
# Petr má 30 let
# Eva má 35 let
# Karel už není

# Příklad použití zip pro spojení dvou seznamů
# Pokud jsou seznamy různé délky, zip zastaví na nejkratším seznamu.
# Pokud chci spojit všechny položky, můžu použít itertools.zip_longest.
kratky = ["a", "b"]
dlouhy = [1, 2, 3, 4, 5]

list(zip(kratky, dlouhy))  # [('a', 1), ('b', 2)]
print("Tohle je výstup z zip:   ", list(zip(kratky, dlouhy)))
# Výstup: [('a', 1), ('b', 2)]
# Pokud jsou seznamy různé délky, zip zastaví na nejkratším seznamu.
# --
# nebo
# --
print("Tohle je výstup z zip_longest: ", end="")
print(list(zip_longest(kratky, dlouhy)))
print("Tohle je výstup z zip_longest: ", end="")
print(list(zip_longest(kratky, dlouhy)))

# Výstup: [('a', 1), ('b', 2), (None, 3), (None, 4), (None, 5)]

# Příklad použití enumerate pro získání indexu a položky
# Použití enumerate pro získání indexu a položky
seznam1 = ["a", "b", "c"]
seznam2 = [1, 2, 3]

for i, (x, y) in enumerate(zip(seznam1, seznam2)):
    print(f"Index {i}: {x} -> {y}")
# Výstup:
# Index 0: a -> 1
# Index 1: b -> 2
# Index 2: c -> 3
# Použití enumerate pro získání indexu a položky
seznam = ["a", "b", "c", "d", "e"]
seznam_s_indexy = enumerate(seznam, start=1)  # Začínáme od 1
for i, x in seznam_s_indexy:
    print(f"Index {i}: {x}")

seznam_psu = ["čivava", "husky", "labrador, světlý"]
hadi = ["krajta - královská","krajta - zelená", "kobra - čínská", "zmije jedovatá", "užovka - obojková"]
kdo_koho_sezral = zip(seznam_psu, hadi)
for pes, had in kdo_koho_sezral:
    print(f"{pes.upper()} sežral -----> {had.capitalize()}")
    print("co", "??? nebo takto ? 😉")
    print(f"{had.upper()} sežral -----> {pes.capitalize()}")
# Příklad použití zip a enumerate pro spojení dvou seznamů
# Použití zip pro spojení dvou seznamů
# Použití zip_longest pro spojení dvou seznamů s různými délkami
hadi = ["krajta - královská","krajta - zelená", "kobra - čínská", "zmije jedovatá", "užovka - obojková"]
seznam_psu = ["čivava", "husky", "labrador, světlý"]
kolik_hadů = len(hadi)
kolik_psů = len(seznam_psu)
# Výpis počtu hadů a psů
if kolik_hadů > kolik_psů:
    print("Je více hadů než psů.")
elif kolik_hadů < kolik_psů:
    print("Je více psů než hadů.")
else:
    print("Počet hadů a psů je stejný.")

print(f"Počet hadů: {kolik_hadů}, počet psů: {kolik_psů}")
print("Tohle je výstup z zip_longest: ", end="")
print(list(zip_longest(seznam_psu, hadi, fillvalue="nic")))
print("=" * 50 + "\nKdo myslíte, že by takhle mohl žrát? 😄😄😄😄😄\n" + "=" * 50)
kdo_koho_sezral_longest = zip_longest(seznam_psu, hadi, fillvalue="nic")
for pes, had in kdo_koho_sezral_longest:
    if pes == "nic":
        print(f"{had.capitalize()} už se nežrala, protože není pes.")
        continue
    if had == "nic":
        print(f"{pes.capitalize()} už se nežral, protože není had.")
        continue
    print(f"{pes.upper()} sežral -----> {had.capitalize()}")
    print("co", "??? nebo takto ? 😉")
    print(f"{had.upper()} sežral -----> {pes.capitalize()}")
print("Tohle je výstup z zip_longest: ", end="")
print(list(zip_longest(seznam_psu, hadi, fillvalue="nic")))
print("=" * 50 + "\nKdo myslíte, že by takhle mohl žrát? 😄😄😄😄😄\n" + "=" * 50)
# Příklad použití zip a enumerate pro spojení dvou seznamů
>>>>>>> 779e25b96b82147dab8ec2afdb6117bebfec1cdd
# Použití zip pro spojení dvou seznamů