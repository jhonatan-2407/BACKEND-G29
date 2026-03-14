#Se tiene numero ganador y el ususario tiene que intentar adivinarlo, si el numero ganador es 10
#y  el usuario ingresa 20, entonces indicarle que el numero es menor
# y si el usuario ingresa 5, indicarles que el numero es mayor
# si el usuario adivina el numero, felicitarlo y termina el juego

numero_ganador = 10
intento = 0

while intento != numero_ganador:
    
   
    intento = int(input("Introduce un número: "))
    
    if intento > numero_ganador:
        print("El número secreto es menor")
    elif intento < numero_ganador:
        print("El número secreto es mayor")
    else:
        print("Felicidades encontraste el número secreto")

print("Fin del juego")

    