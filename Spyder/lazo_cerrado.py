import numpy as np  # Importa la librería para operaciones matemáticas avanzadas y manejo de arreglos.
import matplotlib.pyplot as plt  # Importa la librería para graficar.
import control  # Importa la librería para modelado y simulación de sistemas dinámicos.

# Parámetros de simulación
x0 = 0  # Condición inicial.
t0, tF, dt = 0, 10, 1E-3  # Tiempo inicial, tiempo final y paso temporal (1 ms).
N = round((tF - t0) / dt) + 1  # Número total de puntos en el tiempo.
t = np.linspace(t0, tF, N)  # Arreglo de tiempo de 0 a 10 segundos con paso de 1 ms.
u1 = np.sin(3.1416 * t)  # Entrada sinusoidal con frecuencia angular 3.1416 rad/s.

# Elementos del circuito PX NORMAL (representa un estado normal del sistema fisiológico).
L1 = 1E-6  # Inductancia en Henrys.
R1 = 0.3  # Resistencia en Ohms.
R2 = 0.3  # Resistencia en Ohms.
C1 = 1.0  # Capacitancia en Faradios.
C2 = 1.2  # Capacitancia en Faradios.

# Cálculo de la función de transferencia para el sistema NORMAL
a1 = L1 * C1 * C2 * R2  # Coeficiente para el término cúbico del denominador.
b1 = C1 * C2 * R1 * R2 + L1 * C1 + L1 * C2  # Coeficiente para el término cuadrático.
c1 = C1 * R1 + C2 * R1 + C2 * R2  # Coeficiente para el término lineal.
d1 = 1  # Coeficiente constante del denominador.
num1 = [1]  # Numerador de la función de transferencia (constante).
den1 = [a1, b1, c1, d1]  # Denominador de la función de transferencia.
sys_open = control.tf(num1, den1)  # Crea la función de transferencia del sistema en lazo abierto.

# Diseño del controlador PID
Kp =   7504.3123990786# Ganancia proporcional.
Ki = 40028.7836532803   # Ganancia integral.
Kd = 312.586659285931  # Ganancia derivativa.
controller = control.tf([Kd, Kp, Ki], [1, 0])  # Controlador PID.

# Sistema en lazo cerrado
sys_closed = control.feedback(controller * sys_open, 1)  # Crea el sistema en lazo cerrado con retroalimentación unitaria.
print("Función de transferencia en lazo cerrado:", sys_closed)

# Respuesta del sistema en lazo cerrado
_, y_closed = control.forced_response(sys_closed, t, u1, x0)  # Respuesta del sistema en lazo cerrado.

# Gráfica de la entrada y la respuesta
plt.figure(figsize=(8, 5))
plt.plot(t, u1, label='Entrada: $u(t)$ (sinusoidal)', color='purple')
plt.plot(t, y_closed, label='Salida: $y(t)$ (Lazo cerrado)', color='blue')
plt.grid(True)
plt.xlim(0, 10)
plt.xticks(np.arange(0, 11, 1))
plt.ylim(-1.5, 1.5)
plt.xlabel('$t$ $[segundos]$')
plt.ylabel('$V(t)$ $[volts]$')
plt.title('Respuesta del Sistema en Lazo Cerrado con Controlador PID')
plt.legend(loc='upper right')
plt.show()
