# Bucle que recorre todos los números enteros empezando desde el 100 hasta el 300 
# (recordando que en la función range, el límite superior de 301 es exclusivo).
for i in range(100, 301):
    
    # Se evalúa la condición matemática: si el residuo de dividir la variable 'i' 
    # entre 12 es distinto de cero. El operador '%' obtiene este residuo.
    if (i % 12) != 0:
        
        # Si la condición es verdadera (el número NO es divisible por 12), la palabra 
        # reservada 'continue' fuerza al bucle a omitir el código restante y pasar a 
        # la siguiente iteración.
        continue
        
    # Si la condición del 'if' fue falsa (es decir, el residuo es exactamente 0), 
    # el programa llega a esta línea e imprime el número, confirmando que es múltiplo de 12.
    print(i)
