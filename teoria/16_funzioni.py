##MODULARITA'-->suddividere il codice in funzioni
import afunzioni
import random

COSTANTE = 3,14 #costante, avvessibile ovunque ma soltante in lettura


def main():
    #stirnga è una variabile locale
    nome = input("inserisci una parola :")
    print(afunzioni.prima_lettera_maiuscola(nome))

    voti = [random.randint(2, 10) for i in range(10)]
    print(f"\n{voti}")
    m, n = afunzioni.media(voti)
    print(f"MEDIA voti : {m}\nTOTALE voti : {n}")
    if m>6:
        print("😁😜")
    else:
        print("🙈🤬")


if __name__ == "__main__":
    main()