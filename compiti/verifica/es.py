def controllo_lettere(frase):
    for carattere in frase:
        if not carattere.isalpha():
            return "false"
    return "true"


file = open("file.txt", "r")
righe = file.readlines()  # LEGGI TUTTE LE RIGHE
file.close()

diz = {}
for riga in righe:
    riga = riga.strip()  # RIMUOVE \n e spazi bianchi
    if riga:  # SE LA RIGA NON È VUOTA
        diz[riga] = controllo_lettere(riga)

for chiave, valore in diz.items():
    print(f"'{chiave}': {valore}")