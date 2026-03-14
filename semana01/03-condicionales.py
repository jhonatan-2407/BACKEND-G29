edad = 10

#if condiciones
if edad > 18:
    print("Eres mayor de edad")
else:
    #si no es verdad
    print("Eres menor de edad")

print("Gracias")


# se puede agregar varias condicionales con and y or
# and > todas tienen q ser verdaderas
# or > basta q una sea verdadera 

# Tengo mi página de ventas ytengo los siguiente, tengo productos que vendo a personas solo de peru
# si al momento de pagar la persona es de peru, el envío es gratis y si no lo es el envpio es 100 dólares 

nacionalidad = "boliviana"

# mostrar cuando se cambia a boliviana

if nacionalidad == "peruana":
    print("Envío gratis")
else:
    print("El envío es 100 dolares")


#Tengo un estaurante y genero promociones, si es jueves 11 am o las 15:00, mostrar el broaster a 5.00, 
# si no indicar que no hay promociones vigentes  
# Si el día es sabado 2x1 en bebidas

dia = "Jueves"
hora = "15:00"

if dia == "Jueves" and (hora == "11:00" or hora == "15:00"):
    print("Tenemos promociones vigentes")

#sino si condicional

elif dia == "sabado":
    print("2x1 en bebidas")

else:
    print("No hay promociones vigentes")


# Tengo una tienda de ropa:
# sie el genero es masculino, solo tengo stock en las tallas XL o L
# Si es femenino tengo stock en L o M
Genero = "Femenino"
Talla = "XL"


#Mostrar al usuario si tengo o no tengo stock en mi ropa 

if Genero == "Masculino" and (Talla == "XL" or Talla == "L"):
    print ("Stock disponible")

elif Genero == "Femenino" and (Talla == "L" or Talla == "M"):
    print ("Stock disponible")

else:
    print("Stock no disponible")



