#Ejerciocio de adivinar un numero
print("_________________________________")
print("        ADIVINA EL NUMERO")
print("_________________________________")

import random

#input
n = int(input("Digite el numero que quieres adivinar del 1 al 50: "))
nran = random.randint(1,50)


#process
while n != nran:
    if n<nran:
        print("Perdiste, intenta con un numero mas grande.")
    else:
        print("Perdiste, intenta con un numero mas pequeño.")
    print("")
    n = int(input("Digite otro numero:"))
else:
    print("Ganaste, adivinaste el numero.")