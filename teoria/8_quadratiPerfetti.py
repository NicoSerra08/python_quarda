##chiede al utente un numero positivo dispari, poi verifica che se si sommano tutti i unmeri dispari si ha un quadrato perfetto

import math ##libreria con funzioni matematiche

a=int(input("inserisci un numero :"))
somma=0

if a >= 1:
    for i in range (1, 2* a +1, 2):
        somma= somma+i 
        print(f"{i}")
else:
    print(f"numero minore di zero") 
       

radiceIntera=math.isqrt(somma)

print(f"la somma dei primi {a} numeri é : {somma}") 
print(f"quadrato perfetto: {radiceIntera**2 == somma}") ## nelle graffe restituisce olo true o false pk è una condizione 
print(f"quadrato perfetto di {radiceIntera}") 
