# Inicializa la variable de control 'a' con el valor de 1 para asegurar 
# que el bucle principal (while) inicie correctamente.
a = 1

# Solicita al usuario ingresar un dato por teclado y lo guarda como cadena de texto.
value = input('Ingrese un valor')

# Convierte explícitamente el texto ingresado a un número entero (int).
value = int(value)

# Inicia un ciclo que se repetirá continuamente mientras la variable 'a' sea igual a 1.
while a == 1:
    
    # Inicia un bucle para recorrer los números desde el 1 hasta el valor ingresado.
    for i in range(1,value+1):
        
        # Reinicia el contador de divisores a 0 para analizar el número actual 'i'.
        conta = 0
        
        # Bucle interno que prueba todos los posibles divisores 'n' desde 1 hasta 'i'.
        for n in range(1, i+1):
            
            # Calcula el residuo de la división entre el número 'i' y el divisor 'n'.
            residue = i%n
            
            # Si la división es exacta (residuo 0), se suma 1 al contador de divisores.
            if residue == 0:
                conta = conta + 1
            
            # Estas líneas están inactivas (comentadas). Se usaban para hacer pruebas 
            # de escritorio (depurar) y ver cómo cambiaban las variables paso a paso.
            # print("i = ", i)
            # print("n = ", n)
            # print("residue = ", residue)
            # print("conta = ", conta)
            
    # Nota sobre la indentación: Como este 'if' está a la misma altura del primer 'for' 
    # (y no por dentro), esta evaluación solo se le aplicará al último número que 
    # haya tomado la variable 'i' (es decir, el número límite que ingresaste).
    # Evalúa si ese último número tuvo exactamente 2 divisores (lo que lo hace primo).
    if conta == 2:
       print(f'{i} es un primo')
       print("\n")
       
    # Si el contador fue diferente de 2, el número no es primo.
    else:
       print(f'{i} NOOO es un primo')
       print("\n")

    # Muestra en consola un mensaje preguntando si se desea evaluar un nuevo número.
    print('Do you want to continue?. Press 1 to do that')
    
    # Captura la respuesta del usuario.
    a = input()
    
    # Convierte la respuesta del usuario a un número entero.
    a = int(a)

    # Evalúa si la respuesta es distinta de 1 (lo que significa que el usuario quiere salir).
    if a != 1:
        
        # La instrucción 'break' fuerza la salida inmediata del bucle 'while', 
        # terminando definitivamente la ejecución del programa.
        break

    # Si el usuario ingresó 1, el bucle no se rompe. Se pide un nuevo valor 
    # numérico para iniciar otra vez el cálculo desde arriba.
    value = input('Ingrese un valor')
    
    # Convierte ese nuevo valor a entero para usarlo en la siguiente vuelta.
    value = int(value)
