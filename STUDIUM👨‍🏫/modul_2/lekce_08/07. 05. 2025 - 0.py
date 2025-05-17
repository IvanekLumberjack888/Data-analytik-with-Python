from ast import arg

def vytvor_osobu(jmeno: str, prijmeni: str, bydliste: str) -> dict:
    return{
        "jmeno": jmeno,
        "prijmeni": prijmeni,
        "bydliste": bydliste
    }
vytvor_osobu("Ivo", "Doležal", "Brno")
print(vytvor_osobu)

def math_operation(operation, *numbers, multiplier):
    if operation == "sum":
        return sum(numbers)
    elif operation == "max":
        return max(numbers)
    elif operation == "average":
        return arg()
print(math_operation("sum", 1, 2, 3, 4, 5, 44, 6, multiplier=2))

def pozdrav(*jmena, pocet_pozdravu: int = 5) -> str:  
    vystup = ""
    for jmeno in jmena:
        vystup = vystup + "\n"+ f"Tys {jmeno}? Ahoj{(pocet_pozdravu - 1) * ', ahoj'}."
    return vystup

print(pozdrav("Petr", "Pavel", "Jirka", pocet_pozdravu=2))

def vytvor_slovnik(kwargs):
    #Vypis slovnik, ktery obsahuje libovolne mnozstvi sbalenych hodnot.
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key.upper(), value, sep=":")

# ctrl + shift + sipka
duplikace řádků
# alt + sipka