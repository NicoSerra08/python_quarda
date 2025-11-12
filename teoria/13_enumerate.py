
def main_0():
    lista=["ak", "nico", "chri", "solare"]
    nome_max = None
    len_max = 0
    for nome in lista:
        if len(nome)>len_max:
            nome_max = nome
            len_max = len(nome)
    print(nome_max)

def main():
    lista=["ak", "nico", "chri", "solare"]
    
    for i, nome in enumerate(lista):
        print(f"{i} - {nome}")

   
if __name__=="__main__":     #__ si chiama dunder (doubkle underscore):
    print(__name__)
    main()
