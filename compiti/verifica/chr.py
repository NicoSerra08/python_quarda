#Cercare i giochi di un genere specifico
#Visualizzare il gioco con il punteggio più alto
#Calcolare la media dei punteggi
#Trovare i giochi usciti dopo un certo anno
def cercaGiochiGenere(genere, diz):
    for videogioco in diz:
        if genere == videogioco["genere"]:
            return videogioco
        else:
            return None
        
def punteggioPiuAlto(diz):
    max = 0
    for videogioco in diz:
        if videogioco["punteggio"] > max:
            return videogioco

def mediaPunteggi(diz):
    somma = 0
    for videogioco in diz:
        somma += videogioco["punteggio"]

    return somma / len(diz)    

def uscitaDopoUnCertoAnno(diz, anno):
    diz2 = []
    for videogioco in diz:
        if videogioco["anno"] > anno:
            diz2.append(videogioco)

    return diz2


def main():
    videogiochi = [
        {"titolo": "The Legend of Zelda", "genere": "Avventura", "anno": 2017, "punteggio": 9.7},
        {"titolo": "Super Mario Odyssey", "genere": "Platform", "anno": 2017, "punteggio": 9.6},
        {"titolo": "Elden Ring", "genere": "RPG", "anno": 2022, "punteggio": 9.5},
        {"titolo": "Portal 2", "genere": "Puzzle", "anno": 2011, "punteggio": 9.5},
        {"titolo": "Minecraft", "genere": "Sandbox", "anno": 2011, "punteggio": 9.0}
    ]

    var = 0

    while var == 0:
        scelta = int(input("Cosa vorresti fare:\n1) Cercare i giochi di un genere specifico\n2) Visualizzare il gioco con il punteggio più alto\n3) Calcolare la media dei punteggi\n4) Trovare i giochi usciti dopo un certo anno\n0 per uscire\nScelta: "))

        if scelta == 1:
            genere = input("Inserisci il genere per trovare i giochi di quel tipo: ")
            trovato = cercaGiochiGenere(genere, videogiochi)
            if trovato == None:
                print(f"Genere {genere} non presente")
            else:
                print(f"Videogioco trovato: {trovato}")

        if scelta == 2:
            punteggio = punteggioPiuAlto(videogiochi)
            print(f"Il videogioco con il punteggio più alto è: {punteggio}")

        if scelta == 3:
            media = mediaPunteggi(videogiochi)
            print(f"La media dei punteggi dei vari giochi è: {media}")

        if scelta == 4:
            anno = int(input("Inserisci un anno per vedere i giochi usciti dopo di esso: "))
            videogiochi_anno = uscitaDopoUnCertoAnno(videogiochi, anno)
            if videogiochi_anno == []:
                print("Non ci sono giochi presenti usciti dopo quell'anno")
            else:
                print(f"I videogiochi usciti dopo il {anno} sono:")
                for videogioco in videogiochi_anno:
                    print(videogioco)

        if scelta == var:
            var += 1

if __name__ == "__main__":
    main()