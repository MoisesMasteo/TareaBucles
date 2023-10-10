frase = input("Dime una frase: ")
letra = input("Dime la letra que quieres contar: ")

contador = 0
for algo in frase:
    if algo == letra:
        contador = contador + 1
        
print(f"La letra {letra} aparece {contador} veces en la frase {frase}.")