# Ejercicio 1: Registro de Estudiantes
# Objetivo:

# Crear un diccionario para almacenar información sobre estudiantes y realizar algunas operaciones básicas como agregar, modificar y mostrar datos.
# Instrucciones:

# Crea un diccionario llamado estudiantes, donde las claves sean los nombres de los estudiantes y los valores sean otro diccionario con las claves edad y calificacion.


def show_menu():
  print("""

  1. Agregar nuevo estudiante
  2. Modificar la calificacion de un estudiante
  3. Mostrar informacion de todos los estudiantes
  4. Eliminar un estudiante por su nombre
  5. Salir del programa

""")

students = {}

flag = True
while flag:
  show_menu()

  try:

    user_selection = str(input("Ingresa el numero de la opcion a seguir: "))

    print("")

    if user_selection == "1":
      user_name = str(input("Ingresa tu nombre: ")).lower()

      while not user_name.isalpha():
        user_name = str(input("ERROR!, Ingresa un nombre valido: "))

      user_age = int(input("Ingresa tu edad: "))

      while user_age < 0 or user_age > 100:
        user_age = int(input("ERROR!, Ingresa una edad valida: "))

      user_grade = int(input("Ingresa una calificacion (0 - 100): "))

      while user_grade < 0 or user_grade > 100:
        user_grade = int(input("ERROR!, Ingresa una calificacion valida: "))

      students[user_name] = {"Edad": user_age, "Calificacion": user_grade}

      print("")

      print("* Estudiante creado con exito! *")

      print("")

    if user_selection == "2":
      user_name_modifier = str(input("Ingresa el nombre del usuario al cual le modificaras la calificacion: "))

      print("")

      for user in students.keys():
        
        if user == user_name_modifier:

          user_new_grade = str(input("Ingresa la nueva calificacion: "))
          
          print("")

          students[user_name]["Calificacion"] = user_new_grade

          print(f"La calificacion del estudiante {user} fue actualizada al valor {students[user_name]["Calificacion"]}")

          break

    if user_selection == "3":
      print(students)

  except ValueError:
    print("Ingresaste un valor invalido.")


  

# El programa debe permitir al usuario realizar las siguientes operaciones:
# Agregar un nuevo estudiante (nombre, edad, calificación).
# Modificar la calificación de un estudiante.
# Mostrar la información de todos los estudiantes.
# Eliminar un estudiante por su nombre.