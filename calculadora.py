numero_1 = int(input("Ingrese el primer número:"))
numero_2 = int(input("Ingrese el segundo número:"))

print("Seleccione la operación que desea realizar:")
print("sus opciones son las siguinetes:")
print("1. Sumar: +")
print("2. Restar: -")
print("3. Multiplicar: *")
print("4. Dividir: /")
operacion = input("ingrese el simbolo de la operacion que desea realizar:")



if operacion == "+":
    print(f"la suma es: " ,numero_1 + numero_2)   
    
    pass
elif operacion == "-":
    print(f"la resta es: ", numero_1 - numero_2)
    
    pass
elif operacion == "*":
    print(f"la multiplicacion es: ", numero_1 * numero_2)
    
    pass            
elif operacion == "/":
    if numero_2 == 0:
        print("Error: no se puede dividir por cero.")
    else:
        print("la division es: ", numero_1 / numero_2)
    
    pass
else:

    print("la operacion ingresada no es valida")


# FUNCIONES PARA LA CALCULADORA BÁSICA


def pedir_numeros():
    pass
def mostrar_menu():
    pass
def sumar(a, b):
    pass
def restar(a, b):
    pass
def multiplicar(a, b):
    pass
def dividir(a, b):
    pass
