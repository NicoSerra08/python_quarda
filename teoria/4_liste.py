
##in python abbiamo le condizioni. tra le colezioni abbiamo:
## LISTE, TUPLE, DIZIONARI, SET.

##-------------------LISTE-----------------------
l = [3, 2.4, "ciao", True]
##per accedere agli elementi vigono le stesse regole di INDICIZZAZIONE delle stringhe
print(l)
print(f"l'ultimo elemento della stringa è: {l[-1]}")
print(f"la stringa senza il primo e l'utimo carattere è {l[1:-1]}")

##agginta di un elemento alla lista
l.append("NUOVO") ##NON RESTITUISCE NULLA, MODIFICA
l.append("nuovo")
l.pop() ##elimina l'ultimo carattere
print(l)

