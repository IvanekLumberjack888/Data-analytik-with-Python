<<<<<<< HEAD
# Opakování seznamu s indexy
ovoce = {"ovoce": ["jablko", "hruška", "banán"]}
iterator = iter(ovoce["ovoce"])
print(f"{1}: {next(iterator)}")
print(f"{2}: {next(iterator)}")
print(f"{3}: {next(iterator)}")
# Výstup: 1: jablko, 2: hruška, 3: banán
# Opakování seznamu s indexy pomocí enumerate
# Použití enumerate pro získání indexu a položky
ovoce_list = ["jablko", "hruška", "banán"]
for i, polozka in enumerate(ovoce_list, start=1):
    # Začínáme od 1, takže start=1
    # i bude index položky v seznamu
    print(f"{i}: {polozka}")


# Výstup: 1: jablko, 2: hruška, 3: banán
zelenina = ["mrkev", "brambora", "cibule"]
zelenina.__iter__()
for i, polozka in enumerate(zelenina, start=1):
=======
# Opakování seznamu s indexy
ovoce = {"ovoce": ["jablko", "hruška", "banán"]}
iterator = iter(ovoce["ovoce"])
print(f"{1}: {next(iterator)}")
print(f"{2}: {next(iterator)}")
print(f"{3}: {next(iterator)}")
# Výstup: 1: jablko, 2: hruška, 3: banán
# Opakování seznamu s indexy pomocí enumerate
# Použití enumerate pro získání indexu a položky
ovoce_list = ["jablko", "hruška", "banán"]
for i, polozka in enumerate(ovoce_list, start=1):
    # Začínáme od 1, takže start=1
    # i bude index položky v seznamu
    print(f"{i}: {polozka}")


# Výstup: 1: jablko, 2: hruška, 3: banán
zelenina = ["mrkev", "brambora", "cibule"]
zelenina.__iter__()
for i, polozka in enumerate(zelenina, start=1):
>>>>>>> 779e25b96b82147dab8ec2afdb6117bebfec1cdd
    print(f"{i}: {polozka}")