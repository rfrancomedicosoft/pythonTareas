# MédicoSoft 2020
# 1. Encuentra el par con la suma dada en el arreglo
# Lee el README.md antes de comenzar


def find_pair(array, sum):
    for i in range (0, len(array), 1): #iteración para leer todos los datos del array.
        z = array [i]
        for j in range (i+1, len(array), 1): #iteración para leer todos los datos del array una posición adelante del anterior 
            y = array [j]
            if z + y == sum:
                print (z, y)
       # array [i] = 0   #Esta fue la solución para la duplicación de pares. Alcance a corregirlo.
            
            

def envio_variables():     #Función para enviar los datos.
    array = [2,4,0,6,1,7,8,3,2,5]
    sum = 10
    find_pair(array, sum)

envio_variables()
