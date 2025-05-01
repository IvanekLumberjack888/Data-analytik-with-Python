print("Pokračujeme.")
#opakování
print(10 + 5) #15
print(10 - 3) #7
print(10 * 2) #20
print(10 / 4) #2.5 float
print(10 // 4) #2
print(10 % 4) #2
print(2 ** 3) #8

#boolean
print(5 < 10)   # True
print(5 == 5)   # True
print(5 != 3)   # True
print(5 > 10)   # False

x = 3
if x > 5:
    print("A")
elif x == 3:
    print("B")
else:
    print("C")
#tohle bude B


jmeno = "Radim Jedlicka"
print(jmeno.upper())        # "RADIM JEDLICKA"
print(jmeno.split())        # ["Radim", "Jedlicka"]

seznam = [1, 2, 3]
seznam.append(4)
print(seznam)               # [1, 2, 3, 4]
