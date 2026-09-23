# Las siguientes líneas están comentadas (inactivas), pero su propósito original era
# crear un ciclo del 1 al 20 para evaluar si cada número es par (residuo == 0) o impar.
# for i in range (1,21):
#     residual = i%2
#     if residual == 0:
#         print(f'{i} is even')
#     else:
#         # Muestra una forma alternativa de imprimir comentada (usando f-strings)
#         #print(f'{i} is odd')
#         # Imprime el resultado concatenando la conversión a texto de 'i' con una cadena
#         print(str(i) + ' is odd')

# Otro bloque de código inactivo que pretendía iterar del 0 al 5 (el 6 es exclusivo)
# para calcular y mostrar el cubo (potencia de 3) de cada número en cada vuelta.
# for i in range (0,6):
#     result = i**3
#     print(result)

# Solicita al usuario ingresar un valor por teclado y lo guarda como cadena de texto (string).
times = input("Enter a number of times: ")

# Convierte la entrada de texto a un número con decimales (float). Esto ayuda a 
# evitar errores si el usuario llega a escribir un número con punto, como "5.0".
times = float(times)

# Convierte el número decimal a un número entero (int), recortando cualquier parte decimal.
times = int(times)

# Imprime en consola el tipo de dato final de la variable (mostrará <class 'int'>).
print(type(times))

# Muestra en pantalla el valor numérico entero que quedó guardado en la variable.
print(times)

# Evalúa si el número validado y convertido es exactamente igual a 0.
if times == 0:
    
    # Si la condición es cierta (es 0), se imprime que no se realizará ninguna acción.
    print("Don't do anything")
    
# Si el número ingresado es distinto de 0 (como un número positivo)...
else:
    
    # Inicia un ciclo que cuenta desde el 1 hasta el número ingresado por el usuario. 
    # (Se utiliza '+1' porque el límite superior de la función range siempre es exclusivo).
    for i in range(1, times+1):
        
        # Imprime en cada iteración el valor de la variable contadora 'i'.
        print("i = ", i)
