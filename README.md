[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=Eliaslozadam/Sistema-Rrspiratorio-Sindrome-de-Insuficiencia-Respiratorio-Agudo)

# Sistema Respiratorio Síndrome de Insuficiencia Respiratoria Aguda
## Estudiantes
Bejarano Lozada Elias; Cruz Preciado Brissa Celeste; Vazquez Aldeco Kennia Michelle.
Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: elias.Bejarano201@tectijuana.edu.mx; L21212149@tectijuana.edu.mx; L21212183@tectijuana.edu.mx

## Asignaturas o departmento donde se puede usar la Actividad
Modelado de Sistemas Fisiológicos de Ingeniería Biomédica

## Información general
El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivo general
Diseñar un gemelo digital de un sistema fisiológico que permita identificar las diferencias entre un paciente afectado por una enfermedad (caso) y un individuo saludable (control) para desarrollar un protocolo de tratamiento mediante un sistema de control en lazo cerrado.

## Descripción detallada del sistema
El sistema se basa en un modelo matemático que utiliza un circuito eléctrico equivalente para representar la dinámica del sistema respiratorio afectado por el **Síndrome de Insuficiencia Respiratoria Aguda (SIRA)**. Este modelo incluye componentes como inductancias, resistencias y capacitancias, los cuales reflejan propiedades fisiológicas clave como la inercia del flujo de aire, la resistencia en las vías respiratorias y la elasticidad pulmonar. 

### Ecuaciones principales del sistema
1. **Ecuación de voltaje de entrada**:  Pao(t) = L * di1(t)/dt + R1 * i1(t) + (1/C1) * ∫[i1(t) - i2(t)] dt
2. **Ecuación de continuidad de flujo**:  (1/C1) * ∫[i1(t) - i2(t)] dt = R2 * i2(t) + (1/C2) * ∫i2(t) dt
3. **Ecuación de voltaje de salida**:  Pp(t) = (1/C2) * ∫i2(t) dt

### Características del modelo
- **Entrada (Pao(t))**: Representa la presión aplicada al sistema respiratorio, que inicia el flujo de aire a través del modelo.
- **Salida (Pp(t))**: Define la presión generada en las vías respiratorias profundas después de que el aire pasa por las resistencias y capacitancias del sistema.

### Componentes principales
- **Inductancia (L)**: Representa la inercia al flujo de aire.  
- **Resistencias (R1, R2)**: Modelan las obstrucciones en las vías respiratorias superiores e inferiores.  
- **Capacitancias (C1, C2)**: Reflejan la elasticidad pulmonar, la cual disminuye en pacientes con SIRA.  

### Implementación del modelo
El modelo es implementado mediante herramientas de simulación como **MATLAB** y **Simulink**, permitiendo realizar un análisis comparativo entre pacientes sanos y afectados. Los resultados obtenidos pueden utilizarse para diseñar sistemas de control adaptativos y proponer estrategias de tratamiento.

## Referencias principales

1. M. J. Tobin, *Principles and Practice of Mechanical Ventilation*, 3rd ed. New York, NY, USA: McGraw-Hill Education, 2013.

2. R. M. Kacmarek, J. K. Stoller, and A. J. Heuer, *Egan's Fundamentals of Respiratory Care*, 11th ed. St. Louis, MO, USA: Elsevier, 2016.

