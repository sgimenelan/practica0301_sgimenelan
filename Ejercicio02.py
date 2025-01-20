#Escribir una función que lea dos ficheros csv con una lista larga de
#  datos de personas (50 personas y 1000 personas) y llame a dos
#  funciones que pongan su nombre en formato capitalizado y calculen
#  la letra de DNI correspondiente. Realiza la comprobación de
#  rendimiento con la librería cProfile y muestra los datos. 
# Describe que indica cada dato que nos proporciona cProfile.
import os
def capitalizado(n):
    for i in n:
        nombre = i.tittle()
    print(nombres)
def letra():

def procesar_fichero(seleccion):
    if seleccion == 0:
        with open("50.csv", "w") as file:
            capitalizado()

    elif seleccion == 1:
        with open("1000.csv", "w") as file:
            
seleccion = int(print("50.csv(0), 1000.csv(1): "))