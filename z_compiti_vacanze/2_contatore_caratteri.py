def main():
    testo = "nnniiicccooossseeerrraaa "
    conteggio = {}
    for carattere in testo:
        if carattere in conteggio:
            conteggio[carattere] += 1
        else:
            conteggio[carattere] = 1
    print("Conteggio caratteri:")
    for carattere, numero in conteggio.items():
        print(f"  '{carattere}': {numero}")


if __name__ == "__main__":
    main()
