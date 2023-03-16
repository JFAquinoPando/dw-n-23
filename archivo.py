def obtener_edad():
    print("Hola desde la función")

# obtener_edad()

def saludar(nombre = 'Anónimo'):
    print("Hola, soy " + nombre + ", y tu?")

saludar()
saludar('Pedro')


def operacionAritmetica(numero1, numero2, operacion):
    if (operacion == "suma" or operacion == "+"):
        return numero1 + numero2
    elif(operacion == "resta" or operacion == "-"):
        return numero1 - numero2
    elif(operacion == "multiplicacion" or operacion == "*"):
        return numero1 * numero2
    elif(operacion =="dividir" or operacion == "/"):
        if(numero2 == 0):
            return "No se puede dividir entre 0 (cero)"
        return numero1 / numero2
    else:
        return "No hay operacion posible"

numero1 = int(input("Ingrese un valor: "))
numero2 = int(input("Ingrese otro valor: "))
operacion = input("Ingrese la operacion a realizar: ")
valor = operacionAritmetica(numero1, numero2, operacion)
print("resultado: ",valor)
