# ColRus (.coru) – Lenguaje DSL para Aprendizaje Profundo

**ColRus** es un lenguaje de dominio específico (DSL) diseñado desde cero para facilitar el desarrollo de algoritmos y procesos de *Deep Learning*. Implementado en Python utilizando ANTLR4 y el patrón de diseño *Visitor*, ColRus permite realizar operaciones matemáticas, manipular matrices, controlar flujo de ejecución y construir modelos de aprendizaje automático, todo desde una sintaxis personalizada y ejecutable en consola.

---

## Características principales

### ● Operaciones aritméticas y trigonométricas

Permite:

- Suma, resta, multiplicación, división, módulo (`%`)
- Potencia (`^`), raíces, exponenciales
- Funciones como `sin(x)`, `cos(x)`, `tan(x)`, `log(x)`

### ● Operaciones con matrices

- Declaración y asignación de matrices
- Suma, resta, multiplicación matricial
- Inversa, transpuesta y otras funciones lineales

### ● Estructuras de control

- **Condicionales:**
  ```coru
  if (condicion) {
      // bloque verdadero
  } else {
      // bloque falso
  }
  ```
- **Bucle for:**
  ```coru
  for(i = 0; i < 10; i = i + 1) {
      // instrucciones
  }
  ```
- **Bucle while:**
  ```coru
  while (condicion) {
      // instrucciones
  }
  ```

### ● Declaración de funciones

```coru
funcion nombreFuncion(param1, param2) {
    resultado = param1 + param2;
    return resultado;
}
```

- Se llama como: `nombreFuncion(4, 5);`

### ● Gráficos de datos

- Representación visual con funciones integradas:
  ```coru
  graficar(x, y);
  graficar_multi(x, y1, y2);
  graficar_barras(nombres, valores);
  graficar_pastel(nombres, valores);
  ```

### ● Manejo de archivos

- Lectura: `datos = leer("archivo.txt");`
- Escritura: `escribir("salida.txt", datos);`

### ● Aprendizaje automático

- **Regresión lineal:**
  ```coru
  regresion_lineal("puntos.txt");
  ```
- **Perceptrón multicapa:**
  ```coru
  entrenar_perceptron("xor_data.txt");
  ```
- **Agrupamiento (Clustering):**
  ```coru
  clustering("datos.txt", k);
  ```

---

## Reglas sintácticas generales

- Todas las instrucciones terminan con `;`
- Asignaciones: `x = 5;`
- Comentarios de línea: `// esto es un comentario`
- Identificadores no deben iniciar con números

---

## Ejecución del lenguaje

1. **Requisitos:** Python 3, ANTLR4
2. **Ejecutar un archivo ColRus:**
   ```bash
   python3 interpreter.py archivo.coru
   ```

---

## Estructura del proyecto

- `interpreter.py`: Intérprete principal del lenguaje
- `ColRus.g4`: Gramática personalizada en ANTLR4
- Archivos `.coru`: Programas de ejemplo y pruebas funcionales

---

## Ejemplos de uso

### Suma y funciones matemáticas

```coru
x = 10;
y = 2;
z = x^y + sin(x);
```

### Trabajo con matrices

```coru
A = [[1,2],[3,4]];
B = [[5,6],[7,8]];
C = A + B;
D = inversa(C);
```

### Entrenar perceptrón para XOR

```coru
entrenar_perceptron("xor_data.txt");
```

---
