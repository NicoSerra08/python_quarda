
##selezione

if 1==2:
    ##in python i blocchi di codice si fanno con le indentazioni (fatta con 4 spazi, oppure con un tab)
    print("vero!")
else:
    print("falso!")

print("\n\n")

print("premi A per inserire.")
print("premi B per modificare.")
print("premi C per cancellare.")

tasto=input("->")
tasto=tasto.upper()##trasforma qualsiasi carattere inserito dal utente in MAIUSCOLO
## tasto= tasto.lower()----stessa cosa ma in minuscolo

if tasto == "A":
    print("l'utente vuole inserire")
elif tasto =="B":
    print("l'utente vuole modificare")
elif tasto =="C":
    print("l'utente vuole cancellare")
else:
    print("tasto non valido")