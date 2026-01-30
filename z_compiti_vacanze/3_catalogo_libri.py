libri = [
    {"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
    {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
    {"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},
    {"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
    {"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
]

def libri_di_autore(autore):
    return [libro for libro in libri if libro["autore"] == autore]

def prezzo_medio():
    prezzi = [libro["prezzo"] for libro in libri]
    return sum(prezzi) / len(prezzi) if prezzi else 0 ##sum = somma di tutti

def libro_piu_recente():
    return max(libri, key=lambda libro: libro["anno"])

while True:
    print("\n" + "-"*40)
    print("CATALOGO LIBRI")
    print("="*40)
    print("1. Cercare libri di un autore")
    print("2. Calcolare il prezzo medio")
    print("3. Trovare il libro più recente")
    print("-"*40)
    
    scelta = input("Scegli cosa fare: ")
    
    if scelta == "1":
        autore = input("Inserisci il nome dell'autore: ")
        risultati = libri_di_autore(autore)
        if risultati:
            print(f"\nLibri di {autore}:")
            for libro in risultati:
                print(f"  - {libro['titolo']} ({libro['anno']}), {libro['prezzo']}€")
        else:
            print(f"\nNessun libro trovato per {autore}")
            
    elif scelta == "2":
        media = prezzo_medio()
        print(f"\nIl prezzo medio dei libri è: {media:.2f}€")
        
    elif scelta == "3":
        recente = libro_piu_recente()
        print(f"\nLibro più recente:")
        print(f"  - {recente['titolo']} di {recente['autore']}")
        print(f"    Anno: {recente['anno']}, Prezzo: {recente['prezzo']}€")
        
        
    else:
        print("Scelta non valida!")
