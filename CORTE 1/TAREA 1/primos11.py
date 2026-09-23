# Importa el módulo 'time', el cual proporciona herramientas para medir el tiempo 
# de ejecución de las operaciones del código.
import time

# Captura el tiempo actual del sistema en segundos y lo almacena en la variable 
# 'inicio' para utilizarlo como punto de partida de nuestra medición.
inicio = time.time()

# Inicia un bucle externo que recorre los números desde el 1 hasta el 30 
# (el límite 31 es exclusivo). A diferencia del ejemplo anterior, este inicia en 1.
for i in range(1,31):
    
    # Inicializa una variable contadora en 0 al comienzo de cada iteración. 
    # Esta variable llevará la cuenta de cuántos divisores exactos tiene el número 'i'.
    conta = 0
    
    # Inicia un bucle interno para iterar desde el 1 hasta el número actual 'i' 
    # (se usa 'i+1' para asegurar que el número actual sea incluido en la división).
    for n in range(1, i+1):
        
        # Calcula el residuo de dividir el número actual 'i' entre el divisor de prueba 'n'.
        residue = i%n
        
        # Evalúa si la división fue exacta (residuo igual a 0).
        if residue == 0:
            
            # Si es un divisor exacto, incrementa el valor de la variable contadora en 1.
            conta = conta + 1              
            
    # Al finalizar el bucle interno, verifica si el número tuvo exactamente 2 divisores.
    # Un número es primo si solo es divisible por 1 y por sí mismo.
    if conta == 2:
        
        # Imprime en la consola que el número evaluado es primo utilizando un f-string.
        print(f'{i} es un primo')
        
        # Imprime un salto de línea adicional ("\n") para separar visualmente 
        # este resultado del siguiente número primo que se encuentre.
        print("\n")

# Captura nuevamente el tiempo del sistema justo después de que terminan los ciclos.
fin = time.time()

# Calcula el tiempo total restando el tiempo de inicio al tiempo final, 
# y multiplica el resultado por 1000 para mostrar los segundos convertidos a milisegundos.
print("t = ", (fin - inicio)*1000)
