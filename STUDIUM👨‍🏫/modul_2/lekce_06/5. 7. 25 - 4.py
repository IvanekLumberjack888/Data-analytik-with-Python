# range
# modelování čísel v Pythonu bude dneska o range
# range je funkce, která generuje posloupnost čísel
# range(start, stop, step)
# start - počáteční hodnota (včetně)   
# stop - koncová hodnota (bez)
# step - krok, jakým se čísla generují (výchozí je 1)
oddelovac = "--⏭️--" * 2
# Čísla od 0 do 4
for i in range(5):
    print(i)
print(oddelovac)

print("Čísla od 3 do 8")
for i in range(3, 9):
    print(i)
print(oddelovac)

print("Sudá čísla od 0 do 10")
for i in range(0, 11, 2):
    print(i)
print(oddelovac)

print("Čísla pozpátku od 10 do 1")
for i in range(10, 0, -1):
    print(i)
print(oddelovac)
print("Čísla od 1 do 10, ale jen lichá")
for i in range(1, 11, 2):
    print(i)
print(oddelovac)