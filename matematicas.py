class Matematicas:
    PI = 3.141592653589793
    E = 2.718281828459045

    @staticmethod
    def _normalize_angle(x):
        """Normaliza un ángulo a [-π, π] para mejorar la precisión en funciones trigonométricas."""
        two_pi = 2 * Matematicas.PI
        x = x % two_pi
        if x > Matematicas.PI:
            x -= two_pi
        elif x < -Matematicas.PI:
            x += two_pi
        return x

    @staticmethod
    def sin(x):
        """Calcula el seno de x (en radianes) usando una serie de Taylor."""
        x = Matematicas._normalize_angle(x)  # Normalizar a [-π, π]
        result = x
        term = x
        for i in range(1, 15):  # Más términos para mayor precisión
            term *= -x * x / ((2 * i) * (2 * i + 1))
            if abs(term) < 1e-15:  # Criterio de convergencia
                break
            result += term
        return result

    @staticmethod
    def cos(x):
        """Calcula el coseno de x (en radianes) usando una serie de Taylor."""
        x = Matematicas._normalize_angle(x)  # Normalizar a [-π, π]
        result = 1
        term = 1
        for i in range(1, 15):
            term *= -x * x / ((2 * i - 1) * (2 * i))
            if abs(term) < 1e-15:
                break
            result += term
        return result

    @staticmethod
    def tan(x):
        """Calcula la tangente de x (en radianes)."""
        c = Matematicas.cos(x)
        if abs(c) < 1e-10:
            raise ValueError("Tangente indefinida")
        return Matematicas.sin(x) / c

    @staticmethod
    def asin(x):
        """Calcula el arcseno de x en [-1, 1]."""
        if abs(x) > 1:
            raise ValueError("Dominio inválido para arcseno")
        if abs(x) < 1e-10:
            return x
        result = x
        term = x
        for i in range(1, 15):
            term *= (2 * i - 1) * x * x / (2 * i)
            next_term = term / (2 * i + 1)
            if abs(next_term) < 1e-15:
                break
            result += next_term
        return result

    @staticmethod
    def acos(x):
        """Calcula el arccoseno de x en [-1, 1]."""
        if abs(x) > 1:
            raise ValueError("Dominio inválido para arccos")
        return Matematicas.PI / 2 - Matematicas.asin(x)

    @staticmethod
    def atan(x):
        """Calcula el arctangente de x."""
        if abs(x) < 1e-10:
            return x
        if x > 1:
            return Matematicas.PI / 2 - Matematicas.atan(1 / x)
        elif x < -1:
            return -Matematicas.PI / 2 - Matematicas.atan(1 / x)
        result = x
        term = x
        for i in range(1, 15):
            term *= -x * x
            next_term = term / (2 * i + 1)
            if abs(next_term) < 1e-15:
                break
            result += next_term
        return result

    @staticmethod
    def sqrt(x):
        """Calcula la raíz cuadrada de x usando el método de Newton."""
        if x < 0:
            raise ValueError("Raíz cuadrada de un número negativo no está definida")
        if x == 0:
            return 0
        z = x / 2.0  # Estimación inicial
        for _ in range(10):
            if abs(z * z - x) < 1e-10:
                break
            z = (z + x / z) / 2
        return z

    @staticmethod
    def log(x):
        """Calcula el logaritmo natural de x."""
        if x <= 0:
            raise ValueError("Dominio inválido para logaritmo")
        if x == 1:
            return 0
        # Normalizar x para mejorar la convergencia
        k = 0
        while x > 2:
            x /= Matematicas.E
            k += 1
        while x < 0.5:
            x *= Matematicas.E
            k -= 1
        z = (x - 1) / (x + 1)
        result = 0
        for i in range(1, 20, 2):
            term = (z ** i) / i
            if abs(term) < 1e-15:
                break
            result += term
        return 2 * result + k

    @staticmethod
    def exp(x):
        """Calcula e^x usando una serie de Taylor."""
        if x > 10:  # Evitar desbordamiento
            raise ValueError("Argumento demasiado grande para exp")
        result = 1
        term = 1
        for i in range(1, 20):
            term *= x / i
            if abs(term) < 1e-15:
                break
            result += term
        return result

    @staticmethod
    def pow(x, y):
        """Calcula x^y usando log y exp."""
        if x == 0 and y <= 0:
            raise ValueError("Potencia indefinida")
        if x < 0:
            raise ValueError("Base negativa no soportada")
        return Matematicas.exp(y * Matematicas.log(x))

    @staticmethod
    def abs(x):
        """Calcula el valor absoluto de x."""
        return x if x >= 0 else -x

    @staticmethod
    def sinh(x):
        """Calcula el seno hiperbólico de x."""
        return (Matematicas.exp(x) - Matematicas.exp(-x)) / 2

    @staticmethod
    def cosh(x):
        """Calcula el coseno hiperbólico de x."""
        return (Matematicas.exp(x) + Matematicas.exp(-x)) / 2

    @staticmethod
    def tanh(x):
        """Calcula la tangente hiperbólica de x."""
        ex = Matematicas.exp(x)
        e_minusx = Matematicas.exp(-x)
        if abs(ex + e_minusx) < 1e-10:
            raise ValueError("Tangente hiperbólica indefinida")
        return (ex - e_minusx) / (ex + e_minusx)