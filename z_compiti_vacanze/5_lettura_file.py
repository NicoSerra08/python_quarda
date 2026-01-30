def main():
    file = open("testo.txt", "r")
    righe = file.readlines()
    file.close()
    
    righe_non_vuote = 0
    for riga in righe:
        if riga.strip() != "":
            righe_non_vuote += 1
    
    num_parole = 0
    for riga in righe:
        parole_in_riga = riga.split()
        num_parole += len(parole_in_riga)
    
    caratteri_senza_spazi = 0
    for riga in righe:
        for carattere in riga:
            if carattere != " " and carattere != "\n":
                caratteri_senza_spazi += 1
    
    print(f"Righe: {righe_non_vuote}")
    print(f"Parole: {num_parole}")
    print(f"Caratteri (senza spazi): {caratteri_senza_spazi}")

if __name__ == "__main__":
    main()