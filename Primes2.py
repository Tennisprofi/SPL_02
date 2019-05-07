""" primzahlen - Python 3.3.4
    Berechnet alle Primzahlen im Intervall [2 - obere Grenze] """
 
def eingabe (a):
    """ abgesicherte Eingabe fuer Integerwerte (a==False)
    """
    b = 0
 
    while a == False:
        try:
            b = int(input(':'))
            a = True
            if b < 3:
                a =False
                print ('Bitte eine positive Zahl groesser als 2 eingeben', end = ' ')
        except ValueError:
            print ('Bitte eine Integerzahl eingeben', end = ' ')
            a = False
    return b
 
def aufaddition (a, b, c):
    """ addiert die bisher gefundenen Primzahlen auf bis >= aktuelle Zahl
    """
    while a <= c:
        a += b
 
    return (a)
     
pz = [2]
pzsumme = [2]
 
print ('bis zu welcher Zahl sollen die Primzahlen berechnet werden?', end = ' ')
maximum = eingabe (False)
 
pzanz = 1
lfdzahl = 3
flag = True
i = 0
j = 0
 
while lfdzahl in range (2, maximum+1):
     
    while flag == True and i < pzanz:
 
        while i in range (0, pzanz):
            if pzsumme[i] == lfdzahl:
                flag = False                   # keine Primzahl
 
            pzsumme[i] = aufaddition (pzsumme[i], pz[i], lfdzahl)
 
            i += 1
 
    if flag == True:
        pz.append (lfdzahl)
        pzsumme.append (lfdzahl)
        pzanz += 1
 
    lfdzahl +=1
    i = 0
    flag = True
 
 
 
print (pz)