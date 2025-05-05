# Control de acceso con doble autenticacion 


datos_usuario = {}
usuario = str(input("Ingresa tu nombre de usuario: "))
contraseña_usuario = str(input("Ingresa la contraseña: "))

intentos = 3
contraseña_fija = "pepe123"
verificacion = "12AK03"

if contraseña_usuario == contraseña_fija:
    codigo_verificacion = str(input(f"\nHola {usuario} Ingresa el codigo de verificacion que se te envio por SMS: "))
    while codigo_verificacion != verificacion:
        error_verificacion = str(input(f"\nERROR!, Ingresa nuevamente el codigo, tienes {intentos} intentos: "))
        intentos = intentos - 1

        codigo_verificacion = error_verificacion

        if codigo_verificacion == verificacion:
            print("ACCESO PERMITIDO!")

            datos_usuario = {
            "Nombre de usuario": usuario,
            "Contraseña": contraseña_usuario,
            "Codigo de verificacion": codigo_verificacion
            }

            print(f"Los datos de inicio de sesion son los siguientes {datos_usuario}")
            break
        else:
            if intentos == 1:
                print("ERROR, Superaste el limite de intentos.")
                break
else:
    print("\nContraseña incorrecta, vuelve a intentarlo mas tarde.")
