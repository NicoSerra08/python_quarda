mac= input ("inserici un mac address")
file = open("interrogazioni/elemento.csv","r")
lines = file.readlines()
n =  len(lines)
for i in lines:
    if mac:
         pipi = lines.split("-")
         print(pipi[2])
        


##porco dio non funziona non so pk, non trova il file.