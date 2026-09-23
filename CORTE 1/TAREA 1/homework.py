# Solicita al usuario ingresar un dato por teclado, el cual se guarda inicialmente 
# en la variable 'a' como una cadena de texto (string).
a = input("Enter a number: ")

# Convierte explícitamente el texto almacenado en 'a' a un número entero (int) 
# y sobrescribe la variable con este nuevo valor numérico.
a = int(a)

# Pide al usuario que ingrese un segundo dato y lo guarda en la variable 'b' como texto.
b = input("Enter b number: ")

# Transforma el texto de 'b' a un número con decimales (float) y lo reasigna a la variable.
b = float(b)

# Realiza la suma matemática entre la variable entera 'a' y la decimal 'b', 
# guardando el resultado de la operación en la variable 'c'.
c = a + b

# Evalúa si el valor numérico de 'a' es exactamente igual al valor numérico de 'b' 
# (por ejemplo, si 'a' es 5 y 'b' es 5.0, esta condición sería verdadera).
if a == b:
    
    # Si los valores son idénticos, imprime en consola la palabra "equal".
    print("equal")
    
# Si la condición del 'if' es falsa (los números tienen valores distintos)...
else:
    
    # Imprime la palabra "Different" en la pantalla.
    print("Different")

# Utiliza la función type() para obtener y mostrar en pantalla la clase o tipo de 
# dato de la variable 'a' (mostrará <class 'int'>).
print("Type of a is: ", type(a))

# Muestra en consola el tipo de dato que contiene la variable 'b' (mostrará <class 'float'>).
print("Type of b is: ", type(b))

# Imprime en pantalla el resultado de la suma que calculamos anteriormente en 'c'.
print("c = ", c)

# A diferencia de la primera comparación (que miraba el valor), aquí se evalúa 
# estrictamente si ambas variables pertenecen a la misma clase (mismo tipo de dato).
if type(a) == type(b):
    
    # Si ambas variables compartieran el mismo tipo (ej. ambas int), se imprime esto.
    print("a and b are of the same type")
    
# Si los tipos de dato no coinciden (como en este script, donde 'a' es int y 'b' es float)...
else:
    
    # Imprime el mensaje confirmando que las variables son de tipos diferentes.
    print("a and b are of different type")
