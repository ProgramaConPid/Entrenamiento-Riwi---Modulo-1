

# Ejercicios basicos (Nivel principiante)

# 1. Nombre y edad

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

print(f"Hola {nombre}, tienes {edad}")

# 2. Suma de dos numero enteros

n1 = int(input("Ingresa el primr numero: "))
n2 = int(input("Ingresa el segundo numero: "))

resultado = n1 + n2
print(f"El resultado de {n1} + {n2} es: {resultado}")

# 3. Multiplicacion de decimales

num_1 = float(input("Ingresa el primer numero decimal: "))
num_2 = float(input("Ingresa el primer segundo decimal: "))

resultado_multiplicacion = num_1 * num_2
print(f"El resultado de multiplicar {num_1} X {num_2} es: {round(resultado_multiplicacion, 2)}")

# 4. Doble y triple

num_entero = int(input("Ingresa un numero entero: "))

doble = num_entero ** 2
triple = num_entero ** 3

print(f"El doble del numero: {num_entero} es: {doble} y el triple es: {triple}")


# 5. Reprtir n numero de veces una palabra

palabra = input("Ingresa una palabra: ")
cantidad = int(input("Ingresa la cantidad de veces que se repetira la palabra: "))

repeticiones = ((palabra+" ") * cantidad)

print(repeticiones)


# 6. Pedir al usuario dos numeros y mostrar el resultado de dividir el primero entre el segundo

numero_1 = int(input("Ingresa un numero: "))
numero_2 = int(input("Ingresa otro numero: "))

division = numero_1 / numero_2
print(f"El resultado de la division {numero_1} / {numero_2} = {division}")

# 7. Pedir al usuario su nombre y mostrar cuentas letras tiene

nombre_usuario = input("Ingresa tu nombre: ")
convertir_a_lista = nombre_usuario.split(" ")
cadena = ""
cadena = cadena.join(convertir_a_lista)

print(f"El nombre {nombre_usuario} tiene {len(cadena)} letras.")

# 8. Pedir al usuario dos numeros y mostrar la division entera y el modulo entre ellos

x = float(input("Ingresa un numero: "))
y = float(input("Ingresa otro numero: "))

division_entera = x // y
division_al_modulo = x % y

print(f"Div Entera: {x} / {y} = {division_entera} - Div Modulo: {x} % {y} = {division_al_modulo}")

# 9. Todas las operaciones

a = int(input("Ingresa un numero: "))
b = int(input("Ingresa otro numero: "))

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

print(f"Suma = {suma}, Resta = {resta}, Multiplicacion = {multiplicacion}, Division = {division}")

# 10. Potencias con f strings

numero_entero = int(input("Ingresa un numero entero: "))

potencia = num_entero ** 2
cubo = num_entero ** 3

print(f"El doble de {numero_entero} es: {potencia} y el triple es: {cubo}")

# 11. Pedir decimal y mostrar solo el entero

num_decimal = float(input("Ingresa un numero decimal: "))
mostrar_entero = int(num_decimal)

print(f"El entero es: {mostrar_entero}")

# 12. Mayor de edad sin condicional

edad_usuario = int(input("Ingresa tu edad: "))
condicion = edad_usuario >= 18

print(f"El usuario es mayor de edad?: {condicion}")

# 13. Verificar igualdad de numeros

n_1 = int(input("Ingresa un numero entero: "))
n_2 = int(input("Ingresa otro numero entero: "))

igualdad = n_1 == n_2
print(f"{n1} es igual a {n_2}?: {igualdad}")

# 14. Mayor que

numero_uno = int(input("Ingresa el primer numero: "))
numero_dos = int(input("Ingresa el segundo numero: "))

mayor_que = numero_uno > numero_dos
print(f"El numero {numero_uno} es mayor que {numero_dos}?: {mayor_que}")

# 15. Menor o igual

n_uno = int(input("Ingresa el primer numero: "))
n_dos = int(input("Ingresa el segundo numero: "))

menor_o_igual = n_uno <= n_dos
print(f"El numero {n_uno} es menor o igual que {n_dos}?: {menor_o_igual}")

# 16. Ambos mayores que 10

primer_numero = int(input("Ingresa el primer numero: "))
segundo_numero = int(input("Ingresa el segundo numero: "))

ambos_mayores_a_dies = primer_numero > 10 and segundo_numero > 10
print(f"Tanto {primer_numero} como {segundo_numero} son mayores a 10?: {ambos_mayores_a_dies}")

# 17. Al menos uno mayor a 10

p_numero = int(input("Ingresa el primer numero: "))
s_numero = int(input("Ingresa el segundo numero: "))

al_menos_uno_mayor_a_dies = p_numero > 10 or s_numero > 10
print(f"Al menos un numero entre {p_numero} y {s_numero} es mayor a 10?: {al_menos_uno_mayor_a_dies}")

# 18. No son iguales 

num_uno = int(input("Ingresa el primer numero: "))
num_dos = int(input("Ingresa el segundo numero: "))

no_igual = not num_uno == num_dos
print(f"El numero {num_uno} no es igual a {num_dos}?: {no_igual}")

# 19. Promedio

nota_1 = float("Ingresa la primera calificacion - 1/10: ")
nota_2 = float("Ingresa la primera calificacion - 1/10: ")
nota_3 = float("Ingresa la primera calificacion - 1/10: ")

promedio = (nota_1 + nota_2 + nota_3) / 3
print(f"El promedio final es: {promedio}")

# 20. Divisible entre 5

numeroUno = int(input("Ingresa un numero entero: "))

divisible_entre_cinco = numero_uno % 5 == 0
print(f"El numero {numeroUno} es divisible entre 5?: {divisible_entre_cinco}")