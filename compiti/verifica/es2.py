def analizza_parola(parola):
    vocali = "aeiouAEIOUàèéìòù"
    cont_vocali = 0
    cont_consonanti = 0
    
    for lettera in parola:
        if lettera.isalpha():
            if lettera in vocali:
                cont_vocali += 1
            else:
                cont_consonanti += 1
    
    if cont_vocali == 0 and cont_consonanti == 0:
        return None
    
    if cont_vocali > cont_consonanti:
        tipo = "vocale-dominante"
    elif cont_consonanti > cont_vocali:
        tipo = "consonante-dominante"
    else:
        tipo = "pari"
    
    return {
        "vocali": cont_vocali,
        "consonanti": cont_consonanti,
        "tipo": tipo
    }


# Programma principale
file = open("file.txt", "r", encoding="utf-8")
righe = file.readlines()
file.close()

risultati = {}

for riga in righe:
    parola = riga.strip()
    if parola:  # se non è vuota
        analisi = analizza_parola(parola)
        if analisi:  # se non è None
            risultati[parola] = analisi

# Stampa risultati
print("PAROLA           VOCALI  CONSONANTI  TIPO")
print("-" * 50)

for parola, analisi in risultati.items():
    print(f"{parola:15} {analisi['vocali']:6} {analisi['consonanti']:11} {analisi['tipo']:20}")