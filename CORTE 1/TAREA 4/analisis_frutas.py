import pandas as pd

# 1. Carga del archivo CSV (Requisito 1)
try:
    df = pd.read_csv('Fruits.csv')
except FileNotFoundError:
    print("Error: No se encuentra el archivo 'Fruits.csv'.")
    exit()

# 14. Crear nueva columna a partir de una condición definida (Requisito 14)
# Condición: Si el precio es mayor a 2.0 es 'Premium', sino 'Estándar'
df['Categoria'] = ['Premium' if p > 2.0 else 'Estándar' for p in df['price usd']]

# Estructuras explícitas exigidas por el profesor (Requisitos 15, 16, 17)
# Requisito 15: Lista
opciones_menu = ["1. Info general", "2. Buscar fruta", "3. Buscar color", 
                 "4. Filtrar por rango de precios", "5. Precio máx/mín y promedio", 
                 "6. Estadísticas por fruta/color", "7. Ordenar por precio", "8. Salir"]

# Requisito 16: Tupla (usada como referencia para el filtro de precios)
rango_referencia = (0.0, 10.0) 

# Requisito 17: Diccionario (para dar la bienvenida)
mensajes = {"bienvenida": "\n=== SISTEMA DE ANÁLISIS DE FRUTAS ===", "despedida": "\nSaliendo..."}

# 19. Ciclo principal del programa (Requisito 19)
while True:
    print(mensajes["bienvenida"])
    for opcion in opciones_menu:
        print(opcion)
    print("="*37)
    
    # 18. Estructura condicional (Requisito 18)
    seleccion = input("Digita una opción (1-8): ")
    
    if seleccion == '1':
        # 2. Mostrar información básica (Requisito 2)
        print("\n--- INFORMACIÓN DEL DATASET ---")
        print(df.info())
        print("\nPrimeras 5 filas:")
        print(df.head())
        
    elif seleccion == '2':
        # 11. Identificar tipos de fruta diferentes (Requisito 11)
        frutas_unicas = df['type'].unique()
        print(f"\nFrutas disponibles: {list(frutas_unicas)}")
        
        # 3. Mostrar registros de una fruta específica (Requisito 3)
        fruta = input("Escribe la fruta a buscar: ").capitalize()
        filtro = df[df['type'] == fruta]
        
        if not filtro.empty:
            print(f"\nRegistros de {fruta}:")
            print(filtro)
        else:
            print("Fruta no encontrada.")
            
    elif seleccion == '3':
        # 12. Identificar colores diferentes (Requisito 12)
        colores_unicos = df['color'].unique()
        print(f"\nColores disponibles: {list(colores_unicos)}")
        
        # 4. Mostrar registros de un color específico (Requisito 4)
        color = input("Escribe el color a buscar: ").capitalize()
        filtro = df[df['color'] == color]
        
        if not filtro.empty:
            print(f"\nRegistros del color {color}:")
            print(filtro)
        else:
            print("Color no encontrado.")
            
    elif seleccion == '4':
        # 5. Filtrar frutas por rango de precios (Requisito 5)
        print(f"\nRango de referencia sugerido: {rango_referencia[0]} a {rango_referencia[1]} USD")
        try:
            min_p = float(input("Precio mínimo: "))
            max_p = float(input("Precio máximo: "))
            # Uso de operadores lógicos (Tópico evaluativo 10)
            filtro_rango = df[(df['price usd'] >= min_p) & (df['price usd'] <= max_p)]
            print(f"\nFrutas entre {min_p} y {max_p} USD:")
            print(filtro_rango)
        except ValueError:
            print("Error: Debes ingresar números válidos.")

    elif seleccion == '5':
        # 6, 7 y 8. Min, Max y Promedio (Requisitos 6, 7, 8)
        max_precio = df['price usd'].max()
        min_precio = df['price usd'].min()
        promedio = df['price usd'].mean()
        
        fruta_max = df[df['price usd'] == max_precio]['type'].iloc[0]
        fruta_min = df[df['price usd'] == min_precio]['type'].iloc[0]
        
        print("\n--- RESUMEN DE PRECIOS ---")
        print(f"Fruta más cara: {fruta_max} ({max_precio} USD)")
        print(f"Fruta más barata: {fruta_min} ({min_precio} USD)")
        print(f"Precio promedio global: {promedio:.2f} USD")

    elif seleccion == '6':
        # 9 y 10. Estadísticas por fruta o color (Requisitos 9, 10)
        sub_opcion = input("¿Calcular estadística por (1) Fruta o (2) Color?: ")
        if sub_opcion == '1':
            fruta_stat = input("Escribe la fruta: ").capitalize()
            datos_fruta = df[df['type'] == fruta_stat]
            if not datos_fruta.empty:
                print(f"\nEstadísticas de {fruta_stat}:")
                print(datos_fruta['price usd'].describe())
            else:
                print("Fruta no encontrada.")
        elif sub_opcion == '2':
            color_stat = input("Escribe el color: ").capitalize()
            datos_color = df[df['color'] == color_stat]
            if not datos_color.empty:
                print(f"\nEstadísticas del color {color_stat}:")
                print(datos_color['price usd'].describe())
            else:
                print("Color no encontrado.")

    elif seleccion == '7':
        # 13. Ordenar registros de acuerdo al precio (Requisito 13)
        print("\nOrdenando dataset de mayor a menor precio...")
        df_ordenado = df.sort_values(by='price usd', ascending=False)
        print(df_ordenado.head(15)) # Muestra los 15 más caros

    elif seleccion == '8':
        print(mensajes["despedida"])
        break
        
    else:
        print("\nOpción inválida. Intenta nuevamente.")