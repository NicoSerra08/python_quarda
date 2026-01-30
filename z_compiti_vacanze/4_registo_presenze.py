presenze = {
    "Marco": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15"],
    "Sara": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-16", "2024-01-17"],
    "Luca": ["2024-01-10", "2024-01-11"],
    "Elena": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15", "2024-01-16"]
}

conta = lambda nome: len(presenze.get(nome, []))

top_studente = max(presenze, key=lambda x: len(presenze[x]))

presenti = lambda data: [s for s, d in presenze.items() if data in d]

print("Marco:", conta("Marco"), "presenze")
print("Top studente:", top_studente, "con", conta(top_studente), "presenze")
print("Presenti il 2024-01-12:", presenti("2024-01-12"))