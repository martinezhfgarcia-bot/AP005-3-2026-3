# Importa el módulo incorporado 'time', el cual permite utilizar funciones 
# relacionadas con el manejo del tiempo (como pausar la ejecución del script).
import time

# Crea una variable llamada 'cadena' y le asigna el valor de texto "Python".
cadena = 'Python'

# Inicia un bucle 'for' que va a iterar o recorrer uno por uno los caracteres 
# (las letras) que componen la palabra almacenada en la variable 'cadena'.
for letra in cadena:
    
    # En cada iteración, evalúa si el carácter actual es exactamente 
    # igual a la letra minúscula 't'.
    if letra == 't':
        
        # Si la letra efectivamente es la 't', la instrucción 'continue' 
        # aborta la ejecución de las líneas que siguen en esta vuelta y hace 
        # que el bucle salte inmediatamente a la siguiente letra ('h').
        continue
        
    # Si la letra no es la 't' (es decir, no se activó el 'continue'), 
    # el programa llega hasta aquí e imprime el carácter actual en la consola.
    print(letra)
    
    # Utiliza la función 'sleep' del módulo 'time' para detener o pausar 
    # la ejecución del programa durante exactamente 1 segundo antes de pasar 
    # a la siguiente vuelta del ciclo, creando un efecto de impresión retardada.
    time.sleep(1)
