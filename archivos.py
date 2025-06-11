class Archivos:
    @staticmethod
    def leer_archivo(nombre):
        """Lee un archivo de texto y devuelve su contenido como string."""
        try:
            with open(nombre, 'r', encoding='utf-8') as f:
                return f.read()
        except IOError as e:
            raise ValueError(f"Error al leer {nombre}: {str(e)}")

    @staticmethod
    def escribir_archivo(nombre, contenido):
        """Escribe un string en un archivo de texto."""
        try:
            with open(nombre, 'w', encoding='utf-8') as f:
                f.write(str(contenido))
        except IOError as e:
            raise ValueError(f"Error al escribir {nombre}: {str(e)}")

    @staticmethod
    def leer_csv(archivo):
        """Lee un archivo CSV y devuelve una lista de listas de valores numéricos."""
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                lines = [line.strip().split(',') for line in f.readlines() if line.strip()]
                if not lines:
                    raise ValueError("Archivo CSV vacío")
                num_cols = len(lines[0])
                if not all(len(row) == num_cols for row in lines):
                    raise ValueError("Filas con diferente número de columnas")
                result = []
                for row in lines:
                    try:
                        result.append([float(x) for x in row])
                    except ValueError:
                        raise ValueError(f"Datos no numéricos en {archivo}")
                return result
        except IOError as e:
            raise ValueError(f"Error al leer CSV {archivo}: {str(e)}")

    @staticmethod
    def escribir_csv(archivo, datos):
        """Escribe una lista de listas en un archivo CSV."""
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                for row in datos:
                    f.write(','.join(str(x) for x in row) + '\n')
        except IOError as e:
            raise ValueError(f"Error al escribir CSV {archivo}: {str(e)}")