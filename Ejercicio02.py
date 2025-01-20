#Escribir una función que lea dos ficheros csv con una lista larga de
#  datos de personas (50 personas y 1000 personas) y llame a dos
#  funciones que pongan su nombre en formato capitalizado y calculen
#  la letra de DNI correspondiente. Realiza la comprobación de
#  rendimiento con la librería cProfile y muestra los datos. 
# Describe que indica cada dato que nos proporciona cProfile.
import cProfile
def capitalizado(n):
    for i in n:
        nombre = i.split(",")[0].strip()
        print(nombre.title())

def letra(n):
    letras_dni = {
        0: "T", 1: "R", 2: "W", 3: "A", 4: "G", 5: "M", 6: "Y",
        7: "F", 8: "P", 9: "D", 10: "X", 11: "B", 12: "N", 13: "J",
        14: "Z", 15: "S", 16: "Q", 17: "V", 18: "H", 19: "L", 20: "C",
        21: "K", 22: "E"
    }
    for i in n:
        x = i.split(",")
        if len(x) > 1:
            numero = int(x[1].strip())
            print(x[1].strip(), letras_dni[numero % 23])

def procesar_fichero():
    seleccion = input("Ingrese el nombre del archivo (50.csv o 1000.csv): ")
    with open(seleccion, "r") as file:
        lista = file.readlines()
        capitalizado(lista)
        letra(lista)
cProfile.run("procesar_fichero()")
procesar_fichero()

            
