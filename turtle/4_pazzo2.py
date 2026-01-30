import turtle
import random
import time
import math

# Setup della finestra
screen = turtle.Screen()
screen.setup(width=1000, height=800)
screen.title("🐢 ULTIMATE TURTLE SHOW 🚀")
screen.bgcolor("black")
screen.tracer(0)  # Disabilita animazione automatica

def rainbow_color(angle):
    """Genera colore arcobaleno"""
    r = int(127 * (math.sin(angle) + 1))
    g = int(127 * (math.sin(angle + 2) + 1))
    b = int(127 * (math.sin(angle + 4) + 1))
    return (r, g, b)

def effetto_stelle_cadenti():
    """Stelle cadenti con trail"""
    screen.bgcolor("darkblue")
    screen.colormode(255)
    
    stelle = []
    for _ in range(20):
        t = turtle.Turtle()
        t.speed(0)
        t.shape("circle")
        t.shapesize(random.uniform(0.1, 0.5))
        t.color("yellow")
        t.penup()
        
        x = random.randint(-450, 450)
        y = random.randint(300, 400)
        t.goto(x, y)
        
        dx = random.uniform(-1, 1)
        dy = random.uniform(-3, -2)
        stelle.append((t, dx, dy))
    
    for _ in range(50):
        for stella, dx, dy in stelle:
            x, y = stella.position()
            stella.goto(x + dx, y + dy)
            
            # Aggiunge trail
            if random.random() < 0.3:
                trail = turtle.Turtle()
                trail.speed(0)
                trail.shape("circle")
                trail.shapesize(0.05)
                trail.color("white")
                trail.penup()
                trail.goto(x, y)
                screen.update()
        
        screen.update()
        time.sleep(0.05)
    
    for stella, _, _ in stelle:
        stella.hideturtle()

def spirale_ipnotica():
    """Spirale colorata che ruota"""
    screen.bgcolor("black")
    screen.colormode(255)
    
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    for i in range(200):
        col = rainbow_color(i/20)
        t.pencolor(col)
        t.forward(i * 1.5)
        t.right(91)
        screen.update()
    
    t.hideturtle()

def esplosione_fuochi():
    """Fuochi d'artificio colorati"""
    screen.bgcolor("black")
    screen.colormode(255)
    
    colors = ["red", "yellow", "blue", "green", "purple", "orange"]
    
    for esplosione in range(10):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        
        for _ in range(30):
            t = turtle.Turtle()
            t.speed(0)
            t.hideturtle()
            t.penup()
            t.goto(x, y)
            
            col = random.choice(colors)
            t.color(col)
            
            angolo = random.random() * 6.28
            distanza = random.randint(20, 100)
            
            t.pendown()
            t.goto(x + distanza * math.cos(angolo), 
                   y + distanza * math.sin(angolo))
            
            screen.update()
            time.sleep(0.01)
            
            t.clear()
            t.hideturtle()

def disegna_fiore():
    """Fiore complesso con petali"""
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    
    # Petali colorati
    colors = ["#FF6B9D", "#FF8E53", "#FFDD59", "#A3E4D7", "#6A5ACD"]
    
    for petalo in range(36):
        t.color(random.choice(colors))
        t.begin_fill()
        t.circle(100, 60)
        t.left(120)
        t.circle(100, 60)
        t.end_fill()
        t.left(10)
        screen.update()
    
    # Centro del fiore
    t.penup()
    t.goto(0, -40)
    t.color("yellow")
    t.pendown()
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    
    screen.update()
    t.hideturtle()

def effetto_arcobaleno():
    """Arcobaleno rotante"""
    screen.bgcolor("black")
    screen.colormode(255)
    
    t = turtle.Turtle()
    t.speed(0)
    t.width(3)
    
    for i in range(180):
        col = rainbow_color(i/30)
        t.pencolor(col)
        t.forward(i)
        t.right(59)
        screen.update()
    
    t.hideturtle()

def cerchi_concentrici():
    """Cerchi concentrici pulsanti"""
    screen.bgcolor("black")
    screen.colormode(255)
    
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    
    for frame in range(50):
        t.clear()
        
        for i in range(10):
            raggio = 20 + i * 20 + 10 * math.sin(frame/5 + i)
            col = rainbow_color(frame/20 + i/10)
            
            t.penup()
            t.goto(0, -raggio)
            t.pencolor(col)
            t.pendown()
            t.circle(raggio)
        
        screen.update()
        time.sleep(0.05)
    
    t.hideturtle()

def big_bang_finale():
    """Effetto finale spettacolare"""
    screen.bgcolor("black")
    screen.colormode(255)
    
    # Punto iniziale
    centro = turtle.Turtle()
    centro.shape("circle")
    centro.color("white")
    centro.shapesize(0.1)
    centro.penup()
    
    # Espansione
    for size in range(1, 150, 3):
        centro.shapesize(size/50)
        col = rainbow_color(size/50)
        centro.color(col)
        
        # Cerchi di espansione
        if size % 10 == 0:
            onda = turtle.Turtle()
            onda.hideturtle()
            onda.penup()
            onda.goto(0, -size*3)
            onda.pencolor("cyan")
            onda.pendown()
            onda.circle(size*3)
            screen.update()
        
        screen.update()
        time.sleep(0.03)
    
    # Messaggio finale
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.penup()
    msg.goto(0, -100)
    msg.color("#FFD700")
    
    # Scrittura progressiva
    testo = "PYTHON È MAGIA!"
    display = ""
    for lettera in testo:
        display += lettera
        msg.clear()
        msg.write(display, align="center", font=("Arial", 48, "bold"))
        screen.update()
        time.sleep(0.1)
    
    time.sleep(2)

def mostra_messaggio(testo, y=0, size=24, col="white"):
    """Mostra un messaggio a schermo"""
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, y)
    t.color(col)
    t.write(testo, align="center", font=("Arial", size, "bold"))
    screen.update()
    return t

def main():
    """Programma principale"""
    print("\n" + "="*50)
    print("   🚀 INIZIO SHOW TURTLE ULTIMATE!   ")
    print("="*50 + "\n")
    
    time.sleep(2)
    
    # Sequenza di effetti
    effetti = [
        ("1. STELLE CADENTI", effetto_stelle_cadenti),
        ("2. SPIRALE IPNOTICA", spirale_ipnotica),
        ("3. FIORE MAGICO", disegna_fiore),
        ("4. FUOCHI D'ARTIFICIO", esplosione_fuochi),
        ("5. ARCABALENO ROTANTE", effetto_arcobaleno),
        ("6. CERCHI PULSANTI", cerchi_concentrici),
        ("7. BIG BANG FINALE", big_bang_finale)
    ]
    
    for nome, effetto in effetti:
        print(f"\n▶ {nome}")
        
        # Pulisci schermo
        screen.clear()
        screen.bgcolor("black")
        screen.tracer(0)
        
        # Mostra nome effetto
        mostra_messaggio(nome, 300, 20, "cyan")
        time.sleep(1)
        
        # Esegui effetto
        effetto()
        
        time.sleep(1)
    
    # Messaggio finale
    screen.clear()
    screen.bgcolor("black")
    mostra_messaggio("SHOW COMPLETATO!", 50, 36, "gold")
    mostra_messaggio("I tuoi amici sono a bocca aperta! 😲", -50, 24, "white")
    
    print("\n" + "="*50)
    print("   🎉 SHOW COMPLETATO CON SUCCESSO!   ")
    print("="*50)
    print("\nChiudi la finestra per uscire...")
    
    turtle.mainloop()

# Esegui il programma
if __name__ == "__main__":
    main()