import turtle

tarta = turtle.Turtle()
tarta.speed(3)


file = open('file.txt', 'r')


for riga in file:
    riga = riga.strip()  
    
    if 'avanti' in riga:
        parti = riga.split()  
        passi = int(parti[1])  
        tarta.forward(passi)
    
    elif 'destra' in riga:
        parti = riga.split()
        gradi = int(parti[1])
        tarta.right(gradi)
    
    elif 'colore' in riga:
        parti = riga.split()
        nome_colore = parti[1]
        
        # Traduzione semplice
        if nome_colore == 'rosso':
            tarta.color('red')
        elif nome_colore == 'verde':
            tarta.color('green')
        elif nome_colore == 'blu':
            tarta.color('blue')
        else:
            tarta.color(nome_colore)
    
    elif 'salta' in riga:
        parti = riga.split()
        x = int(parti[1])
        y = int(parti[2])
        tarta.penup()
        tarta.goto(x, y)
        tarta.pendown()
    
    elif 'cerchio' in riga:
        parti = riga.split()
        raggio = int(parti[1])
        tarta.circle(raggio)

file.close()

turtle.done()