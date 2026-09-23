# Inicia un bucle infinito que mantendrá el programa ejecutándose y pidiendo 
# números continuamente (hasta que el usuario detenga el programa a la fuerza).
while True:

    # Muestra un mensaje en consola pidiendo un dato y utiliza la función int() 
    # para convertir inmediatamente ese texto ingresado en un número entero.
    value = int(input("Enter a positive integer value: "))
    
    # Imprime en pantalla el valor numérico que el usuario acaba de ingresar.
    print("Value: ", value)
    
    # La función isinstance() evalúa si la variable 'value' es del tipo entero (int).
    # El resultado de esta evaluación (True o False) se guarda en la variable 'a'.
    a = isinstance(value, int)
    
    # Verifica que se cumplan dos condiciones a la vez: que el valor sí sea un 
    # entero ('a' es True) y que sea un número positivo (estrictamente mayor a 0).
    if a == True and value > 0:
        
        # Inicializa la variable 'fact' con el valor de 1. Esta variable servirá 
        # como un acumulador multiplicativo para calcular el factorial.
        fact = 1
        
        # Crea un ciclo que recorre los números desde el 1 hasta el número 
        # ingresado por el usuario (se usa '+ 1' porque el límite final es exclusivo).
        for i in range (1, value + 1):
            
            # En cada vuelta, multiplica el acumulador 'fact' por el número actual 'i'
            # y actualiza la variable 'fact' con ese nuevo resultado.
            fact = fact * i            
            
        # Una vez termina el ciclo de multiplicaciones, imprime el resultado final 
        # utilizando una cadena con formato (f-string) para insertar las variables.
        print(f'The factorial of {value} is: ', fact)
        
    # Si la validación inicial falló (por ejemplo, si el usuario ingresó un 0 o un negativo)...
    else:
        
        # Muestra un mensaje de error solicitando que se ingrese un entero positivo válido.
        print("Please, enter a positive integer number")
