
def main():
    MAC = input("Inserisci un MAC address -> ")
    
    file = open("mac-vendors-export.csv", "r", encoding = 'utf-8')
    file.readline()
    for riga in file:
        if riga.split(",")[0] == MAC:
            print(riga.split(",")[1])
            file.close()
            return
    
    file.close()
    print(f"MAC {MAC} non trovato.")

if __name__ == "__main__":
    main()
    
##_____________----------_____________-----------____________-----------

def main():
    mac = input("inserisci il MAC addres :")
    file= open("mac-vendors-export.csv", "r") ##oggetto file
    file.readlines()##lista di stringhe che contiene le righe

    for riga in file:
        if riga.split(",")[0].upper() == mac:
            print(riga)
            file.close()
            return        
        
    file.close()
    print(f"mac: {mac} non trovato")
    
   
if __name__=="__main__":   
    print(__name__)
    main()

