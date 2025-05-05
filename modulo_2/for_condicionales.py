# 10 Nuevos Ejercicios para Practicar Ciclo for en Python

# 1. Imprimir caracteres de una cadena:

cadena = input("Ingresa una palabra: ")

for caracter in cadena:
    print(caracter)

print("")
# 2. Sumar los números en una lista:

lista = [1, 2, 3, 4, 5]

suma = 0
for i in range(len(lista)):
    suma += lista[i]

print(f"La suma de los numeros es {suma}")

print("")
# 3. Números impares del 1 al 30:

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

for numero in lista:

    if numero % 2 != 0:
        print(numero)

# 4. Encontrar la letra más frecuente:

palabra = input("Ingresa una palabra: ")
repeticiones = 0

for letra in palabra:
    if letra in palabra:
        conteo = palabra.count(letra)
        if conteo > 1:
            print(f"La letra {letra} se repite {conteo} veces.")
            break
        else:
            print("Ninguna letra se repite mas de 1 vez.")
            break

print("")

# 5. Verificar si un número es primo:

numero = int(input("Ingresa un numero: "))

for i in range(2, numero):

    if numero % i == 0:
        print(f"El numero {numero} no es primo.")
        break
    else:
        print(f"El numero {numero} es primo.")
        break

print("")

# 6. Sumar números negativos:

numeros = [4, -2, -6, 7, -3]

suma_negativos = 0
for i in range(len(numeros)):

    if numeros[i] > 0:
        continue
    else:
        suma_negativos += numeros[i]

print(f"La suma de los numeros negativos es: {suma_negativos}")

# 7. Contar palabras con más de 3 letras:

palabra_usuario = input("Ingresa una oracion: ")

convertir_oracion = palabra_usuario.split("")

