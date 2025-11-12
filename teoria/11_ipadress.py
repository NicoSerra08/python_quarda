ip = input("inserisci un indirizzo IP ->")

ottetti_str = ip.split(".") ## è un metodo delle stringhe per essere separate, suddivide una stringa col carattere separatore
print(ottetti_str)

ottetti = [] ##lista vuota
for s in ottetti_str:
    int (s)
    ottetti.append(int(s))

print(ottetti)
print(ottetti[0])
print(bin(ottetti[0]))## trasforma in binario con "0b" al inizio



    