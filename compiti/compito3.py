##crea un programa in py che chiede al utente un numero intero, e stampa il numero per 2, per 3, per 5 ,usare l'operatore % per il resto della diviisone

n=int(input("inserisci un numero intero: "))

n22=n//2
n33=n//3
n55=n//5
n2= n%2
n3= n%3
n5= n%5

print(f"{n} / 2 = {n22}, con resto {n2}")
print(f"{n} / 3 = {n33}, con resto {n3}")
print(f"{n} / 5 = {n55}, con resto {n5}")