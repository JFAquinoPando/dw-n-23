"""
1- Hacer un programa que imprima del 10 al 0 en orden decreciente.
"""
def imprimir(desde, hasta):
    while(desde >= hasta):
        print(desde)
        desde=desde-1


imprimir(10,2)