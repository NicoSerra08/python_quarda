##verifica di Serra Nicolò

def temp_media(dati):
    somma = 0
    for citta in dati:
        somma +=citta["temp"]

    media = somma / len(dati)
    return media


def filtra_citta(dati, nome):
    variazioni= []
    for citta in dati:
        if citta["citta"] == nome:
            variazioni.append(citta["temp"])
    return variazioni


def temp_per_citta(dati):
    diz={}
    for citta in dati:
        if citta["citta"]in diz:
            diz[citta["citta"]] = citta["temp"]
        else:
            diz[citta["citta"]] = citta["temp"]

def carica_regioni(nome):
    d = {}
    file = open(nome, "r")
    righe = file.readlines()
    file.close()

    for riga in righe:
        rig = riga.split (";")
        d= [rig[0]] = rig[1][:-1]
    return d

def main():
    dati = [
        {"citta": "minalo", "temp": 12},
        {"citta": "Roma", "temp": 18},
        {"citta": "Milano", "temp": 14},
        {"citta": "Napoli", "temp": 20},
        {"citta": "Roma", "temp": 17},
        {"citta": "Napoli", "temp": 22},
        {"citta": "Milano", "temp": 10}
    ]

    media = temp_media(dati)
    print(f"la media è:{media}")


    citta = input("inserisci la città :")
    print(f"variazione di {citta} = {filtra_citta(dati, citta)}")

    lista_temp_per_citta = temp_per_citta(dati)
    print(f"temp per ogni città: {lista_temp_per_citta}")

    nome_file = "regioni.txt"
    dizionario_regioni = carica_regioni(nome_file)
    print(f"diz città = regione {dizionario_regioni}")



if __name__== "__main__":
    main()    