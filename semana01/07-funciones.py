def saludar():
    print("Bienvenido")

saludar()
saludar()
saludar()
saludar()

# valores predeterminados
def saludar_con_nombre(nombre, estilo="Formal"):
    if estilo == "Formal":
        print("Buenas noches",nombre)
    else:
        print("Habla",nombre)

saludar_con_nombre("Eduardo")
saludar_con_nombre("Roberto", "informal")

# funcion con valores ilimitados
def sumar(*args):
    print(args)

sumar(10,20,50,22,200)
#todos los parametros ingresados se almacenan en una tupla (inmutable y ordenada)