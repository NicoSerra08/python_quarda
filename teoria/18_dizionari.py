def main():
    #un diizonario python è una sequenza di coppie chiave:valore
    elenco= {"a3-32-b4-ff-f4-32":"luca",
             "65-A0-AA-11-F4-19":"mario"}
    mac = "a3-32-b4-ff-f4-32"
    ## prima parte = chiave
    ## seconda parte = valore 
    if mac in elenco:   
        print(elenco[mac])
    else:
        print("mac non trovato")
    ##la ricerca si può sempre e solo fare sulla chiave


    # aggiungo un nuovo elemento al dionario
    elenco["FF-FF-FF-FF-FF-FF"]="broadcast"

    print(elenco)

if __name__=="__main__":
    main()