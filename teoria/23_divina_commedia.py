
file = open('promessi_sposi.txt', 'r')
testo = file.read()
file.close()

parole = testo.split()
totale = len(parole)

# 3. Troviamo le 5 parole più lunghe
parole.sort(key=len, reverse=True)  # Ordina dalla più lunga alla più corta
parole_lunghe = parole[:5]  # Prende le prime 5

conteggio = {}
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

for lettera in alfabeto:
    conteggio[lettera] = 0

for parola in parole:
    if parola:  # Se non è vuota
        prima_lettera = parola[0].lower()
        if prima_lettera in conteggio:
            conteggio[prima_lettera] += 1

print("ANALISI DEL TESTO:")
print(f"Totale parole: {totale}\n")

print("Le 5 parole più lunghe:")
for i, parola in enumerate(parole_lunghe, 1):
    print(f"{i}. {parola} ({len(parola)} lettere)")

print("\nParole per lettera iniziale:")
for lettera in alfabeto:
    if conteggio[lettera] > 0:
        print(f"{lettera.upper()}: {conteggio[lettera]}")
        