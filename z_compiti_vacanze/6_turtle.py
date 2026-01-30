import turtle

def main():
    p = int(input("Inserire il numero di lati: "))
    lunghezza = int(input("Inserire la lunghezza del poligono(100+): "))
    s = 360 / p
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()

    for i in range(p):
        turtle.speed(2)
        turtle.color("blue")
        turtle.pensize(3)
        turtle.forward(lunghezza)
        turtle.left(s)
    
    turtle.penup()
    turtle.goto(40, -10)
    turtle.write(f"poligono a {p} lati", align="center", font=("Arial", 20))
    
    turtle.mainloop()

if __name__ == "__main__":
    main()