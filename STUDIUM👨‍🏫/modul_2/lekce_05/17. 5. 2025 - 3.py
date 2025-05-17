x, y = 0, 1
vysledky = []
delka_rady = 15

# Přidej počáteční hodnoty, pokud je to potřeba
vysledky.append(x)
vysledky.append(y)

while len(vysledky) < delka_rady:
    dalsi_clen = x + y
    vysledky.append(dalsi_clen)
    x, y = y, dalsi_clen  # Posun v posloupnosti

print("Fibonacciho posloupnost:", vysledky)
