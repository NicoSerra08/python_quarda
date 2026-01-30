#conta_canzoni_per_artista()
def canzoni_per_artista(nome, list):
    list2 = []
    for canzone in list:
        if nome == canzone["artista"]:
            list2.append(canzone)

    return list2

def durata_totale_album(nome, list):
    durata = 0
    for canzone in list:
        if nome == canzone["album"]:
            durata += canzone["durata"]

    return durata

def canzone_piu_ascoltata(list):
    max = 0
    nome = ""
    for canzone in list:
        if canzone["ascolti"] > max:
            max = canzone["ascolti"]
            nome = canzone["titolo"]

    return nome

def media_ascolti_per_artista(nome, list):
    ncanzoni = 0
    somma = 0
    for canzone in list:
        if nome == canzone["artista"]:
            ncanzoni += 1
            somma += canzone["ascolti"]

    return somma / ncanzoni

def top5_canzoni(list):
    pass

def conta_canzoni_per_artista(list, nome):
    cont = 0
    for canzoni in list:
        if nome == canzoni["artista"]:
            cont += 1

    return cont


def main():
    canzoni = [
        {"titolo": "Bohemian Rhapsody", "artista": "Queen", "album": "A Night at the Opera", "durata": 354, "ascolti": 1500000},
        {"titolo": "Don't Stop Me Now", "artista": "Queen", "album": "Jazz", "durata": 209, "ascolti": 980000},
        {"titolo": "Somebody to Love", "artista": "Queen", "album": "A Day at the Races", "durata": 296, "ascolti": 750000},
        {"titolo": "Hotel California", "artista": "Eagles", "album": "Hotel California", "durata": 391, "ascolti": 1200000},
        {"titolo": "Take It Easy", "artista": "Eagles", "album": "Eagles", "durata": 210, "ascolti": 650000},
        {"titolo": "Smells Like Teen Spirit", "artista": "Nirvana", "album": "Nevermind", "durata": 301, "ascolti": 1800000},
        {"titolo": "Come As You Are", "artista": "Nirvana", "album": "Nevermind", "durata": 219, "ascolti": 890000},
        {"titolo": "In Bloom", "artista": "Nirvana", "album": "Nevermind", "durata": 254, "ascolti": 560000},
        {"titolo": "Stairway to Heaven", "artista": "Led Zeppelin", "album": "Led Zeppelin IV", "durata": 482, "ascolti": 2100000},
        {"titolo": "Imagine", "artista": "John Lennon", "album": "Imagine", "durata": 183, "ascolti": 1350000}
    ]

    autore = input("Inserisci il nome dell'artista per cercare le sue canzoni: ")
    print(f"Le canzoni di {autore} sono: ")
    list = canzoni_per_artista(autore, canzoni)
    for canzone in list:
        print(canzone)

    album = input("Inserisci il nome dell'album per il calcolo della durata totale: ")
    print(f"La durata totale è di: {durata_totale_album(album, canzoni)}")

    print(f"La canzone più ascoltata è {canzone_piu_ascoltata(canzoni)}")

    nome_autore = input("Inserisci il nome dell'autore per calcolare la media ascolti: ")
    print(f"La medi ascolti di {nome_autore} è di: {media_ascolti_per_artista(nome_autore, canzoni)}")

    name_autore = input("Inserisci il nome dell'autore per calcolare quante canzoni ha prodotto: ")
    print(f"L'artista {name_autore} ha prodotto {conta_canzoni_per_artista(canzoni, name_autore)} canzoni")

if __name__ == "__main__":
    main()