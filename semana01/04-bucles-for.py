alumnos = ["Eduardo","Pedro","Juan","Gilberto", "Felipe"]

for alumno in alumnos:
    # cada vuelta que se itere , se almacenará en la variable del for

    if alumno == "Eduardo":
        #si quiero saltarme esa iteracion
        continue
    #si quiero detener de manera abrupta ka iteracion
    if alumno == "Gilberto":
        break
    print (alumno)


# range (valor inicial, valor final, incrementador)
# si el valor inicial es 1, podemos prescindir de el
# si el contador es +1, podemos prescindir de el

for numero in range(1,10):
    print(numero)


# también se usa para iterar texto
texto = "Hola mi nombre es Paul"
for letra in texto:
    print(letra)

    #tengo los sgtes precios

productos = [10.5, 11.2, 14, 20]

# el precio mas el igv 18%

for precio in productos:
    print("Valor principal:")
    print(precio)
    print("Valor con igv")
    print(precio * 1.18)

# tengo los siguientes productos

ventas = [
    {
        "producto":"Cafe", 
        "precio": 12.5
    }, 
    {
        "producto":"Agua mineral", 
        "precio": 5
    }, 
    {
        "producto": "Manjar", 
        "precio":8.4
    }]
total = 0

#Me gustaria saber cuanto he vendido (25.90)

for venta in ventas:
    total += venta["precio"]
    print(total)
