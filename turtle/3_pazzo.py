import turtle
import random
import time
import math

def disegna_fuochi_artifici():
    """Crea un effetto fuochi d'artificio"""
    colors = ["red", "yellow", "blue", "green", "purple", "orange", "pink", "cyan"]
    
    for _ in range(30):
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        t.penup()
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        t.goto(x, y)
        
        color = random.choice(colors)
        t.color(color)
        
        # Esplosione di cerchi
        for size in range(1, 25, 2):
            t.pendown()
            t.circle(size)
            t.penup()
            t.right(10)
        
        t.clear()

def effetto_spirale_multicolore():
    """Crea spirali colorate ipnotiche"""
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    for i in range(200):
        t.color(colors[i % len(colors)])
        t.forward(i * 2)
        t.right(91)
    
    t.hideturtle()

def disegna_fiore():
    """Disegna un fiore complesso"""
    t = turtle.Turtle()
    t.speed(0)
    
    # Petali
    colors = ["#FF6B9D", "#FF8E53", "#FFDD59", "#A3E4D7", "#6A5ACD"]
    
    for petalo in range(36):
        t.color(random.choice(colors))
        t.begin_fill()
        for _ in range(2):
            t.circle(100, 60)
            t.left(120)
        t.end_fill()
        t.right(10)
    
    # Centro del fiore
    t.penup()
    t.goto(0, -40)
    t.color("yellow")
    t.pendown()
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    
    t.hideturtle()

def effetto_stelle_cadenti():
    """Crea stelle cadenti animato"""
    screen = turtle.Screen()
    screen.bgcolor("darkblue")
    
    stars = []
    colors = ["white", "yellow", "lightblue", "silver"]
    
    for _ in range(15):
        star = turtle.Turtle()
        star.speed(0)
        star.shape("circle")
        star.color(random.choice(colors))
        star.shapesize(random.uniform(0.1, 0.5))
        star.penup()
        
        x = random.randint(-400, 400)
        y = random.randint(300, 400)
        star.goto(x, y)
        
        dx = random.uniform(-2, 2)
        dy = random.uniform(-3, -1)
        
        stars.append((star, dx, dy))
    
    for _ in range(50):
        for star, dx, dy in stars:
            x, y = star.position()
            star.goto(x + dx, y + dy)
        
        turtle.update()
        time.sleep(0.05)
    
    for star, _, _ in stars:
        star.clear()
        star.hideturtle()

def disegna_mandala():
    """Disegna un mandala ipnotico"""
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    # Cerchi concentrici colorati
    colors = ["#FF5252", "#FF4081", "#E040FB", "#7C4DFF", 
              "#536DFE", "#448AFF", "#40C4FF", "#18FFFF",
              "#64FFDA", "#69F0AE", "#B2FF59", "#EEFF41"]
    
    for i in range(12):
        t.color(colors[i])
        t.penup()
        t.goto(0, -20 * (i + 1))
        t.pendown()
        t.circle(20 * (i + 1))
        t.penup()
    
    # Disegno geometrico interno
    t.goto(0, 0)
    t.pendown()
    
    for i in range(72):
        t.color(colors[i % len(colors)])
        t.forward(200)
        t.backward(200)
        t.right(5)
    
    t.hideturtle()

def effetto_arcobaleno():
    """Crea un effetto arcobaleno che si espande"""
    t = turtle.Turtle()
    t.speed(0)
    t.width(3)
    
    colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
    
    for i in range(180):
        t.color(colors[i % len(colors)])
        t.forward(i)
        t.right(59)
    
    t.hideturtle()

def main():
    """Programma principale - SHOW TURTLE!"""
    print("=" * 50)
    print("   🎨 SHOW TURTLE - LO SPETTACOLO GRAFICO!   ")
    print("=" * 50)
    print("\nPreparati per uno show mozzafiato!")
    print("Chiudi la finestra tra un effetto e l'altro...")
    time.sleep(2)
    
    # Setup iniziale
    screen = turtle.Screen()
    screen.title("🐢 SHOW TURTLE - by Python Master 🎯")
    screen.bgcolor("black")
    
    # 1. MANDALA IPNOTICO
    print("\n🎯 EFFETTO 1: Mandala Ipnottrico")
    disegna_mandala()
    time.sleep(3)
    screen.clear()
    screen.bgcolor("white")
    
    # 2. FIORE COMPLESSO
    print("🌸 EFFETTO 2: Fiore Magico")
    disegna_fiore()
    time.sleep(3)
    screen.clear()
    screen.bgcolor("darkblue")
    
    # 3. STELLE CADENTI
    print("⭐ EFFETTO 3: Stelle Cadenti")
    effetto_stelle_cadenti()
    time.sleep(1)
    screen.clear()
    screen.bgcolor("black")
    
    # 4. SPIRALE MULTICOLORE
    print("🌀 EFFETTO 4: Spirale Ipnottrica")
    effetto_spirale_multicolore()
    time.sleep(2)
    screen.clear()
    screen.bgcolor("lightgray")
    
    # 5. ARCABALENO
    print("🌈 EFFETTO 5: Arcobaleno Rotante")
    effetto_arcobaleno()
    time.sleep(2)
    screen.clear()
    screen.bgcolor("black")
    
    # 6. FUOCHI D'ARTIFICIO FINALE
    print("🎆 EFFETTO FINALE: Fuochi d'Artificio!")
    for _ in range(5):
        disegna_fuochi_artifici()
        time.sleep(0.5)
    
    # Messaggio finale
    screen.clear()
    screen.bgcolor("black")
    
    final_t = turtle.Turtle()
    final_t.speed(1)
    final_t.color("gold")
    final_t.penup()
    final_t.goto(0, 100)
    
    final_t.write("SHOW COMPLETATO!", align="center", 
                  font=("Arial", 30, "bold"))
    
    final_t.goto(0, 50)
    final_t.color("white")
    final_t.write("Python Turtle Graphics", align="center", 
                  font=("Courier", 20, "italic"))
    
    final_t.goto(0, -50)
    final_t.color("cyan")
    final_t.write("I tuoi amici saranno a bocca aperta! 😲", 
                  align="center", font=("Arial", 18))
    
    print("\n" + "=" * 50)
    print("   🎉 SHOW COMPLETATO CON SUCCESSO!   ")
    print("=" * 50)
    
    turtle.mainloop()

if __name__ == "__main__":
    main()