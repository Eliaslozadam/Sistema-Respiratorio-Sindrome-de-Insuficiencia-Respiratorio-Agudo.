import numpy  # Importa la librería para operaciones matemáticas avanzadas y manejo de arreglos.
import matplotlib.pyplot as plt  # Importa la librería para graficar.
import control  # Importa la librería para modelado y simulación de sistemas dinámicos.

# Parámetros de simulación
x0 = 0  # Condición inicial.
t0, tF, dt = 0, 10, 1E-3  # Tiempo inicial, tiempo final y paso temporal (1 ms).
N = round((tF - t0) / dt) + 1  # Número total de puntos en el tiempo.
t = numpy.linspace(t0, tF, N)  # Arreglo de tiempo de 0 a 10 segundos con paso de 1 ms.
u1 = numpy.sin(3.1416 * t)  # Entrada sinusoidal con frecuencia angular 3.1416 rad/s.

# Elementos del circuito PX NORMAL (representa un estado normal del sistema fisiológico).
L1 = 1E-6  # Inductancia en Henrys.
R1 = 0.3  # Resistencia en Ohms.
R2 = 0.3  # Resistencia en Ohms.
C1 = 1.0  # Capacitancia en Faradios.
C2 = 1.2  # Capacitancia en Faradios.

# Elementos del circuito PX SIRA (representa un estado alterado del sistema fisiológico).
L2 = 2E-6  # Inductancia en Henrys.
R3 = 0.6  # Resistencia en Ohms.
R4 = 0.5  # Resistencia en Ohms.
C3 = 0.3  # Capacitancia en Faradios.
C4 = 0.4  # Capacitancia en Faradios.

# Cálculo de la función de transferencia para el sistema NORMAL
a1 = L1 * C1 * C2 * R2  # Coeficiente para el término cúbico del denominador.
b1 = C1 * C2 * R1 * R2 + L1 * C1 + L1 * C2  # Coeficiente para el término cuadrático.
c1 = C1 * R1 + C2 * R1 + C2 * R2  # Coeficiente para el término lineal.
d1 = 1  # Coeficiente constante del denominador.
num1 = [1]  # Numerador de la función de transferencia (constante).
den1 = [a1, b1, c1, d1]  # Denominador de la función de transferencia.
sys1 = control.tf(num1, den1)  # Crea la función de transferencia.
print("Función de transferencia NORMAL:", sys1)

# Cálculo de la función de transferencia para el sistema SIRA
a2 = L2 * C3 * C4 * R4  # Coeficiente para el término cúbico del denominador.
b2 = C3 * C4 * R3 * R4 + L2 * C3 + L2 * C4  # Coeficiente para el término cuadrático.
c2 = C3 * R3 + C4 * R3 + C4 * R4  # Coeficiente para el término lineal.
d2 = 1  # Coeficiente constante del denominador.
num2 = [1]  # Numerador de la función de transferencia (constante).
den2 = [a2, b2, c2, d2]  # Denominador de la función de transferencia.
sys2 = control.tf(num2, den2)  # Crea la función de transferencia.
print("Función de transferencia SIRA:", sys2)

# Respuesta del sistema NORMAL y SIRA a la entrada sinusoidal en 10 segundos
fig4 = plt.figure()  # Crea una figura para graficar.



# Respuesta del sistema NORMAL (primer caso)
ts, Pp1 = control.forced_response(sys1, t, u1, x0)  # Calcula la respuesta.
plt.plot(t, Pp1, '-', color=[0, 0.25, 0.4], label='$P_p(t)$: Caso')  # Gráfica de la respuesta.

# Respuesta del sistema NORMAL (segundo caso)
ts, Pp2 = control.forced_response(sys1, t, u1, x0)  # Calcula la respuesta.
plt.plot(t, Pp2, ':', color='yellow', label='$P_p(t)$: Tratamiento')  # Gráfica de la respuesta.

# Respuesta del sistema SIRA
ts, Pp3 = control.forced_response(sys2, t, u1, x0)  # Calcula la respuesta.
plt.plot(t, Pp3, '-', color='blue', label='$P_p(t)$: Control')  # Gráfica de la respuesta.

# Configuración de la gráfica
 # Activa la rejilla en la gráfica.
plt.xlim(0, 10)  # Limita el eje x de 0 a 10 segundos.
plt.xticks(numpy.arange(0, 11, 1))  # Marca los ejes x cada segundo.
plt.ylim(-1, 1)  # Limita el eje y de -1.2 a 1.2 volts.
plt.xlabel('$t$ $[segundos]$')  # Etiqueta para el eje x.
plt.ylabel('$V(t)$ $[volts]$')  # Etiqueta para el eje y.
plt.title('')  # Título de la gráfica.
plt.legend(bbox_to_anchor=(0.5, -0.28), loc='center', ncol=4)  # Posiciona la leyenda fuera de la gráfica.
plt.show()  # Muestra la gráfica.

# Guardar la gráfica como imagen
fig4.set_size_inches(7, 5)  # Ajusta el tamaño de la figura.
fig4.savefig('python_SIRA.png', dpi=600, bbox_inches='tight')  # Guarda como imagen PNG.
#fig4.savefig('python_sinusoidal.pdf')  # Guarda como PDF (opcional, comentado).
