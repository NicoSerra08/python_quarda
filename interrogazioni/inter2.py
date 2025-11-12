##verifica se la frase è palindroma

a = input("inserisci una stringa:")
a = a.lower() ##lo rende tutto piccolo

if a==a[::-1]:
    print("la frase è palindroma")
else:
    print("la frase non è palindroma")
    
