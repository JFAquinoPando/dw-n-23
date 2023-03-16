"""
Introducir por teclado tantas frases como se deseen y contarlas.
"""
""" frase = ""
contador = -1
while(frase != "*"):
    contador=contador+1
    frase = input("Introduce una frase (* para finalizar):")
print("La cantidad de frases introducidas es:", contador) """

señal_fin = input("Introduce tu señal para finalizar la frase:")
def contar_frases(señal):
    frase = ""
    contador = -1
    frases = []
    while(frase != señal):
        #contador=contador+1
        frase = input("""Introduce una frase:""")
        frases.append(frase)
    frases.pop()
    return len(frases) #contador

cantidad = contar_frases(señal_fin)
print("La cantidad de frases introducidas es:", cantidad)
