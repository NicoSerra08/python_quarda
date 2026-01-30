##simulare n partite di pari e disari
# imput: 
# -n di partite
# -nome 1 giocatore
# -nome 2 giocatore
# -per simulare le partire usare un dizionario
# -chiave:i nomi
# -lista con le varie giocate
#le singole partite sono generate con random.randit

import random

def main():
    print("ES PARI E DISPARI")
    print("-" * 30)

    n_partite = int(input("Quante partite vuoi giocare? "))

    nome1 = input("Nome primo giocatore (Pari): ")
    nome2 = input("Nome secondo giocatore (Dispari): ")

    giocate = {
        nome1: [],
        nome2: []
    }

    # Conta le vittorie
    vittorie = {nome1: 0, nome2: 0}

    # Simula le partite
    print("\n" + "-" * 30)
    print("INIZIO PARTITE")

    for partita in range(1, n_partite + 1):
        print(f"\nPartita {partita}:")
        
        num1 = random.randint(0, 5)
        num2 = random.randint(0, 5)
        
        giocate[nome1].append(num1)
        giocate[nome2].append(num2)
        
        somma = num1 + num2
        
        print(f"{nome1}: {num1}")
        print(f"{nome2}: {num2}")
        print(f"Somma: {somma}")
        
        if somma % 2 == 0:  
            print(f"Vince {nome1} (PARI)")
            vittorie[nome1] += 1
        else:  
            print(f"Vince {nome2} (DISPARI)")
            vittorie[nome2] += 1

    print("\n" + "-" * 30)
    print("RISULTATI FINALI")

    print(f"\nGiocate di {nome1}: {giocate[nome1]}")
    print(f"Giocate di {nome2}: {giocate[nome2]}")

    print(f"\nVittorie:")
    print(f"{nome1}: {vittorie[nome1]}")
    print(f"{nome2}: {vittorie[nome2]}")

    # Vincitore finale
    if vittorie[nome1] > vittorie[nome2]:
        print(f"{nome1.upper()} --> sei un grande, hai sconfitto {nome2}")
    elif vittorie[nome2] > vittorie[nome1]:
        print(f"{nome2.upper()} --> sei un grande, hai sconfitto {nome1}")
    else:
        print("mi spiace ma avete pareggiato")


if __name__ == "__main__":
    main()