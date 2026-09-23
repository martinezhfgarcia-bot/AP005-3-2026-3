# Inicia un bucle 'for' que teóricamente está programado para recorrer 
# los números del 1 al 5 (recordando que el límite 6 es exclusivo).
for i in range(1,6):
    
    # Dentro de la primera iteración del 'for' (donde 'i' toma el valor de 1 inicial), 
    # se inicia un bucle interno 'while' que se ejecutará repetidamente 
    # mientras la variable 'i' sea menor o igual a 4.
    while i <= 4:
        
        # Incrementa el valor actual de 'i' sumándole 1 en cada vuelta del 'while'.
        i += 1
        
        # Imprime en la consola el nuevo valor actualizado de 'i'. 
        # (En la consola se verá impreso secuencialmente: 2, 3, 4 y 5).
        print(i)
        
    # Inmediatamente después de que el 'while' termina su trabajo (porque 'i' llegó a 5), 
    # el programa lee esta instrucción 'break'. Esto interrumpe y destruye por 
    # completo el bucle 'for' externo, impidiendo que continúe con los demás números.
    break
