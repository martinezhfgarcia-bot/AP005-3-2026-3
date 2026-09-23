# Importa el módulo 'time', el cual permite acceder a funciones relacionadas 
# con el reloj del sistema, muy útil para medir el rendimiento de un script.
import time

# Toma la marca de tiempo actual del sistema (en segundos) y la guarda en la 
# variable 'inicio'. Este será el punto de partida de nuestro cronómetro.
inicio = time.time()

# Inicia un bucle externo que recorre los números desde el 0 hasta el 30 
# (el límite de 31 es exclusivo). Estos son los números que evaluaremos.
for i in range(0,31):
    
    # Inicializa una variable contadora en 0 al comienzo de cada iteración. 
    # Esta variable llevará la cuenta de cuántos divisores exactos tiene el número 'i'.
    conta = 0
    
    # Inicia un bucle interno que va desde el 1 hasta el número actual 'i' 
    # (se usa 'i+1' para que el número 'i' sí sea incluido en la división).
    for n in range(1, i+1):
        
        # Calcula el residuo de dividir el número actual 'i' entre el posible divisor 'n'.
        residue = i%n
        
        # Evalúa si la división es exacta (residuo igual a 0).
        if residue == 0:
            
            # Si es una división exacta, incrementa el contador de divisores en 1.
            conta = conta + 1
              
    # Fuera del bucle interno, verifica si el número actual tuvo exactamente 
    # 2 divisores. Matemáticamente, un número primo solo es divisible por 1 y por sí mismo.
    if conta == 2:
        
        # Si la condición se cumple, imprime que el número es primo usando un f-string.
        print(f'{i} es un primo')
        
# Toma una nueva marca de tiempo del sistema justo después de que el bucle 
# haya terminado de evaluar todos los números. Este es el final del cronómetro.
fin = time.time()

# Calcula el tiempo total de ejecución restando el tiempo inicial al tiempo final. 
# Luego, multiplica el resultado por 1000 para convertir los segundos a milisegundos 
# y muestra el resultado en pantalla.
print("t = ", (fin - inicio)*1000)
