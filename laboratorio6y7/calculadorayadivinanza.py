def calculadora():
    print("Calculadora Básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = int(input("Selecciona una opción (1-4): "))

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == 1:
        print(f"Resultado: {num1 + num2}")
    elif opcion == 2:
        print(f"Resultado: {num1 - num2}")
    elif opcion == 3:
        print(f"Resultado: {num1 * num2}")
    elif opcion == 4:
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Error: División por cero.")
    else:
        print("Opción no válida.")

calculadora()

import random
numero_secreto = random.randint(1, 100)
print("¡Adivina el número (entre 1 y 100)!")
while True:
    intento = int(input("Tu intento: "))
    if intento < numero_secreto:
        print("El número es mayor.")
    elif intento > numero_secreto:
        print("El número es menor.")
    else:
        print("¡Felicidades, adivinaste el número!")
        break
