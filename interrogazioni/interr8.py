
def main():
    frase=input("inserisci una frase: ")
    num=int(input("inserisci un numero: "))

    if len(frase)>num:
        print(frase[:-num]+ "*"*num)

