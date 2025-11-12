


# in questo programma usimo l'assegnazione  

a="\nciccio bello"
print(a)   #stampa a
print(type(a))    #stampa il tipo di a


parola=input("inserisci una parola :") # qua usuamo l'indicializzazione delle striinghe
print(f"il primo carattere è {parola[0]}")
print(f"l'ultimo carattere è {parola[-1]}")



num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))
num3 = int(input("Inserisci il terzo numero: "))

# calcolo della somma
somma = num1 + num2 + num3

# output del risultato
print(f"\nLa somma di {num1}, {num2}, {num3} è {somma}:")

if somma < 10:
    print("è minore di 10")
else:
    print("è maggiore di 10")


    

