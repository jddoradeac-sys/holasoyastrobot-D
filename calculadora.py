def calcular_propina():
    """Calculadora de propinas flexible"""
    
    print("=" * 50)
    print("      CALCULADORA DE PROPINAS")
    print("=" * 50)
    
    # Obtener el monto total
    while True:
        try:
            monto_total = float(input("\n¿Cuál es el monto total de la cuenta? $"))
            if monto_total < 0:
                print("El monto no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Por favor ingresa un número válido.")
    
    # Opciones de propina
    print("\nOpciones de propina:")
    print("1. Porcentaje personalizado")
    print("2. 10%")
    print("3. 15%")
    print("4. 20%")
    print("5. 25%")
    
    opcion = input("\nSelecciona una opción (1-5): ")
    
    if opcion == "1":
        while True:
            try:
                porcentaje = float(input("¿Cuál es el porcentaje de propina? %"))
                if porcentaje < 0:
                    print("El porcentaje no puede ser negativo.")
                    continue
                break
            except ValueError:
                print("Por favor ingresa un número válido.")
    elif opcion == "2":
        porcentaje = 10
    elif opcion == "3":
        porcentaje = 15
    elif opcion == "4":
        porcentaje = 20
    elif opcion == "5":
        porcentaje = 25
    else:
        print("Opción no válida. Usando 15% por defecto.")
        porcentaje = 15
    
    # Calcular propina
    propina = monto_total * (porcentaje / 100)
    total_con_propina = monto_total + propina
    
    # Mostrar resultados
    print("\n" + "=" * 50)
    print("RESULTADO:")
    print("=" * 50)
    print(f"Monto original:        ${monto_total:.2f}")
    print(f"Porcentaje de propina: {porcentaje}%")
    print(f"Propina:               ${propina:.2f}")
    print(f"Total a pagar:         ${total_con_propina:.2f}")
    print("=" * 50)
    
    # Preguntar si quiere calcular otra
    repetir = input("\n¿Deseas calcular otra propina? (s/n): ")
    if repetir.lower() == "s":
        calcular_propina()
    else:
        print("\n¡Gracias por usar la calculadora de propinas!")


# Ejecutar la calculadora
if __name__ == "__main__":
    calcular_propina()
    pass
def multiplicar(a, b):
    pass
def dividir(a, b):
    pass





# Dónde está el bug

try:
    password = int(input("Clave: "))

# Agregar prints para investigar

    print(f"DEBUG tipo: {type(password)}")

    print(f"DEBUG valor: [{password}]")

    print(f"DEBUG len: {len(str(password))}")
    
    if password == 1234: # bug aca y ahora si
        print("Acceso concedido")

    else:
    
        print("Acceso denegado")
except ValueError:
    
    print("Error: debe ingresar un número")
    

# calculadora de propinas

# Pedir total de la cuenta
total = float(input("Ingrese el total de la cuenta: "))

# Pedir porcentaje de propina
porcentaje = int(input("Ingrese el porcentaje de propina (10, 15 o 20): "))

# Validar porcentaje
if porcentaje == 10 or porcentaje == 15 or porcentaje == 20:
    propina = total * (porcentaje / 100)
    total_con_propina = total + propina
    
    print(f"Propina: Q{propina:.2f}")
    print(f"Total a pagar: Q{total_con_propina:.2f}")
else:
    print("Porcentaje no válido")


# Contador 

contador = 0
i = 1
while i <= 10:
    if i % 2 == 0:
        contador += 1
    i += 1
print(f"pares: {contador}") 
#  resultado:  pares: 5

# acumulador 

suma  = 0
i = 1
while i <= 100:
    suma += i
    i += 1
print(f"total: {suma}")
# resultado: total: 5050


import random
numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 10

while intentos < max_intentos:
    intento = int(input("Adivina un numero (1-100): "))
    intentos += 1
    
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado el número {numero_secreto} en { intentos} intentos.")
        break
    










