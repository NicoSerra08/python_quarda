n=int(input("quanti numeri di fibonacci vuoi? --->"))
a, b = 1, 1 #inizializzazione non dichiarazione.

if n>2:
    print(a ,end=" - ")
    print(b, end=" - ")
    for i in range(n-2):
        a,b= a+b,a 
        print(a, end=" - ")
        if i==n-3:
            print("\b\b ") #cancella l'ultimo trattino

elif n==2:
    print(f"{a}", end=" - ")
    print(f"{b}")

elif n==1:
    print(f"{a}")
elif n==0:
    print("nessun numero")
