nombres = ["Juan", "Ana", "Luis"]
print("Lista de estudiantes:")
for nombre in nombres:
    print(nombre)

contactos = {
    "Juan": "juan@example.com",
    "Ana": "ana@example.com"
}
print("Contactos:")
for clave, valor in contactos.items():
    print(f"{clave}: {valor}")

nuevo_nombre = input("Agrega un nuevo nombre: ")
nombres.append(nuevo_nombre)

nuevo_contacto = input("Agrega un nuevo correo para Juan: ")
contactos["Juan"] = nuevo_contacto
print(f"Lista actualizada: {nombres}")
print(f"Contactos actualizados: {contactos}")