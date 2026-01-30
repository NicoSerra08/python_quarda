testo = open('promessi_sposi.txt', 'r').read()

contatore = {}
totale_lettere = 0

for carattere in testo:
    if carattere.isalpha():
        lettera = carattere.lower()
        totale_lettere += 1
        if lettera in contatore:
            contatore[lettera] += 1
        else:
            contatore[lettera] = 1

percentuali = {}
for lettera in contatore:
    percentuali[lettera] = (contatore[lettera] / totale_lettere) * 100

print("CONTEGGIO LETTERE:")
for lettera in sorted(contatore):
    print(f"{lettera} = {percentuali[lettera]:.2f}% ({contatore[lettera]})")
    

print(f"\ntotale lettere : {totale_lettere}")

## str.isalpha() restituisce True se il carattere è una lettera
## str.lower() converte in minuscolo    