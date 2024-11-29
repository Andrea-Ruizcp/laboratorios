numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(f"El cuadrado de {num} es {num ** 2}")

while True:
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada.lower() == "salir":
        break
    print("Aún no has escrito 'salir'.")