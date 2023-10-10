palabra = str(input("Dime una palabra: "))

letras = []

for reversa in palabra:
    letras.append(reversa)

for reversa in reversed(letras):
    print(reversa, end="")