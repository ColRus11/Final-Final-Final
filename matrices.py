class Matriz:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        """Devuelve una representación en cadena de la matriz."""
        return str(self.data)

    def __repr__(self):
        """Devuelve una representación oficial en cadena de la matriz."""
        return f"Matriz({self.data})"

    @staticmethod
    def transpuesta(matrix):
        """Calcula la transpuesta de una matriz."""
        if isinstance(matrix, Matriz):
            matrix = matrix.data
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        result = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
        return Matriz(result)

    @staticmethod
    def inversa(matrix):
        """Calcula la inversa de una matriz cuadrada usando eliminación gaussiana."""
        if isinstance(matrix, Matriz):
            matrix = matrix.data
        n = len(matrix)
        if n == 0 or any(len(row) != n for row in matrix):
            raise ValueError("La matriz debe ser cuadrada")

        # Crear una copia de la matriz para no modificar la original
        augmented = [[matrix[i][j] for j in range(n)] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

        # Eliminación gaussiana
        for i in range(n):
            # Buscar el pivote máximo en la columna i
            max_pivot = abs(augmented[i][i])
            max_row = i
            for k in range(i + 1, n):
                if abs(augmented[k][i]) > max_pivot:
                    max_pivot = abs(augmented[k][i])
                    max_row = k

            # Si no hay pivote válido, la matriz no es invertible
            if max_pivot < 1e-10:
                raise ValueError("La matriz no es invertible")

            # Intercambiar filas si es necesario
            if max_row != i:
                augmented[i], augmented[max_row] = augmented[max_row], augmented[i]

            # Normalizar la fila del pivote
            pivot = augmented[i][i]
            for j in range(2 * n):
                augmented[i][j] /= pivot

            # Eliminar la columna i en otras filas
            for k in range(n):
                if k != i:
                    factor = augmented[k][i]
                    for j in range(2 * n):
                        augmented[k][j] -= factor * augmented[i][j]

        # Extraer la inversa (parte derecha de la matriz aumentada)
        result = [[augmented[i][j] for j in range(n, 2 * n)] for i in range(n)]
        return Matriz(result)