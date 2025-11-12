

#stringhe

stringa="ciao mondo"
print(stringa)
print(f"l'ultimo carattere della stringa è {stringa[-1]}")


#esempio di slicing delle stringhe
#prende la stringa e stampa solo dal carattere 2 (compreso), al carattere 4 (non compreso)
print(f"la sotto-stringa 2-4 è {stringa[2:4]}")



#concatena 2 stirnghe, però tutte attaccate
nome = "mario"
cognome = "rossi"
x = nome + " " + cognome
print(x)



#ma si può anche fare cosi
nomee, cognomee = "mario", "rossi"
z = nomee + " " + cognomee
print(z)



#concatenazione di una stringa con se stessa
y = (nome +" ")*5
print (y)


