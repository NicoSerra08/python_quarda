##classe quadrato(lato, x, y, colore)
##metodi: perimetro, area, disegna
## programma che disegna 100 quadrati casuali nela finsetra, casuale in tutto (lato, colore, posizione)


import turtle
import random
class Quadrato():
    # Costruttore
    def __init__(self, lato, x, y, colore):
        self.lato = lato
        self.x = x
        self.y = y
        self.colore = colore
    
    def __str__(self):
        return f"Quadrato [lato={self.lato}, pos=({self.x},{self.y}), colore={self.colore}]"
    
    def perimetro(self):
        return 4 * self.lato
    
    def area(self):
        return self.lato ** 2
    
    def disegna(self):
        # Disegna il quadrato nella posizione specificata
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        
        # Imposta il colore
        turtle.fillcolor(self.colore)
        turtle.pencolor(self.colore)
        
        # Disegna il quadrato riempito
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.lato)
            turtle.left(90)
        turtle.end_fill()
        
        turtle.penup()


    def genera_colore_casuale():
        r = random.random()
        g = random.random()
        b = random.random()
        return (r, g, b)


    def main():
        # Configurazione finestra
        turtle.setup(800, 600)
        turtle.speed(0)  # Velocità massima
        turtle.hideturtle()
        turtle.colormode(1.0)  # Modalità RGB con valori 0-1
        
    
        
        # Disegna 100 quadrati casuali
        print("=== disegno 100 qua ===")
        for i in range(100):
            # Genera parametri casuali
            lato = random.randint(10, 60)  # Lato tra 10 e 60
            x = random.randint(-350, 350)  # Posizione x
            y = random.randint(-250, 250)  # Posizione y
            colore = genera_colore_casuale()  # Colore RGB casuale
            
            # Crea e disegna il quadrato
            quadrato = Quadrato(lato, x, y, colore)
            quadrato.disegna()
            
            # Stampa info ogni 20 quadrati
            if (i + 1) % 20 == 0:
                print(f"Disegnati {i + 1} quadrati...")
        
        print("\n✓ Completato! 100 quadrati disegnati.")
        print("Clicca sulla finestra per chiudere.")
        
        # Mantieni la finestra aperta
        turtle.done()


    if __name__ == "__main__":
        main()