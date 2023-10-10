contraseña = str(input("Escriba la contraseña: "))
password = "Hola1234"

while contraseña != password:
    print("Error, contraseña inválida.")
    contraseña = str(input("Escriba la contraseña de nuevo: "))
print("Bienvenido")