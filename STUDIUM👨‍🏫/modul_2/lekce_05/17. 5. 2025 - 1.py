oddelovac = "---"
# while cyklus
index = 0

while index < 27:
   if index > 3:
       print("index:", index)
   index = index + 1

print("Smyčka skončila")

print(oddelovac)

index = 0
# kombinace podmínkového zápisu
# s logickým operátorem, kdy jeden je *False*
while index < 5 and index // 2 == 1:
    print("index:", index)
    index = index + 1
print("Smyčka skončila")

print(oddelovac)

# while je True a je tam or
index = 0
# kombinace podmínkového zápisu
# s logickým operátorem
while index < 5 or index == 10:
    print("index", index)
    index = index + 1

print("Smyčka skončila")
print(oddelovac)