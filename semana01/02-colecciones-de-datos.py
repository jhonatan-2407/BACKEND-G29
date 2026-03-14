#Listas (lists)
# Mutable (puede cambiar su contenido) y ordenada (se maneja por indices)

numeros_telefonicos = ["105","104","694944654",123]

numeros_telefonicos.append("*123#")
numeros_telefonicos.append(True)

# podemos acceder por sus indices siempre empieza en cero
print(numeros_telefonicos[0])

#se puede obtener uan sub lista de los elementos usando limites
print(numeros_telefonicos[1:3])
print(numeros_telefonicos[2:])
print(numeros_telefonicos[:3])
print(numeros_telefonicos[-1])

#la forma en la cual se puede retirar elementos
# con el metodo pop lo quitamos  de la lista almacenandolo en otra variable

elemento_eliminado = numeros_telefonicos.pop(0)

# del > elimina el elemento y ya no se recupera
del numeros_telefonicos[0]

#clear limpia toda la lista y la dejsa enblanco
numeros_telefonicos.clear()

#Crear una lista menu_postres:
#croissant
#torta de manzana
#voladores
#luego quitar los croissant
#agregar alfajores
#Imprimir la lista para ver q hay

menu_postres = ["Croissant", "Torta de manzana", "voladores"]
del menu_postres[0]
menu_postres.append("Alfajores")
print(menu_postres)
print(menu_postres[0:1])
print(menu_postres[0:2])


#### TUPLAS ###
# Ordenadas pero no se pueden editar(una vez creadas ahi quedan)

usuarios = ("eduardo","jhonatan", "roxana", "marta")

#Yo puedo solicitar si un valor esta o no en la tupla con la palabra in
print("eduardo" in usuarios)



### diccionarios ###
#coleccion de datos que se manejan por llave-valor en vez de indices y tambn son editables

persona ={
    "nombre":"eduardo",
    "apellido":"perez",
    "nacionalidad":"peruana",
    "direccion":{
        "calle":"av primavera",
        "numero":"1250",
        "referencia":"a media cuadra del semaforo"
    },
    "hobbies":["jugar","pintar","pescar"]

}

print(persona["nombre"])

#como podria saber cual es la calle donde vivo?
#bailar es uno de mis hobbies?
#me gustaria saber mi ultimo hobbie

print(persona["direccion"]["calle"])
print("bailar" in persona["hobbies"])
print(persona["hobbies"][-1])

articulos = {
    "cafe": {
        "cantidad": 10,
        "precio": 4.5,
        "disponible": True
    },
    "leche":{
        "cantidad": 2,
        "precio": 2.3,
        "disponible": False
    },
    "te": {
        "cantidad": 0,
        "precio": 0.5,
        "disponible":False
    },
    "observaciones": ("Falta te", "Agregar azucar", "Mejorar presentacion")
}

#cantidades de leches
#la segunda observacion
#precio del cafe
print(articulos["leche"]["cantidad"])
print(articulos["observaciones"][1])
print(articulos["cafe"]["precio"])


# CONJUNTOS #
#MO ES ORDENADO PERO ESMODIFICABLE

planetas = {"Tierra","Marte","Jupiter","Uranio"}

planetas.add("Neptuno")

planetas.remove("Tierra")

print("Tierra" in planetas)
print(planetas)
