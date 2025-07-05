<<<<<<< HEAD
seznam = [1, 2, 3]
iterator = iter(seznam)
print(next(iterator))  # 1
print(next(iterator))  # 2

seznam_tymu = ["Tým A", "Tým B", "Tým C"]
polozka = ""
for i, polozka in enumerate(seznam_tymu, start=0):
    print(f"{i}: {polozka}")

# jablka a hrušky
ovoce = {"ovoce": ["jablko", "hruška", "banán"], "zelenina": ["mrkev", "brambora", "cibule"]}
for i, (polozka) in enumerate(ovoce["ovoce"], start=1):
    print(f"{i}: {polozka}")

else:
    # Přidání dalších položek do seznamu ovoce
    ovoce["ovoce"].extend(["kiwi", "pomeranč", "broskev"])
    
    for i, polozka in enumerate(ovoce["ovoce"], start=1):
        print(f"{i}: {polozka}")
=======
seznam = [1, 2, 3]
iterator = iter(seznam)
print(next(iterator))  # 1
print(next(iterator))  # 2

seznam_tymu = ["Tým A", "Tým B", "Tým C"]
polozka = ""
for i, polozka in enumerate(seznam_tymu, start=0):
    print(f"{i}: {polozka}")

# jablka a hrušky
ovoce = {"ovoce": ["jablko", "hruška", "banán"], "zelenina": ["mrkev", "brambora", "cibule"]}
for i, (polozka) in enumerate(ovoce["ovoce"], start=1):
    print(f"{i}: {polozka}")

else:
    # Přidání dalších položek do seznamu ovoce
    ovoce["ovoce"].extend(["kiwi", "pomeranč", "broskev"])
    
    for i, polozka in enumerate(ovoce["ovoce"], start=1):
        print(f"{i}: {polozka}")
>>>>>>> 779e25b96b82147dab8ec2afdb6117bebfec1cdd
# Výstup: 0: jablko, 1: hruška, 2: banán