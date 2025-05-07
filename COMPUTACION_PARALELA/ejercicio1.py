'''
# Suma de elementos de una lista 
# Taxonomia SISD.
lista = [1,2,3,4,5,6,7,8,9,10]

def suma(lista):
    total = 0
    for i in lista:
        total += i
    return total

print(suma(lista))

# Suma de dos arreglos
# Taxonomia SIMD.
import numpy as np
arreglo1 = np.array([1,2,3,4,5])
arreglo2 = np.array([6,7,8,9,10])
arreglo3 = arreglo1 + arreglo2
print(arreglo3)
'''

# Múltiples algoritmos de verificación sobre los mismos datos
# Taxonomia MISD
data = 10
print(all([data > 5, data % 2 == 0, data < 20]))

# otra forma de hacerlo
datos_verificar = [1, 2, 3, 4, 5]
def forma1(dato):
    return sum(dato)
def forma2(dato):
    resultado = 0
    for i in dato:
        resultado += i
    return resultado
resultado1 = forma1(datos_verificar)
resultado2 = forma2(datos_verificar)
if resultado1 == resultado2:
    print("Los resultados son iguales")
else:
    print("Los resultados son diferentes")

# otra forma de hacerlo en menos lineas de código
datos_verificar = [1, 2, 3, 4, 5]
resultado1 = sum(datos_verificar)
resultado2 = 0
for i in datos_verificar:
    resultado2 += i
if resultado1 == resultado2:
    print("Los resultados son iguales")
else:
    print("Los resultados son diferentes")







''''''
# Procesamiento paralelo de una lista de tareas 
# Taxonomia MIMD.
from multiprocessing import Pool
import multiprocessing
tareas = ["tareaA", "tareaB", "tareaC", "tareaD"]
def proceso(tarea):
    print(tarea)
procesamiento = multiprocessing.Pool()
procesamiento.map(proceso, tareas)

from multiprocessing import Pool
print(Pool().map(lambda x: x**2, ["A", "B", "C", "D"]))

# otra forma de hacerlo
import multiprocessing
tareas = ["tareaA", "tareaB", "tareaC", "tareaD"]
def proceso(tarea):
    return tarea
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        resultados = pool.map(proceso, tareas)
    for resultado in resultados:
        print(resultado)


# Sumar un valor a cada elemento de un arreglo 
# Taxonomia SIMD.
# Usando numpy
import numpy as np
arreglo = np.array([1,2,3,4,5])
arreglo += 1
print(arreglo)

arreglo = [1,2,3,4,5]
for i in range(len(arreglo)):
    arreglo[i] += 1
print(arreglo)

# Contar la frecuencia de palabras en diferentes partes de un texto 
# Taxonomia MIMD.
texto = "Hola mundo. Hola a todos. Hola a todos los que están aquí."
palabras = texto.split()
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
print(frecuencia)


# Calcular la factorial de un número 
# Taxonomia SISD.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) # n-1 porque el factorial de n es n*(n-1)*(n-2)*...*1

print(factorial(5))

# Calcular la longitud de una cadena usando diferentes métodos
# Taxonomia SIMD.
cadena = "Hola mundo"
longitud = len(cadena)
print(longitud)

# otra forma de hacerlo
longitud = 0
for i in cadena:
    longitud += 1
print(longitud)

longitud = 0
for i in range(len(cadena)):
    longitud += 1
print(longitud)