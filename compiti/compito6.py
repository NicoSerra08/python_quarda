##chiede al utente un numero di bit, 
##poi chiede al utente un numero binario (gestiti come stringhe)
##se la lunghezza del numero binario inserito è minore del numero di bit bisogna aggiungere tanti zeri quanti caratteri mancano


bit = input("inserici bit ->")
b = input("inserisci il numero binairo")

if len(b) > bit:
    print(b[0 : bit])

if len(b) < bit:
    print(b[0: ])