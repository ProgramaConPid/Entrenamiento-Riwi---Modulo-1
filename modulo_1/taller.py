# Taller Modulo 1 - Semana 1 (Sistema de validacion de productos)

# Lista en la cual se almacenaran los productos
productList = []

# Inicializar la variable addProduct en "si" para ingresar al bucle while
addProduct = "si"

# Bucle while que se ejecutara hasta que el usuario no desee agregar mas productos -> (addProduct = "no")
while addProduct == "si":
    name = input("Ingresa el nombre del producto: ").lower()

    while not name.isalpha():
        error_name = input("ERROR, Ingresa un nombre de producto valido: ")
        name = error_name

    price = float(input("Ingresa el precio unitario: "))
    
    # Validar que el precio sea positivo
    while price < 0:
        error_price = int(input("ERROR, Ingresa un precio valido: "))
        price = error_price

    amount = int(input("Ingresa la cantidad del producto (1 - 10): "))
    # Validar que el usuario no sobrepase la cantidad limite (10)
    while amount > 10 or amount < 1:
        error_amount = int(input("Error, Ingresa una cantidad correcta: "))
        amount = error_amount

    discount = input("¿Este producto tiene descuento? si/no: ").lower()

    # Validar si el usuario desea agregar un descuento sobre el producto
    if discount == "si":
        desc_percentage = float(input("Ingresa el porcentaje de descuento (ej. 10 para 10%): "))
        # Se presentara un error si el usuario ingresa un descuento no valido
        if desc_percentage < 0 or desc_percentage > 100:
            print("ERROR - Descuento invalido")
            desc = 0
        else: 
            desc = (desc_percentage / 100) * price * amount # Calcular el descuento
    else:
        desc = 0

    # Calcular el valor total con su respectivo descuento
    final = (price * amount) - desc

    # Diccionario acerca de las caractetiristicas del producto
    product = {
        "Nombre del producto": name,
        "Precio unitario": price,
        "Cantidad del producto": amount,
        "¿El producto tiene descuento?": discount,
        "El descuento es de:": desc,
        "TOTAL": final
    }

    # Agregar el producto a la lista de productos
    productList.append(product)
    response = input("¿Quieres añadir otro producto? si/no: ").lower()

    # Validar si el usuario desea agraegar otro producto
    if response != "si":
        addProduct = "no"

# Imprimir en pantalla el producto/s junto a sus caracteristicas  
for product in productList:
    print(f"""
        Nombre del producto => {product["Nombre del producto"]}
        Precio unitario => {product["Precio unitario"]}
        Cantidad del producto => {product["Cantidad del producto"]}
        ¿El producto tiene descuento? => {product["¿El producto tiene descuento?"]}
        El descuento es de => {product["El descuento es de:"]}
        TOTAL => ${product["TOTAL"]:.2f}
    """)

# ADICIONAL - Recorrer la lista que almacena los productos
total_value = 0
for i in range(len(productList)):
    # Recolectar el valor total de cada producto
    product_value = productList[i]["TOTAL"] 
    # Crear un acumulador que vaya almacenando el total y lo sume con el total de cada producto
    total_value = total_value + product_value

print(f"El precio total de toda la compra es: ${total_value}")