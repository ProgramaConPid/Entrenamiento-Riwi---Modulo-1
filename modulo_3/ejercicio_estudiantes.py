# Ejercicio 1: Registro de Estudiantes
# Objetivo:

# Crear un diccionario para almacenar información sobre estudiantes y realizar algunas operaciones básicas como agregar, modificar y mostrar datos.
# Instrucciones:

# Crea un diccionario llamado estudiantes, donde las claves sean los nombres de los estudiantes y los valores sean otro diccionario con las claves edad y calificacion.

# El programa debe permitir al usuario realizar las siguientes operaciones:

def show_menu():
  print("""
        
  MENU DE OPCIONES:

  1. Agregar nuevo estudiante
  2. Modificar la calificacion de un estudiante
  3. Mostrar informacion de todos los estudiantes
  4. Eliminar un estudiante por su nombre
  5. Salir del programa

  """)

def modified_grade(student_name):
  for user in students.keys():
    
    if user == student_name:

      student_new_grade = str(input("Ingresa la nueva calificacion: "))

      students[user_name]["Calificacion"] = student_new_grade

      print(f"La calificacion del estudiante {user} fue actualizada al valor {students[user_name]["Calificacion"]}")

      break

def show_students():

  list_students = list(students.items())

  print("\nLos estudiantes registrados en la base de datos son los siguientes\n")

  for i in range(len(list_students)):

    print(f"Estudiante #{i+1} => {list_students[i]}")

def delete_user(student_delete):

  for student in students.keys():

    if student == student_delete:

      del students[student]

      print(f"El estudiante {student_delete} ha sido elminado con exito!.")
      
      break

students = {}

flag = True
while flag:
  show_menu()

  try:

    user_selection = int(input("Ingresa el numero de la opcion a seguir: "))

    # Agregar un nuevo estudiante (nombre, edad, calificación)
    if user_selection == 1:

      user_name = str(input("\nIngresa el nombre del estudiante: ")).lower()

      while not user_name.isalpha():
        user_name = str(input("ERROR!, Ingresa un nombre valido: "))

      user_age = int(input("Ingresa la edad del estudiante: "))

      while user_age < 0 or user_age > 100:
        user_age = int(input("ERROR!, Ingresa una edad valida: "))

      user_grade = int(input("Ingresa la calificacion del estudiante (0 - 100): "))

      while user_grade < 0 or user_grade > 100:
        user_grade = int(input("ERROR!, Ingresa una calificacion valida: "))

      students[user_name] = {"Edad": user_age, "Calificacion": user_grade}

      print("\n#####################################")

      print(f"* Estudiante {user_name} creado con exito! *")

      print("#####################################\n")

    # Modificar la calificación de un estudiante.
    if user_selection == 2:
      student_name_modifier = str(input("\nIngresa el nombre del estudiante al cual le modificaras la calificacion: "))

      print("")

      if student_name_modifier in students:
        modified_grade(student_name_modifier)
      else:
        print(f"El estudiante {student_name_modifier} no se encuentra en la lista de estudiantes")

    # Mostrar la información de todos los estudiantes.
    if user_selection == 3:

      if len(students) > 0:

        show_students()

      else:
        print("Actualmente no se encuentra ningun estudiante registrado.")

    # Eliminar un estudiante por su nombre.
    if user_selection == 4:
      student_to_delete = str(input("\nIngresa el nombre del estudiante a eliminar: "))

      print("")

      if student_to_delete in students:
        delete_user(student_to_delete)
      else:
        print(f"El estudiante {student_to_delete} no se encuentra registrado en la lista de estudiantes.")

    # Salir del programa
    if user_selection == 5:

      print("\nSaliendo del programa...")

      flag = False

  except ValueError:
    print("Ingresaste un valor invalido, Intentalo de nuevo mas tarde")