# 🐾 Ejercicio: Gestión de Animales

# Desarrolla un programa en Python que permita gestionar información sobre animales. El programa debe tener un menú usando funciones con las siguientes opciones: ** recuerda que pasa nombre, edad y enfermo cada uno debe de guardarse en su propia lista
print("Bienvenido usuario, a continuacion se mostrara un menu, ingresa el numero de la opcion con la que deseas proceder. \n")

# Funcion que muestra el menu
def show_menu():
  print("""
    
    1. Agregar animal/mascota
    2. Eliminar animalmascota
    3. Listar animales/mascotas registradas
    4. Salir del programa
        
  """)

# Funcion para agregar mascota
def add_pet():

  pet_name = str(input("Ingresa el nombre de tu mascota: ")).lower()
  while not pet_name.isalpha():
    error_pet_name = str(input("ERROR, Ingresa un nombre de mascota valido: "))
    pet_name = error_pet_name

  pet_age = int(input("Ingresa la edad de tu mascota: "))
  while pet_age < 0 or pet_age > 20:
    error_pet_age = int(input("ERROR, Ingresa una edad valida: "))
    pet_age = error_pet_age

  pet_sick = str(input("¿Tu mascota se encuentra enferma? - si/no: ")).lower()
  while pet_sick != "si" and pet_sick != "no":
    error_pet_sick = str(input("ERROR, Ingresa si/no para determinar el estado de tu mascota: "))
    pet_sick = error_pet_sick

  pet_data = {
    "Nombre mascota": pet_name,
    "Edad mascota": pet_age,
    "¿Enfermo/a?": pet_sick
  }

  print(f"""
    Los datos ingresados fueron los siguientes:
        
    Nombre mascota => {pet_data['Nombre mascota']}
    Edad mascota => {pet_data['Edad mascota']}
    ¿Enfermo/a? => {pet_data['¿Enfermo/a?']}
    
  """)

  pets_list.append(pet_data)

# Funcion para eliminar mascota
def delete_pet():

  user_pet = str(input("Ingresa el nombre de la mascota a eliminar: ")).lower()

  for i, pet in enumerate(pets_list):

    if pet["Nombre mascota"] == user_pet:
      del pets_list[i]
      print("Mascota eliminada con exito!")
      break
    
# Funcion para mostrar mascotas registradas
def show_pets():
  print(f"La cantidad de mascotas registradas son: {len(pets_list)} y son las siguientes")

  if len(pets_list) > 0:
    for pet in pets_list:

      print(f"""
            
      [Nombre mascota => {pet["Nombre mascota"]}, Edad => {pet["Edad mascota"]}, ¿Enfermo/a? => {pet["¿Enfermo/a?"]}]

      """)

  else:
    print("No se encontró ninguna mascota registrada")
  
# Lista de mascotas
pets_list = []

flag = True
while flag:
  show_menu()

  try:
    user_selection = int(input("Ingresa el numero de la opcion a realizar: "))

    print("")


    match user_selection:
      
      # 1. Agregar un animal:

      # El usuario debe ingresar el nombre, la edad y si el animal está enfermo o no (sí/no). Esta información debe ser almacenada en tres listas separadas: una para los nombres de los animales, otra para sus edades y otra para su estado de salud.

      case 1:
        
        add_pet()
      
      case 2:

        # 2. Eliminar un animal por su nombre:

        # El usuario debe poder ingresar el nombre del animal que desea eliminar. Si el animal está registrado, debe ser removido de las tres listas. Si el animal no está registrado, se debe mostrar un mensaje indicando que no se encontró.
        
        if len(pets_list) > 0:
          delete_pet()
        else:
          print("No se encontró la mascota ingresada.")
        
      case 3:

        # 3. Listar todos los animales registrados:

        # El programa debe mostrar una lista con todos los animales registrados, incluyendo su nombre, edad y estado de salud (enfermo/sano).

        show_pets()

      case 4:
        
        # 4. Salir:

        # El programa debe permitir al usuario salir del menú.

        flag = False

      case _:
        print("ERROR, Ingresa una opcion valida. 1 - 4")

  except ValueError:
    print("ERROR, Ingresaste un valor invalido.")