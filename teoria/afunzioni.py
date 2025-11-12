
def prima_lettera_maiuscola(stringa):
    '''
    la funzione restituisce la sctringa con la lettera iniziale maiuscola
    '''
    stringa=stringa[0].upper() + stringa[1:].lower()
    return stringa


def media(lista):
    '''
    la funzione restituisce la media dei. valori presenti il lista e il numero di elementi
    '''
    somma = 0.
    for val in lista:
        somma = somma +val
    
    n_lista = len(lista)



    return somma/n_lista, n_lista

