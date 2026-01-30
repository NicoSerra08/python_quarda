def main():
    file=open("file.csv", "r")
    righe = file.readlines()[1::]
    DizionarioMac = {}
    for riga in righe:
        elem = riga.split(",")
        DizionarioMac[elem[0]] = elem[1]

    print(DizionarioMac)
    print("codice elne ")

if __name__ == "__main__":
    main()

    
