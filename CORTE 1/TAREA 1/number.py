# Importa el módulo incorporado 'random', el cual proporciona herramientas 
# y funciones para la generación de números aleatorios.
import random

# Importa el submódulo 'pyplot' de la librería externa 'matplotlib', que se 
# utiliza para la creación de gráficos y visualización de datos. Además, 
# le asigna el alias estándar 'plt' para acortar su uso en el código.
from matplotlib import pyplot as plt

# Add your code below:

# Crea una secuencia de números enteros que va desde el 1 hasta el 12 
# (recuerda que el límite superior, 13, es exclusivo). Estos números se 
# guardan en 'numbers_a' y representarán las coordenadas del eje X.
numbers_a = range(1, 13)

# Utiliza una sintaxis avanzada llamada "comprensión de lista" (list comprehension) 
# para ejecutar un ciclo 12 veces (range(12)). En cada vuelta, genera un número 
# entero aleatorio entre 1 y 1000. El resultado es una lista de 12 números 
# aleatorios que se guarda en 'numbers_b' y representará las coordenadas del eje Y.
numbers_b = [random.randint(1, 1000) for i in range(12)]

# Toma los datos generados y crea internamente un gráfico de líneas. 
# Le pasa 'numbers_a' para los valores horizontales (eje X) y 'numbers_b' 
# para los valores verticales (eje Y).
plt.plot(numbers_a, numbers_b)

# Ejecuta el comando necesario para renderizar y mostrar finalmente 
# la figura del gráfico en la pantalla.
plt.show()
