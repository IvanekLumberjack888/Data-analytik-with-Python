cislo = int(input("Zadejte číslo: "))
if cislo % 3 == 0:
    print("Fizz")  # pokud je číslo dělitelné 3, vypiš Fizz
if cislo % 5 == 0:
    print("Buzz")  # pokud je číslo dělitelné 5, vypiš Buzz
if cislo % 3 == 0 and cislo % 5 == 0:
    print("FizzBuzz")  # pokud je číslo dělitelné 3 i 5, vypiš FizzBuzz
if cislo % 3 != 0 and cislo % 5 != 0:
    print(cislo)  # pokud není číslo dělitelné 3 ani 5, vypiš číslo