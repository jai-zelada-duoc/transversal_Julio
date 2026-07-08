import os
import platform


def limpiar_pantalla():
    """
    Limpia la pantalla de forma compatible con Windows y Linux.
    """
    
    # Detectar el sistema operativo
    sistema = platform.system()
    
    if sistema == "Windows":
        os.system("cls")
    else:  # Linux, macOS, etc.
        os.system("clear")



# ========== DICCIONARIOS INICIALES ==========
dic_juegos = {
    'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
    'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
    'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
    'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
    'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
    'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}

dic_inventario = {
    'G001': [9990, 7],
    'G002': [19990, 0],
    'G003': [42990, 3],
    'G004': [14990, 5],
    'G005': [17990, 9],
    'G006': [39990, 2],
}


# ========== FUNCIÓN: LEER OPCIÓN DEL MENÚ ==========
def leer_opcion():
    """Lee y valida la opción del menú. Retorna un entero válido."""
    while True:
        try:
            opcion = int(input("\t==>> Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("\t\tx ERROR: Debe seleccionar una opción válida")
        except ValueError:
            print("\t\tx ERROR: Debe seleccionar una opción válida")
            # solicita presionar ENTER para continuar.
            input("\nPresione ENTER para continuar...")


# ========== OPCIÓN 1: STOCK POR PLATAFORMA ==========
def stock_plataforma(plataforma, dic_juegos, dic_inventario):
    """Calcula y muestra el stock total disponible para una plataforma."""
    plataforma = plataforma.lower()
    total_stock = 0
    
    for codigo, datos_juego in dic_juegos.items():
        if datos_juego[1].lower() == plataforma:
            total_stock += dic_inventario[codigo][1]
    
    print(f"\tEl total de stock disponibles es: {total_stock}")
    # solicita presionar ENTER para continuar.
    input("\nPresione ENTER para continuar...")
    return


# ========== OPCIÓN 2: BÚSQUEDA POR RANGO DE PRECIO ==========
def busqueda_precio(p_min, p_max, dic_juegos, dic_inventario):
    """Busca y muestra juegos dentro de un rango de precio con stock disponible."""
    juegos_encontrados = []
    
    for codigo, datos_inventario in dic_inventario.items():
        precio = datos_inventario[0]
        stock = datos_inventario[1]
        
        if p_min <= precio <= p_max and stock > 0:
            titulo = dic_juegos[codigo][0]
            juegos_encontrados.append(f"{titulo}--{codigo}")
    
    if juegos_encontrados:
        juegos_encontrados.sort()
        print(f" + Los juegos encontrados son: {juegos_encontrados}")
    else:
        print("\tx ERROR: No hay juegos en ese rango de precios.")


# ========== OPCIÓN 3: ACTUALIZAR PRECIO ==========
def buscar_codigo(codigo, dic_inventario):
    """Verifica si un código existe en el inventario (case-insensitive)."""
    codigo_upper = codigo.upper()
    return codigo_upper in dic_inventario


def actualizar_precio(codigo, nuevo_precio, dic_inventario):
    """Actualiza el precio de un juego si el código existe."""
    codigo_upper = codigo.upper()
    if buscar_codigo(codigo_upper, dic_inventario):
        dic_inventario[codigo_upper][0] = nuevo_precio
        return True
    return False


# ========== OPCIÓN 4: AGREGAR JUEGO - FUNCIONES DE VALIDACIÓN ==========
def validar_codigo(codigo, dic_juegos, dic_inventario):
    """Valida que el código no esté vacío y no exista ya."""
    if not codigo or codigo.isspace():
        return False
    codigo_upper = codigo.upper()
    return codigo_upper not in dic_juegos


def validar_titulo(titulo):
    """Valida que el título no esté vacío ni sea solo espacios."""
    return titulo and not titulo.isspace()


def validar_plataforma(plataforma):
    """Valida que la plataforma no esté vacía ni sea solo espacios."""
    return plataforma and not plataforma.isspace()


def validar_genero(genero):
    """Valida que el género no esté vacío ni sea solo espacios."""
    return genero and not genero.isspace()


def validar_clasificacion(clasificacion):
    """Valida que la clasificación sea exactamente 'E', 'T' o 'M'."""
    return clasificacion in ['E', 'T', 'M']


def validar_multiplayer(multiplayer):
    """Valida que multiplayer sea 's' o 'n' y lo convierte a booleano."""
    if multiplayer.lower() in ['s', 'n']:
        return True
    return False


def validar_editor(editor):
    """Valida que el editor no esté vacío ni sea solo espacios."""
    return editor and not editor.isspace()


def validar_precio_juego(precio):
    """Valida que el precio sea un entero mayor que cero."""
    try:
        precio_int = int(precio)
        return precio_int > 0
    except ValueError:
        return False


def validar_stock_juego(stock):
    """Valida que el stock sea un entero mayor o igual a cero."""
    try:
        stock_int = int(stock)
        return stock_int >= 0
    except ValueError:
        return False


def agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, dic_juegos, dic_inventario):
    """Agrega un nuevo juego a ambos diccionarios."""
    codigo_upper = codigo.upper()
    
    if codigo_upper in dic_juegos:
        return False
    
    # Convertir multiplayer a booleano
    multiplayer_bool = multiplayer.lower() == 's'
    
    # Agregar a diccionario juegos
    dic_juegos[codigo_upper] = [titulo, plataforma, genero, clasificacion, multiplayer_bool, editor]
    
    # Agregar a diccionario inventario
    dic_inventario[codigo_upper] = [int(precio), int(stock)]
    
    return True


# ========== OPCIÓN 5: ELIMINAR JUEGO ==========
def eliminar_juego(codigo, dic_juegos, dic_inventario):
    """Elimina un juego de ambos diccionarios si existe."""
    codigo_upper = codigo.upper()
    
    if buscar_codigo(codigo_upper, dic_inventario):
        del dic_juegos[codigo_upper]
        del dic_inventario[codigo_upper]
        return True
    return False


# ========== PROGRAMA PRINCIPAL ==========
def main():
    # limpia la pantalla
    limpiar_pantalla()
    # menú bienvenida
    print("*"*45)
    print(" ==\tBienvenido al Admin. de Catalogos  ==")
    print(" == \t\tde GameHub\t\t==")
    print("*"*45)
    # valida que se haya ejecutado por 1ra vez
    primera_vez = 1

    """Función principal del programa."""
    while True:
        if primera_vez == 1:
            primera_vez = 0
        else:
            limpiar_pantalla()
        
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Stock por plataforma")
        print("2. Búsqueda de juegos por rango de precio")
        print("3. Actualizar precio de juego")
        print("4. Agregar juego")
        print("5. Eliminar juego")
        print("6. Salir")
        print("=====================================\n")
        
        opcion = leer_opcion()
        
        if opcion == 1:
            # Stock por plataforma
            print(" == 1. STOCK POR PLATAFORMA ==")
            plataforma = input("\tIngrese plataforma a consultar (PC, Switch, PS5 o Xbox): ")
            stock_plataforma(plataforma, dic_juegos, dic_inventario)
        
        elif opcion == 2:
            # Búsqueda de juegos por rango de precio
            print(" == 2. BÚSQUEDA DE JUEGOS x RANGO PRECIO ==")
            while True:
                try:
                    p_min = int(input("\tIngrese precio mínimo: "))
                    p_max = int(input("\tIngrese precio máximo: "))
                    busqueda_precio(p_min, p_max, dic_juegos, dic_inventario)
                    # solicita presionar ENTER para continuar.
                    input("\nPresione ENTER para continuar...")
                    break
                except ValueError:
                    print("\tx ERROR: Debe ingresar valores enteros")
                    # solicita presionar ENTER para continuar.
                    input("\nPresione ENTER para continuar...")
        
        elif opcion == 3:
            # Actualizar precio de juego
            print(" == 3. ACTUALIZAR PRECIO DE JUEGO ==")
            while True:
                codigo = input("\tIngrese código del juego: ")
                
                try:
                    nuevo_precio = int(input("\tIngrese nuevo precio: "))
                    
                    if actualizar_precio(codigo, nuevo_precio, dic_inventario):
                        print(" + Precio actualizado")
                    else:
                        print("\tx ERROR: El código no existe")
                    
                    while True:
                        respuesta = input("+ ¿Desea actualizar otro precio (s/n)?: ").lower()
                        if respuesta in ['s', 'n']:
                            break
                        print("Ingrese 's' o 'n'")
                    
                    if respuesta == 'n':
                        break
                
                except ValueError:
                    print("\tx ERROR: Debe ingresar un precio válido")
                    # solicita presionar ENTER para continuar.
                    input("\nPresione ENTER para continuar...")
        
        elif opcion == 4:
            # Agregar juego
            print(" == 4. AGREGAR JUEGO ==")
            codigo = input("Ingrese código del juego: ")
            titulo = input("Ingrese título: ")
            plataforma = input("Ingrese plataforma: ")
            genero = input("Ingrese género: ")
            clasificacion = input("Ingrese clasificación: ")
            multiplayer = input("¿Es multiplayer? (s/n): ")
            editor = input("Ingrese editor: ")
            precio = input("Ingrese precio: ")
            stock = input("Ingrese stock: ")
            
            # Validar todos los campos
            validaciones = [
                (validar_codigo(codigo, dic_juegos, dic_inventario), "El código es inválido o ya existe"),
                (validar_titulo(titulo), "El título es inválido"),
                (validar_plataforma(plataforma), "La plataforma es inválida"),
                (validar_genero(genero), "El género es inválido"),
                (validar_clasificacion(clasificacion), "La clasificación debe ser 'E', 'T' o 'M'"),
                (validar_multiplayer(multiplayer), "Debe ingresar 's' o 'n' para multiplayer"),
                (validar_editor(editor), "El editor es inválido"),
                (validar_precio_juego(precio), "El precio debe ser un número entero mayor que cero"),
                (validar_stock_juego(stock), "El stock debe ser un número entero mayor o igual a cero"),
            ]
            
            todos_validos = True
            for es_valido, mensaje in validaciones:
                if not es_valido:
                    print(mensaje)
                    todos_validos = False
            
            if todos_validos:
                if agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock, dic_juegos, dic_inventario):
                    print("Juego agregado")
                else:
                    print("El código ya existe")
        
        elif opcion == 5:
            # Eliminar juego
            print(" == 5. ELIMINAR JUEGO ==")
            codigo = input("Ingrese código del juego: ")
            
            if eliminar_juego(codigo, dic_juegos, dic_inventario):
                print("Juego eliminado")
            else:
                print("El código no existe")
        
        elif opcion == 6:
            # Salir
            print("Programa finalizado.")
            break

# ========== EJECUTAR PROGRAMA ==========
main()
