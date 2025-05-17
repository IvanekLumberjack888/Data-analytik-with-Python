odd = "---"
# Ohlášení ve smyčkách

# break - přeskočí zbytek smyčky a pokračuje kódem pod ní(přeskočí i else)
# continue - vrací se k definici smyčky

index = 1

while index <= 6:
    print("index:", index)
    if index == 4:
        print("Mám hodnotu 4")
        break
    index = index + 1
print(odd)
# continue

index = 0

while index <= 19:
    index = index + 1
    # pokud je aktuální hodnota proměnné sudá,
    # pokračuj dále (přeskoč ji)
    if index % 2 == 0:
        continue
    print("index:", index)

# Řízené nekonečné smyčky
print(odd)

dotazovani = True

while dotazovani:
    odpoved = input("Zadej celé číslo od 1 do 5: ")
    
    if odpoved.isnumeric() and int(odpoved) in range (1, 6):
        print("Výborně")
        dotazovani = False
    else:
        print("Špatná hodnota, zkus to znovu.")

print(odd)

while True:
    odpoved = input("Zadej celé číslo od 1 do 5: ")
    if odpoved.isnumeric() and int(odpoved) in range(1, 6):
        print("Výborně")
        break
    else:
        print("Špatná hodnota, zkus to znovu.")