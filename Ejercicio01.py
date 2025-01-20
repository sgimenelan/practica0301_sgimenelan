#Escribir dos funciones, una función que reciba un número entero positivo n 
# y calcule el número de fibonacci asociado a ese número de manera recursiva
#  y otra función que haga la misma operación pero con bucles.
#Con ambas funciones, calcular y comparar el tiempo de ejecución para 
# n = (1, 10, 20, 30 y 40) por fuerza bruta.
def numerofibonacci_bucle(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a
def numerofibonacci_recursiva(n):
    if n == 0 or n == 1:
        return 0
    if n == 2 or n== 3:
        return 1
    else:
        return numerofibonacci_recursiva(n - 1) + numerofibonacci_recursiva(n - 2)
    
import datetime
start_time = datetime.datetime.now()
print(numerofibonacci_bucle(int(input("Introduce un numero entero: "))))
end_time = datetime.datetime.now()
print("El tiempo de ejecución es:", end_time - start_time)