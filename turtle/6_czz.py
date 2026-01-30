import turtle
import time

def main(): 

    screen = turtle.Screen()
    screen.bgcolor("black")
    turtle.color("pink")
    turtle.speed(7)

    turtle.pensize(15)

    turtle.right(90)
    turtle.penup()
    turtle.goto(100,-100)
    turtle.pendown()
    turtle.circle(50)

    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.circle(50)

    turtle.pensize(6)
    turtle.right(180)

    turtle.penup()
    turtle.goto(50,-50)
    turtle.pendown()
    turtle.forward(200)

    turtle.penup()
    turtle.goto(150,-50)
    turtle.pendown()
    turtle.forward(200)

    turtle.pensize(15)

    turtle.circle(50, 180)
    turtle.left(90)
    turtle.forward(100)

    turtle.pensize(4)

    turtle.penup()
    turtle.goto(100, 200)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(20)

    ##prima vena a sinistra
    turtle.color("red")

    turtle.penup()
    turtle.goto(50, 100)
    turtle.pendown()
    turtle.left(50)
    turtle.forward(25)
    turtle.right(40)
    turtle.forward(15)
    turtle.left(20)
    turtle.forward(20)

    ##prima vena a destra
    turtle.penup()
    turtle.goto(150, 115)
    turtle.pendown()
    turtle.right(80)
    turtle.forward(25)
    turtle.left(40)
    turtle.forward(20)
    turtle.right(20)
    turtle.forward(15)


    ##seconda vena a sinistra
    turtle.penup()
    turtle.goto(50, 30)
    turtle.pendown()
    turtle.left(100)
    turtle.forward(25)
    turtle.right(40)
    turtle.forward(15)
    turtle.left(20)
    turtle.forward(25)

    ##seconda vena a destra
    turtle.penup()
    turtle.goto(150, 50)
    turtle.pendown()
    turtle.right(100)
    turtle.forward(20)
    turtle.left(40)
    turtle.forward(20)
    turtle.right(20)
    turtle.forward(20)

    ##sborra
    turtle.color("light blue")
    turtle.pensize(10)


    turtle.penup()
    turtle.goto(100, 220)
    turtle.pendown()
    turtle.right(110)
    turtle.forward(25)

    turtle.penup()
    turtle.goto(120, 250)
    turtle.pendown()
    turtle.right(80)
    turtle.forward(25)


    turtle.penup()
    turtle.goto(80, 280)
    turtle.pendown()
    turtle.right(100)
    turtle.forward(25)


    turtle.mainloop()

if __name__ == "__main__":
    main()