
##Dato un dizionario che associa nomi di studenti ai loro voti (un voto per studente),
##trovare quale voto compare più spesso.
def main():
    studenti_voti = {
    "Marco": 7,
    "Sara": 8,
    "Luca": 6,
    "Elena": 8,
    "Paolo": 7,
    "Giulia": 8,
    "Andrea": 6,
    "Chiara": 7
    }

    diz_contatori = {}

    for studenti in studenti_voti:
        voto = studenti_voti[studenti] #così accedo al valore

        # print(voto)   stampa tutti i VALORI(voti), non le chiavi(nomi)

        if voto in diz_contatori:
            diz_contatori[voto] += 1
        else:
            diz_contatori[voto] = 1
    
    voto_più_frequente = 6
    frequenza_max = 2
    for voto in diz_contatori:
        if diz_contatori[voto] > frequenza_max:
            frequenza_max = diz_contatori[voto]
            voto_più_frequente = voto

    print(f"il voto più frequente:{voto_più_frequente}\n capitato:{frequenza_max}")

if __name__ == "__main__":
    main()        