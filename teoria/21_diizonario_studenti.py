def leggi_registro(nome_file):
    registro = {}
    file = open(nome_file, 'r')
    for riga in file:
        riga = riga.strip()
        if riga:
            parti = riga.split(';')
            nome = parti[0]
            voti = []
            for i in range(1, len(parti)):
                voti.append(int(parti[i]))
            registro[nome] = voti
        print(riga)    
    
    file.close()
    return registro




def calcola_media(voti):
    if len(voti) == 0:
        return 0
    somma = 0
    for voto in voti:
        somma += voto
    return somma / len(voti)



def classifica(registro):
    "Crea la classifica ordinata per media"
    lista_medie = []
    
    for nome, voti in registro.items():
        media = calcola_media(voti)
        lista_medie.append((nome, media))
    
    # Ordina dalla media più alta alla più bassa
    for i in range(len(lista_medie)):
        for j in range(i + 1, len(lista_medie)):
            if lista_medie[j][1] > lista_medie[i][1]:
                # Scambia le posizioni
                temp = lista_medie[i]
                lista_medie[i] = lista_medie[j]
                lista_medie[j] = temp
    
    return lista_medie




def stampa_podio(classifica):
    "Stampa i primi 3"
    print("\n---podio---")
    for i in range(3):
        nome = classifica[i][0]
        media = classifica[i][1]
        print(f"{i+1}° posto: {nome} - Media: {media:.2f}")



def trova_insufficienti(classifica):
    "Trova chi ha media sotto il 6"
    insufficienti = []
    for studente in classifica:
        nome = studente[0]
        media = studente[1]
        if media < 6:
            insufficienti.append(studente)
    return insufficienti




print("\nANALISI VOTI CLASSE")
registro = leggi_registro("registro.txt")

classifica_completa = classifica(registro)

print("\n---tutti gli studenti---")
for studente in classifica_completa:
    print(f"{studente[0]}: {studente[1]:.2f}")

stampa_podio(classifica_completa)

insufficienti = trova_insufficienti(classifica_completa)
if insufficienti:
    print("\n---studenti in difficoltà---")
    for studente in insufficienti:
        print(f"{studente[0]}: {studente[1]:.2f}")
else:
    print("\nNessuno studente sfigato")