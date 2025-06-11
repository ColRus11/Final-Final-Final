ColRus (.coru) – Lenguaje DSL para Aprendizaje Profundo y Computación Numérica
Descripción
ColRus es un lenguaje de dominio específico (DSL) diseñado para computación numérica, aprendizaje automático y visualización de datos. Está implementado en Python utilizando ANTLR4 y el patrón Visitor, dependiendo únicamente de la biblioteca estándar de Python y el runtime de ANTLR4, sin bibliotecas externas. Su sintaxis, basada en palabras clave en español, permite realizar operaciones matemáticas, manipular matrices, implementar estructuras de control y entrenar modelos de aprendizaje automático como perceptrones y clustering K-means. Es ideal para estudiantes, investigadores y entusiastas que deseen explorar programación y aprendizaje automático de manera accesible.
Introducción
ColRus es un lenguaje educativo que combina simplicidad con potencia, enfocado en tareas numéricas y de aprendizaje automático. Soporta operaciones aritméticas, matrices, visualización de datos y modelos como perceptrones multicapa (MLP) y clustering, todo con una sintaxis clara en español. Ejecutado desde la consola, es perfecto para aprender conceptos de programación y experimentar con algoritmos de machine learning sin dependencias externas complejas.
Instalación
Para usar ColRus, necesitas Python 3 y el runtime de ANTLR4. Sigue estos pasos:

Instalar Python 3: Descarga desde python.org.
Instalar ANTLR4: Instala el runtime con:pip install antlr4-python3-runtime


Clonar el Repositorio: Obtén el código desde GitHub:git clone https://github.com/ColRus11/Final-Final-Final.git


Generar Parser: En el directorio del proyecto, genera los archivos del parser:cd Final-Final-Final
antlr4 -Dlanguage=Python3 -visitor -no-listener ColRus.g4


Ejecutar un Programa: Usa el intérprete para ejecutar un archivo .coru:python3 interpreter.py ejemplo.coru



Asegúrate de que los archivos interpreter.py, ColRus.g4, red_neuronal.py, matematicas.py, archivos.py, graficas.py, matrices.py y regresion_lineal.py estén en el directorio Final-Final-Final.
Características
ColRus ofrece un conjunto robusto de funcionalidades para computación numérica y aprendizaje automático, todas implementadas sin bibliotecas externas más allá de Python y ANTLR4:

Operaciones Matemáticas: Aritméticas (suma, resta, multiplicación, división, módulo, potencia), trigonométricas (sin, cos, tan, etc.), logarítmicas y exponenciales.
Matrices: Declaración, operaciones (suma, resta, multiplicación, inversa, transpuesta) y acceso a elementos.
Estructuras de Control: Condicionales (si, sino), bucles (para, mientras, repetir) y funciones definidas por el usuario.
Visualización de Datos: Gráficos de dispersión, líneas, barras y pastel, renderizados en ASCII.
Entrada/Salida de Archivos: Lectura y escritura de archivos CSV para cargar y guardar datos.
Aprendizaje Automático: Regresión lineal, perceptrón multicapa (MLP) con pérdida de entropía cruzada, y clustering K-means.

Reglas de Sintaxis

Instrucciones: Terminan con ;.
Asignaciones: x = 5;.
Comentarios: // Esto es un comentario.
Identificadores: No pueden comenzar con números.
Bloques: Delimitados por {}.
Palabras Clave: En español (si, para, mientras, definir, muestre, etc.).

Funciones Disponibles
ColRus integra módulos internos (Matematicas, Matriz, Archivos, Graficas, MLP, kmeans, regresion_lineal) accesibles mediante notación de punto (e.g., Matematicas.sin). A continuación, un cuadro con las funciones principales, su descripción y cómo llamarlas:



Módulo
Función
Descripción
Llamada de Ejemplo



Matematicas
sin(x)
Calcula el seno de x (radianes) usando serie de Taylor.
Matematicas.sin(1.57);



cos(x)
Calcula el coseno de x (radianes).
Matematicas.cos(0);



tan(x)
Calcula la tangente de x (radianes).
Matematicas.tan(0.785);



asin(x)
Calcula el arcseno de x en [-1, 1].
Matematicas.asin(0.5);



acos(x)
Calcula el arccoseno de x en [-1, 1].
Matematicas.acos(0.5);



