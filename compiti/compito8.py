#stampare la media di ognuno, il numero di voti per ognuno, stampare il voto massimo e quello minimo

def main():
    lista_nomi = ["alice", "mario", "giovanni", "luca"]
    lista_voti = [[6, 10, 5],
                  [6, 7],
                  [8, 10, 9, 9],
                  [5, 8]]
    media = 0

    for nome, voto in zip(lista_nomi, lista_voti):
        print(f"{nome}: {voto}")
        for i in voto:
            media += i

        print(f"Voti presi: {len(voto)}")
        print(f"Media dei voti: {(float)(media / len(voto))}")
        somma = 0
        media = 0
        max = voto[0]
        min = voto[0]

        for i in voto:
            if i > max:
                max = i
            if i < min:
                min = i
            
        print(f"Il voto maggiore è: {max}\nQuello minore è: {min}\n")
        max, min = 0, 0

if __name__ == "__main__": #dunder == __ indica variabili private
    main()