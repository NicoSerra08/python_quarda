##chiede al utente un numero positivo, poi stampa tutti i quadrati dei numeri precedenti di quello

a=int(input("inserisci un numero :"))

if a >= 0:
    for i in range (0, a+1, 1):
        print(f"il quadrato di {i} è {i*i}")

else:
    print("numero negativo rilancia il programma")