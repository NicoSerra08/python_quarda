## il py tutto è un oggetto, anche int float sono oggetti
## anche le funaiozni sono oggetti
## creare classi ci permette di creare nuovi oggetti
import turtle
import math
class Punto():
    #costruttore viene chiamato da punto()
    def __init__(self, x, y):##self è come this in java
        #attributi (in python sono tutti pubblici)
        self.x=x
        self.y=y

    def __str__(self):
        ## deve ritornare una stringa
        return (f"({self.x}, {self.y})")
    
    def distanza_originale(self):
        #ritorna la distanza del punto da (0,0)
        return math.sqrt(self.x**2 + self.y**2)
    
    def scambia_coordinate(self):
        return (f"punto inveritito -->({self.y}, {self.x})\n")
    
    def disegna(self):
        turtle.penup()
        turtle.goto(self.x * 10, self.y * 10)  # Moltiplico per vedere meglio
        turtle.pendown()
        turtle.dot(10)  
        turtle.penup()
        turtle.goto(0, 0)
        turtle.hideturtle()


    def distanza(self, altro):
        dx = self.x - altro.x 
        dy = self.y - altro.y
        return (f"la distanza tra i 2 punti è {math.sqrt(dx**2 + dy**2)}\n")
        #restituisce la distanza tra il nostro punto e un istanza di un altro puntp


def main():
    a = Punto(1,2) ##istanza di punto
    b = Punto(3,4) 
    print(f"primo punto -->{a}") 
    print(f"il punto di dista {a.distanza_originale()} dal origine\n")

    print(f"secondo punto -->{a}") 
    print(b.scambia_coordinate())

    print(a.distanza(b))




if __name__=="__main__":
    main()    