# Inicialización de inventario
productos = ['manzana', 'naranja', 'pera', 'uva']  # Lista de productos
stock = {producto: 0 for producto in productos}  # Diccionario para el stock
bajos = set()  # Conjunto para productos con bajo stock
bajo_limite = 5  # Límite para bajo stock

def agregar_producto(producto, cantidad):
    if producto in productos:
        stock[producto] += cantidad
        print(f"Se han agregado {cantidad} unidades de {producto}.")
        verificar_bajo_stock(producto)
    else:
        print("Producto no válido.")

def eliminar_producto(producto, cantidad):
    if producto in productos:
        if stock[producto] >= cantidad:
            stock[producto] -= cantidad
            print(f"Se han eliminado {cantidad} unidades de {producto}.")
            verificar_bajo_stock(producto)
        else:
            print(f"No hay suficientes unidades de {producto} para eliminar.")
    else:
        print("Producto no válido.")

def verificar_bajo_stock(producto):
    if stock[producto] < bajo_limite:
        bajos.add(producto)
    else:
        bajos.discard(producto)

def mostrar_inventario():
    print("\nInventario actual:")
    for producto in productos:
        print(f"{producto.capitalize()}: {stock[producto]}")

def mostrar_bajos():
    print("\nProductos con menos de 5 unidades:")
    if bajos:
        for producto in bajos:
            print(f"{producto.capitalize()}: {stock[producto]}")
    else:
        print("No hay productos bajos en stock.")

# Función principal para interactuar con el usuario
def main():
    while True:
        comando = input("\nIngrese un comando (ej. 'agregar manzana 10' o 'salir'): ").strip().lower()
        
        if comando == 'salir':
            print("Saliendo del programa...")
            break
        
        partes = comando.split()
        
        if len(partes) == 3:  # Asegurarse de que haya 3 partes
            accion = partes[0]
            producto = partes[1]
            cantidad_str = partes[2]

            try:
                cantidad = int(cantidad_str)
                
                if accion == 'agregar':
                    agregar_producto(producto, cantidad)
                elif accion == 'eliminar':
                    eliminar_producto(producto, cantidad)
                else:
                    print("Acción no válida. Use 'agregar' o 'eliminar'.")
            except ValueError:
                print("La cantidad debe ser un número entero.")
        else:
            print("Comando no válido. Asegúrese de usar el formato correcto.")

        mostrar_inventario()
        mostrar_bajos()

# Ejecutar el programa
if __name__ == "__main__":
    main()
