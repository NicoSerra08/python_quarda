
numeri = [3, 8, 12, 7, 2, 15, 20, 9, 4]
pari = [n for n in numeri if n % 2 == 0]
dispari = [n for n in numeri if n % 2 == 1]
print(f"Numeri pari: {pari}")
print(f"Numeri dispari: {dispari}")