##l'utente inserisce in imput una password, il programma stampa la password oscurata da asterischi

password = input("\nInserisci la tua password: ") 
x = ("*" * len(password))
print(f"\nhai inserito la pasword: {x}")

###stampa la password con il primo carattere visibile
y = len(password) -1
x = ("*" * y)
print(f"hai inserito la pasword: {password[0:1]}{x}")

###stampa la password con il primo e l'ultimo carattere visibile
y = len(password) -2
x = ("*" * y)
print(f"hai inserito la pasword: {password[0:1]}{x}{password[-1]}")









