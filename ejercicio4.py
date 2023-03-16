"""
Hacer un programa que imprima los números
impares entre el 10 y el cero en orden decreciente
y que calcule la suma de esos números impares.
"""
""" inicio = 10
suma = 0
while(inicio >= 0):
    if(inicio % 2 != 0):
        print("impar", inicio)
        suma = suma + inicio
    inicio-=1 # inicio=inicio - 1
print("La suma de numeros impares es:", suma) """
""" 
def devolver_impar():
    inicio = 10
    suma = 0
    while(inicio >= 0):
        if(inicio % 2 != 0):
            print("impar", inicio)
            suma = suma + inicio
        inicio-=1 # inicio=inicio - 1
    print("La suma de numeros impares es:", suma)

devolver_impar() """


def devolver_impar(inicio, fin):
    suma = 0
    lista_impar = []
    while(inicio >= fin):
        if(inicio % 2 != 0):
            #print("impar", inicio)
            lista_impar.append(inicio)
            suma = suma + inicio
        inicio-=1 # inicio=inicio - 1
    return [suma, lista_impar]
    
def imprimir_resultados(suma, listado):
    print("La suma de los valores es", suma)
    hasta = len(listado)
    desde = 0
    while(desde < hasta):
        print("impar:",listado[desde])
        desde=desde+1


resultados = devolver_impar(100,80)
print("Resultados: ", resultados)
imprimir_resultados(resultados[0], resultados[1])
###############################

resultados = devolver_impar(10,0)
print("Resultados: ", resultados)
imprimir_resultados(resultados[0], resultados[1])
###############################

resultados = devolver_impar(5,2)
print("Resultados: ", resultados)
imprimir_resultados(resultados[0], resultados[1])

