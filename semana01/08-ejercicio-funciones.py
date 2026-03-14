# crear una funcion en la cual sirva para calcular la propina de una cuenta, en esta funcion se recibira la cuenta y el porcentaje de propina, es decir, el monto y cuanto de ese monto debe de darse como propina. 
# calcular_propina(100,15)
# el resultado debe ser: "Propina es de 15 soles"
# El valor predeterminado del porcentaje es 10

def calcular_propina(monto, porcentaje=10):
     
    propina = (monto * porcentaje /100)

    print("propina es de ", propina, "soles")

calcular_propina(100,15)
calcular_propina(200)





# Hacer el fizzbuzz 
# FizzBuzz es un popular ejercicio de programación que consiste en imprimir los números del 1 al 100. Se sustituyen los múltiplos de 3 por "Fizz", los múltiplos de 5 por "Buzz" y los múltiplos de ambos (como 15) por "FizzBuzz". Se suele usar para evaluar la lógica básica en entrevistas de desarrollo
# procesar_numero()
# Devolver "Fizz" si el numero es divisible entre 3
# Devolver "Buzz" si el numero es divisible entre 5
# Devolver "FizzBuzz" si el numero es divisible entre 3 y 5
# 30 % 3 > True 

def procesar_numero(numero):
    
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
  
    elif numero % 3 == 0:
        print ("Fizz")
    
    elif numero % 5 == 0:
        print ("Buzz")
    
    else:
        print (numero)       
        

procesar_numero(15)


# Funcion que reciba un operador suma, resta o mutiplicacion y n cantidad de numeros
# y retorne el resultado en base a su operador
# super_funcion("suma", 10,20,30,40,50 ... ) 150

def super_funcion (operacion,*numeros):
    total = 0
    #valores en tupla
    if operacion == "suma":
        for numero in numeros:
            total = total + numero

    elif operacion == "resta":
        for numero in numeros:
            total = total - numero


    elif operacion == "multiplicacion":
        total = 1
        for numero in numeros:
            total = total * numero

    else:
        print ("Operacion no válida")
    print(total)


super_funcion("suma", 10,20,30,40,50)
super_funcion("resta", 100,10,5,6)
super_funcion("multiplicacion",5,4,6,7 )