atan(x)
Calcula el arctangente de x.
Matematicas.atan(1);



sqrt(x)
Calcula la raíz cuadrada de x (método de Newton).
Matematicas.sqrt(16);



log(x)
Calcula el logaritmo natural de x.
Matematicas.log(2.718);



exp(x)
Calcula ( e^x ) usando serie de Taylor.
Matematicas.exp(1);



pow(x, y)
Calcula ( x^y ) usando log y exp.
Matematicas.pow(2, 3);



abs(x)
Calcula el valor absoluto de x.
Matematicas.abs(-5);



sinh(x)
Calcula el seno hiperbólico de x.
Matematicas.sinh(1);



cosh(x)
Calcula el coseno hiperbólico de x.
Matematicas.cosh(1);



tanh(x)
Calcula la tangente hiperbólica de x.
Matematicas.tanh(1);


Matriz
inversa(m)
Calcula la inversa de una matriz cuadrada.
m = [[1,2],[3,4]]; Matriz.inversa(m);



transpuesta(m)
Calcula la transpuesta de una matriz.
Matriz.transpuesta(m);


Archivos
leer_csv("archivo.txt")
Lee un archivo CSV como lista de listas.
datos = Archivos.leer_csv("data.txt");


Graficas
graficar(datos, tipo)
Genera un gráfico (dispersión, líneas, barras, pastel) en ASCII.
graficar [[1,2],[3,4]], "scatter"();


MLP
crear_mlp(capas)
Crea un perceptrón multicapa con capas especificadas.
modelo crear_mlp([2,6,1]);



entrenar_mlp(modelo, datos, etiquetas, épocas, lr)
Entrena el MLP con entropía cruzada.
entrenar_mlp(modelo, [[0,0],[1,1]], [[0],[1]], 10000, 0.01);



predecir_mlp(modelo, entrada)
Predice con el MLP entrenado.
pred = predecir_mlp(modelo, [0,1]);


kmeans
kmeans(puntos, k)
Realiza clustering K-means con k clústeres.
clusters = kmeans([[1,2],[3,4]], 2);


regresion_lineal
regresion_lineal(puntos)
Calcula pendiente e intercepto de una regresión lineal.
coef = regresion_lineal([[1,2],[3,4]]);


Uso
ColRus se ejecuta mediante archivos .coru procesados por interpreter.py. Ejemplos:
1. Operaciones Matemáticas
x = 3.14;
y = Matematicas.sin(x) + Matematicas.cos(x);
muestre y;

2. Matrices
A = [[1,2],[3,4]];
B = [[5,6],[7,8]];
C = A + B;
D = Matriz.inversa(C);
muestre C, D;

3. Estructuras de Control
para i desde 0 hasta 5 {
    muestre i;
}

4. Funciones Definidas
definir funcion suma(a, b) {
    retornar a + b;
}
resultado = suma(3, 4);
muestre resultado;

5. Visualización de Datos
puntos = [[1,2],[3,4],[5,6]];
graficar puntos, "scatter"();

6. Regresión Lineal
puntos = Archivos.leer_csv("puntos_regresion.txt");
coef = regresion_lineal(puntos);
m = coef[0];
b = coef[1];
muestre m, b;

7. MLP para XOR
capas = [2, 6, 1];
modelo crear_mlp ( capas );
entradas = [[0, 0], [0, 1], [1, 0], [1, 1]];
salidas = [[0], [1], [1], [0]];
modelo entrenar_mlp ( entradas, salidas, 20000, 0.01 );
para i desde 0 hasta 3 {
    entrada = entradas[i];
    pred = modelo predecir_mlp ( entrada );
    pred_val = pred[0];
    esperado = salidas[i];
    esperado_val = esperado[0];
    muestre "Entrada:", entrada, "Predicción:", pred_val, "Esperado:", esperado_val;
}

8. Clustering K-means
```colrus
puntos = [[1,2],[3,4],[5,6],[7,8]];
clusters = kmeans(puntos, 2);
muestre clusters;

Sin Bibliotecas Externas
ColRus es completamente autocontenido, utilizando solo la biblioteca estándar de Python y ANTLR4 para el análisis sintáctico. Esto asegura un entorno ligero y portátil, sin dependencias de bibliotecas externas como NumPy o Matplotlib.
Contribuyendo
