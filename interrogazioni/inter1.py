
## data la frase e il numero, se il numero è più piccolo della stringa stampa gli aterischi al posto delle ultime lettere della stringa (numero inserito)
frase=input("inserisci una frase: ")
num=int(input("inserisci un numero: "))

if len(frase)>num:
    print(frase[:-num]+ "*"*num)