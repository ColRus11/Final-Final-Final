ColRus Programming Language
ColRus is a simple, educational programming language designed for numerical computations, machine learning, and data visualization. It features a clear syntax inspired by Spanish keywords, making it accessible for Spanish-speaking learners. ColRus supports matrix operations, neural networks, file I/O, plotting, and mathematical functions, with integrations for machine learning (e.g., MLP) and clustering (e.g., K-means).
Features

Basic Programming Constructs:

Variables, assignments, and expressions.
Control structures: if, while, for (para), and repeat (repetir).
User-defined functions with parameters and return statements.
Print statements (muestre) for output.


Matrix Operations:

Matrix literals (e.g., [[1, 2], [3, 4]]).
Indexing (e.g., matriz[0][1]) and assignments.
Built-in matrix class (Matriz) for operations like addition.


Machine Learning:

Multilayer Perceptron (MLP) for neural networks:
Create (crear_mlp), train (entrenar_mlp), and predict (predecir_mlp).
Example: XOR problem solving with a [2, 6, 1] architecture.


K-means clustering (kmeans) for unsupervised learning.


Mathematical Functions:

Integration with Matematicas module:
Trigonometric: sin, cos, tan, asin, acos, atan.
Hyperbolic: sinh, cosh, tanh.
Other: sqrt, exp, log, pow, abs.
Constants: PI, E.




File I/O:

Read CSV files with Archivos.leer_csv("filename") for data loading.


Data Visualization:

Plotting via Graficas module:
Scatter plots and other plot types (e.g., graficar datos, "scatter").
Supports multiple datasets with customizable symbols.




Linear Algebra:

Linear regression via regresion_lineal module (basic implementation).



Syntax Overview
ColRus uses Spanish keywords and follows a straightforward syntax. Below are key constructs:
Variables and Assignments
x <- 10; entero
matriz <- [[0, 1], [2, 3]]
matriz[0][1] <- 5; // Modifica el elemento en fila 0, columna 1

Control Flow
if x > 5 then
    muestre "Mayor que 5";
sino
    muestre "Menor o igual a 5";
fin.

para i desde 0 hasta 10 entonces
    muestre i;
fin.

mientras x < 0 entonces
    x <- x + 1;
fin.

Functions
definir funcion suma(a, b entero) entonces:
    retornar a + b.
fin.
suma(3, 4);
fin.

Neural Networks (MLP)
capas <- [2, 6, 1];
modelo crear_mlp ( capas );
entradas <- [[0, 0], [0, 1], [1, 0], [1, 1]];
salidas <- [[0], [1], [1], [0]];
modelo entrenar_mlp ( entradas, salidas, 10000, 0.01 );
para i desde 0 hasta 3 entonces
    pred <- modelo predecir_mlp ( entradas[i] );
    muestre "Predicción:", pred[0], "Esperado:", salidas[i][0];
fin.

Plotting
datos <- [[1, 2], [2, 4], [3, 6]];
graficar datos, "scatter";

K-Means Clustering
puntos <- [[1, 2], [2, 3], [10, 12], [11, 10]];
k <- 2;
clusters <- kmeans(puntos, k);

File I/O
datos <- Archivos.leer_csv("xor_data.txt");

Getting Started
Requirements

Python 3.7+
ANTLR4 Python runtime (pip install antlr4-python3-runtime)
Project files in ~/Documentos/Grok:
interpreter.py: ColRus interpreter
Colrus.g4: Grammar file
red_neuronal.py: MLP and K-means
matematicas.py: Math functions
archivos.py: File I/O
graficas.py: Plotting
matrices.py: Matrix operations
regresion_lineal.py: Linear regression



Setup

Clone or set up the project directory:mkdir -p ~/Documentos/Grok
cd ~/Documentos/Grok


Generate ANTLR parser (if not already done):antlr4 -Dlanguage=Python3 -visitor -no-listener ColRus.g4


Ensure all Python modules (red_neuronal.py, matematicas.py, etc.) are in ~/Documentos/Grok.

Running a ColRus Program

Create a .coru file (e.g., ejemplomatrices.coru):matriz <- [[1, 2], [3, 4]];
muestre "Matriz:", matriz;


Run the interpreter with a hardcoded filename in main:
Edit interpreter.py’s main function to set filename = "ejemplomatrices.coru".
Run:python3 interpreter.py





Note: The current main function doesn’t support command-line arguments (python3 interpreter.py ejemplomatrices.coru) without import sys. To enable this, modify main to:
def main():
    try:
        import sys
        filename = sys.argv[1] if len(sys.argv) > 1 else "ejemplo.coru"
        input_stream = FileStream(filename, encoding='utf-8')
        lexer = ColRusLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ColRusParser(stream)
        tree = parser.program()
        interpreter = ColRusInterpreter(debug=True)
        interpreter.visit(tree)
    except Exception as e:
        print(f"Error durante la ejecución: {str(e)}")

Then run:
python3 interpreter.py ejemplomatrices.coru

Example: Solving XOR with MLP
capas <- [2, 6, 1];
modelo crear_mlp ( capas );
entradas <- [[0, 0], [0, 1], [1, 0], [1, 1]];
salidas <- [[0], [1], [1], [0]];
modelo entrenar_mlp ( entradas, salidas, 10000, 0.01 );
para i desde 0 hasta 3 entonces
    entrada <- entradas[i];
    pred <- modelo predecir_mlp ( entrada );
    pred_val <- pred[0];
    esperado <- salidas[i];
    esperado_val <- esperado[0];
    muestre "Entrada:", entrada, "Predicción:", pred_val, "Esperado:", esperado_val;
fin.

Output:
Entrada: [0, 0] Predicción: ~0.01 Esperado: 0
Entrada: [0, 1] Predicción: ~0.99 Esperado: 1
Entrada: [1, 0] Predicción: ~0.99 Esperado: 1
Entrada: [1, 1] Predicción: ~0.01 Esperado: 0

Limitations

No support for dynamic command-line arguments without modifying main (unless sys is allowed).
File I/O (Archivos.leer_csv) requires a specific CSV format (implementation details unavailable).
Plotting (Graficas) is ASCII-based, limited to simple visualizations.
MLP training may require hyperparameter tuning for complex problems.
No advanced error recovery in the interpreter.

Future Improvements

Add command-line argument support (python3 interpreter.py file.coru) with minimal imports.
Enhance Matematicas for more numerical stability in large inputs.
Expand Graficas for advanced plotting (e.g., Matplotlib integration).
Support more machine learning algorithms (e.g., SVM, decision trees).

Contributing
To contribute:

Modify ColRus.g4 for new syntax.
Update interpreter.py for new features.
Add examples in .coru files.
Test with python3 interpreter.py.

Contact the project maintainer for collaboration.
License
This project is for educational purposes and has no formal license. Use and modify freely for learning.
