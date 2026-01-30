
def main():
    lista_nomi=["ak", "nico", "chri", "solare"]
    lista_voti=[[6,7],[9,8,6],[8,9,2],[3]] ##lista di liste
    ## stampa il voto a fianco di ogni persona
    
    for nome,voto in zip(lista_nomi, lista_voti):
        print(f"{nome} - {voto}")
    ##permette di ciclare in parallelo 2 o più liste
   
if __name__=="__main__":    
    print(__name__)
    main()
 