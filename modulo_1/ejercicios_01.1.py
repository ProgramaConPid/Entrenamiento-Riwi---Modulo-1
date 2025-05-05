# 1. Intercambio de valores

valor_1 = int(input('Ingresa el primer valor: '))
valor_2 = int(input('ingresa el segundo valor: '))

print(valor_1,valor_2)

# 2. Inverso de numero de tres cifras

numero_usuario = int(input('Ingresa un numero de tres cifras: '))

centenas = (numero_usuario // 100) % 10
decenas = (numero_usuario // 10) % 10
unidades = numero_usuario % 10

print(unidades,decenas,centenas)

# 3. Extraer hora, minuto, y segundo de segundos totales

num_segundos_usuario = int(input('Ingresa un numero de segundos: '))

horas = num_segundos_usuario // 3600
minutos = (num_segundos_usuario // 60) % 60
segundos = num_segundos_usuario % 10

print(f"{horas} Horas, {minutos} Minutos, {segundos} Segundos")

# 4. Fecha formateada

dia_usuario = int(input('Ingresa el dia: '))
mes_usuario = int(input('Ingresa el mes: '))
ano_usuario = int(input('Ingresa el año: '))

if dia_usuario > 31 or mes_usuario > 12 or ano_usuario > 2025:
    print("ERROR - Dia, Mes o Año invalido")
else:
    if dia_usuario < 10:
        dia = "0" + str(dia_usuario)
    else:
        dia = dia_usuario
    
    if mes_usuario < 10:
        mes = "0" + str(mes_usuario)
    else:
        mes = mes_usuario


print(f"La fecha es: {dia}/{mes}/{ano_usuario}")

# 5. Convertir temperatura F -> C

grados_farenheit = int(input('Ingresa los grados farenheit: '))
grados_celsius = (grados_farenheit - 32) * 5/9

print(f"{grados_celsius} Grados celsius.")

# 6. Calculo de propina y cuenta total

costo_comida = int(input('Ingresa el costo de la comida: '))
propina_usuario = int(input('Ingresa la cantidad de propina que deseas agregar - (10, 15 o 20): '))

if propina_usuario == 10:
    calculo_propina = costo_comida * 0.10
    coste_total = costo_comida + calculo_propina
    print(f"El costo total incluyendo el 10% de propina es: ${int(coste_total)}")

elif propina_usuario == 15:
    calculo_propina = costo_comida * 0.15
    coste_total = costo_comida + calculo_propina
    print(f"El costo total incluyendo el 15% de propina es: ${int(coste_total)}")

elif propina_usuario == 20:
    calculo_propina = costo_comida * 0.20
    coste_total = costo_comida + calculo_propina
    print(f"El costo total incluyendo el 20% de propina es: ${int(coste_total)}")
else:
    print("ERROR - Propina ingresada invalida.")



# 7. extraer un numero de 4 cifras

numero_cuatro_cifras = int(input("Ingresa un numero de cuatro digitos: "))
cadena_numero = str(numero_cuatro_cifras)

digitos = []

for digito in cadena_numero:
    digitos.append(int(digito))
    
print(digitos)

# 8. Formato de precio con decimales

precio_usuario = float(input("Ingresa el precio del producto: "))
precio_redondeado = round(precio_usuario, 2)
precio_formateado = "$"+str(precio_redondeado)

print(f"El precio final del producto es: {precio_formateado}")



# 9. Convertir minutos a dias, horas y minutos

num_minutos = int(input("Ingresa la cantidad de minutos: "))

dias = num_minutos // 1440
horas = num_minutos // 60

print(f"{(dias)} Dias, {horas} Horas")


# 10. Enunciado clasico FizzBuzz

num_usuario = int(input("Ingresa un numero: "))

multiplo_ambos = num_usuario % 3 == 0 and num_usuario % 5 == 0

if multiplo_ambos:
    print("FizzBuzz")
elif num_usuario % 3 == 0:
    print("Fizz")
elif num_usuario % 5 == 0:
    print("Buzz")
else:
    print(num_usuario)



# 11. Entrada al club unicornio ninja

edad_usuario = int(input("Ingresa tu edad: "))

if edad_usuario >= 18 and edad_usuario <= 25:
    pase_dorado = input("Cuentas con un pase dorado? si/no: ")
    if pase_dorado == "no":
        print("Asi no cuentes con pase dorado, estas en el rango de edad para ingresar al club!")
    else:
        print("Tu edad se encuentra en el rango y tienes pase dorado, puedes entrar a la zona VIP del club!")
elif edad_usuario > 25 and edad_usuario < 100:
    pase_dorado = input("Cuentas con un pase dorado? si/no: ")
    if pase_dorado == "si":
        print("Cuentas con la edad indicada y tienes pase dorado, puedes ingresar al club!")
    else:
        print("Cuentas con la edad indicada, pero no tienes pase dorado, por lo tanto, no puedes ingresar al club!")
elif edad_usuario < 18 and edad_usuario > 0:
    print("No cuentas con la edad requerida para ingresar al club!")
else:
    print("ERROR - Ingresaste una edad invalida.")

# 12. Area y perimetro de un circulo

import math

radio_circulo = float(input("Ingresa el radio de la circunferencia: "))
pi = math.pi

perimetro_circulo = pi * radio_circulo
area_circulo = pi * (radio_circulo ** 2)

print(f"El perimetro de la circunferencia es: {round(perimetro_circulo, 2)} y El area es: {round(area_circulo, 2)}")