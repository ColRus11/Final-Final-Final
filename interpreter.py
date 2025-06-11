from antlr4 import *
from ColRusLexer import ColRusLexer
from ColRusParser import ColRusParser
from ColRusVisitor import ColRusVisitor
from matematicas import Matematicas
from graficas import graficar
from regresion_lineal import regresion_lineal
from matrices import Matriz
from archivos import Archivos
from red_neuronal import MLP, kmeans

class ColRusInterpreter(ColRusVisitor):
    def __init__(self, debug=True):
        self.debug = debug
        self.variables = {}
        self.functions = {}
        self.env = {
            "Matriz": Matriz,
            "Matematicas": Matematicas,
            "graficar": graficar,
            "regresion_lineal": regresion_lineal,
            "Archivos": Archivos,
            "MLP": MLP,
            "kmeans": kmeans
        }
        self.local_envs = [{}]

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitStatement(self, ctx):
        if isinstance(ctx, ColRusParser.GraficarStmtContext):
            return self.visitGraficarStmt(ctx)
        return self.visitChildren(ctx)

    def visitDefStmt(self, ctx):
        func_name = ctx.ID().getText()
        params = [param.getText() for param in ctx.params().ID()] if ctx.params() else []
        self.functions[func_name] = ("user_defined", params, ctx.block())
        return None

    def visitExpressionStmt(self, ctx):
        var_name = ctx.ID().getText()
        index = self.visit(ctx.expression(0)) if ctx.LBRACK() else None
        expr_idx = 1 if ctx.LBRACK() else 0
        value = (
            self.visit(ctx.expression(expr_idx)) if ctx.expression(expr_idx)
            else self.visit(ctx.functionCall()) if ctx.functionCall()
            else None
        )
        if value is None:
            raise ValueError(f"No se asignó valor a la variable {var_name} en la línea {ctx.start.line}")
        if index is not None:
            if var_name not in self.variables or not isinstance(self.variables[var_name], (list, Matriz)):
                raise ValueError(f"Variable {var_name} no es un arreglo o matriz en la línea {ctx.start.line}")
            self.variables[var_name][index] = value
        else:
            self.variables[var_name] = value
        return None

    def visitPrintStmt(self, ctx):
        values = [self.visit(expr) for expr in ctx.expression()]
        print(*values)
        return None

    def visitReturnStmt(self, ctx):
        return self.visit(ctx.expression())

    def visitFunctionCallStmt(self, ctx):
        return self.visit(ctx.functionCall())

    def visitForStmt(self, ctx):
        var_name = ctx.ID().getText()
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))
        if start is None or end is None:
            raise ValueError(f"Rango inválido en bucle for: start={start}, end={end}")
        self.local_envs.append({})
        for i in range(int(start), int(end) + 1):
            self.local_envs[-1][var_name] = i
            self.visit(ctx.block())
        self.local_envs.pop()
        return None

    def visitRepeatStmt(self, ctx):
        var_name = ctx.ID().getText()
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))
        if start is None or end is None:
            raise ValueError(f"Rango inválido en bucle repeat: start={start}, end={end}")
        self.local_envs.append({})
        for i in range(int(start), int(end) + 1):
            self.local_envs[-1][var_name] = i
            self.visit(ctx.block())
        self.local_envs.pop()
        return None

    def visitIfStmt(self, ctx):
        condition = self.visit(ctx.expression())
        if condition:
            return self.visit(ctx.block(0))
        return self.visit(ctx.block(1)) if ctx.block(1) else None

    def visitWhileStmt(self, ctx):
        self.local_envs.append({})
        while self.visit(ctx.expression()):
            self.visit(ctx.block())
        self.local_envs.pop()
        return None

    def visitMlpStmt(self, ctx):
        model_name = ctx.ID(0).getText() if isinstance(ctx.ID(), list) else ctx.ID().getText()
        if ctx.CREAR_MLP():
            layers = self.visit(ctx.expression(0)) if ctx.expression() else []
            if isinstance(layers, Matriz):
                layers = layers.data
            elif isinstance(layers, list):
                layers = [int(x) for x in layers]
            self.variables[model_name] = MLP.crear_mlp(layers)
        elif ctx.ENTRENAR_MLP():
            data = self.visit(ctx.expression(0)) if ctx.expression(0) else []
            if isinstance(data, Matriz):
                data = data.data
            elif isinstance(data, list):
                data = [[float(x) for x in row] for row in data]
            labels = self.visit(ctx.expression(1)) if ctx.expression(1) else []
            if isinstance(labels, Matriz):
                labels = labels.data
            elif isinstance(labels, list):
                labels = [[float(x) for x in row] for row in labels]
            epochs = int(self.visit(ctx.expression(2)))
            lr = float(self.visit(ctx.expression(3)))
            MLP.entrenar_mlp(self.variables[model_name], data, labels, epochs, lr)
        elif ctx.PREDECIR_MLP():
            result_name = ctx.ID(0).getText() if ctx.EQUALS() else None
            model_name = ctx.ID(1).getText() if ctx.EQUALS() else model_name
            input_data = self.visit(ctx.expression(0)) if ctx.expression(0) else []
            if isinstance(input_data, Matriz):
                input_data = input_data.data
            elif isinstance(input_data, list):
                input_data = [float(x) for x in input_data]
            prediction = MLP.predecir_mlp(self.variables[model_name], input_data)
            self.variables[result_name or f"{model_name}_pred"] = prediction
        return None

    def visitMemberAccess(self, ctx):
        module_name = ctx.ID(0).getText()
        method_name = ctx.ID(1).getText()
        args = self.visit(ctx.args()) if ctx.args() else []
        module = self.env.get(module_name)
        if not module:
            raise ValueError(f"Módulo o clase no encontrada: {module_name} en la línea {ctx.start.line}")
        method = getattr(module, method_name, None)
        if not method:
            raise ValueError(f"Método no encontrado: {module_name}.{method_name} en la línea {ctx.start.line}")
        try:
            result = method(*args)
            if isinstance(result, list) and all(isinstance(row, list) for row in result):
                result = Matriz(result)
            return result
        except TypeError as e:
            raise ValueError(f"Error en la llamada a {module_name}.{method_name}: {str(e)} en la línea {ctx.start.line}")

    def visitKmeansStmt(self, ctx):
        id_name = ctx.ID().getText()
        points = self.visit(ctx.expression(0))
        k = self.visit(ctx.expression(1))
        points = points.data if isinstance(points, Matriz) else points
        result = kmeans(points, int(k))
        self.variables[id_name] = result
        return None

    def visitExpression(self, ctx):
        return self.visit(ctx.relationalExpr())

    def visitRelationalExpr(self, ctx):
        left = self.visit(ctx.additiveExpr(0))
        if ctx.getChildCount() == 1:
            return left
        right = self.visit(ctx.additiveExpr(1))
        op = ctx.getChild(1).getText()
        ops = {
            '<': lambda x, y: x < y,
            '>': lambda x, y: x > y,
            '<=': lambda x, y: x <= y,
            '>=': lambda x, y: x >= y,
            '==': lambda x, y: x == y,
            '!=': lambda x, y: x != y
        }
        if op not in ops:
            raise ValueError(f"Operador desconocido: {op}")
        return ops[op](left, right)

    def visitAdditiveExpr(self, ctx):
        exprs = [self.visit(ctx.multiplicativeExpr(i)) for i in range(len(ctx.multiplicativeExpr()))]
        if len(exprs) == 1:
            return exprs[0]
        result = exprs[0]
        for i, op in enumerate(ctx.getChild(2*i + 1).getText() for i in range(len(exprs) - 1)):
            right = exprs[i + 1]
            if op == '+':
                if isinstance(result, Matriz) and isinstance(right, Matriz):
                    result = Matriz(result.data + right.data)
                elif isinstance(result, (int, float)) and isinstance(right, (int, float)):
                    result += right
                else:
                    raise ValueError(f"Tipos incompatibles para suma: {type(result)}, {type(right)}")
            elif op == '-':
                if isinstance(result, (int, float)) and isinstance(right, (int, float)):
                    result -= right
                else:
                    raise ValueError(f"Tipos incompatibles para resta: {type(result)}, {type(right)}")
        return result

    def visitArgs(self, ctx):
        return [self.visit(expr) for expr in ctx.expression()]

    def visitMultiplicativeExpr(self, ctx):
        exprs = [self.visit(ctx.powerExpr(i)) for i in range(len(ctx.powerExpr()))]
        if len(exprs) == 1:
            return exprs[0]
        result = exprs[0]
        for i, op in enumerate(ctx.getChild(2*i + 1).getText() for i in range(len(exprs) - 1)):
            right = exprs[i + 1]
            if op == '*':
                result *= right
            elif op == '/':
                result /= right
            elif op == '%':
                result %= right
        return result

    def visitPowerExpr(self, ctx):
        exprs = [self.visit(ctx.unaryExpr(i)) for i in range(len(ctx.unaryExpr()))]
        if len(exprs) == 1:
            return exprs[0]
        result = exprs[0]
        for right in exprs[1:]:
            result **= right
        return result

    def visitUnaryExpr(self, ctx):
        if ctx.SUB():
            return -self.visit(ctx.unaryExpr())
        if ctx.BANG():
            return not self.visit(ctx.unaryExpr())
        return self.visit(ctx.primaryExpr())

    def visitPrimaryExpr(self, ctx):
        if ctx.functionCall():
            return self.visit(ctx.functionCall())
        if ctx.memberAccess():
            return self.visit(ctx.memberAccess())
        return self.visit(ctx.atom())

    def visitAtom(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]
        if ctx.ID():
            var_name = ctx.ID().getText()
            for env in reversed(self.local_envs):
                if var_name in env:
                    return env[var_name]
            if var_name in self.variables:
                value = self.variables[var_name]
            elif var_name in self.env:
                value = self.env[var_name]
            else:
                raise ValueError(f"Variable {var_name} no definida en la línea {ctx.start.line}")
            if ctx.LBRACK():
                index = self.visit(ctx.expression())
                value = value.data if isinstance(value, Matriz) else value
                return value[index]
            return value
        if ctx.matrixExpr():
            return self.visit(ctx.matrixExpr())
        if ctx.expression():
            return self.visit(ctx.expression())
        if ctx.memberAccess():
            return self.visit(ctx.memberAccess())
        raise ValueError(f"Átomo inválido en la línea {ctx.start.line}: {ctx.getText()}")

    def visitMatrixExpr(self, ctx):
        matrix_ctx = ctx.matrix()
        if matrix_ctx:
            if matrix_ctx.row():
                rows = [self.visitRow(row_ctx) for row_ctx in matrix_ctx.row()]
                return Matriz(rows)
            exprs = [self.visit(expr) for expr in matrix_ctx.expression()]
            return exprs
        return Matriz([])

    def visitRow(self, ctx):
        return [self.visit(expr) for expr in ctx.expression()]

    def visitFunctionCall(self, ctx):
        func_name = ctx.ID().getText()
        args = self.visit(ctx.args()) if ctx.args() else []
        func = self.env.get(func_name)
        if not func:
            raise ValueError(f"Función {func_name} no encontrada en la línea {ctx.start.line}")
        if isinstance(func, tuple) and func[0] == "user_defined":
            params, block = func[1], func[2]
            if len(args) != len(params):
                raise ValueError(f"Se esperaban {len(params)} argumentos, se recibieron {len(args)} en la línea {ctx.start.line}")
            self.local_envs.append({})
            for param, arg in zip(params, args):
                self.local_envs[-1][param] = arg
            result = None
            for stmt in block.statement():
                result = self.visit(stmt)
                if result is not None and isinstance(stmt, ColRusParser.ReturnStmtContext):
                    break
            self.local_envs.pop()
            return result
        if callable(func):
            if func_name in ["graficar", "regresion_lineal", "kmeans"]:
                args = [arg.data if isinstance(arg, Matriz) else arg for arg in args]
            return func(*args)
        raise ValueError(f"{func_name} no es invocable en la línea {ctx.start.line}")

    def visitGraficarStmt(self, ctx):
        var_names = [ctx.ID(i).getText() for i in range(len(ctx.ID()))]
        plot_type = ctx.STRING().getText()[1:-1] if ctx.STRING() else "scatter"
        data_sets = []
        for var_name in var_names:
            data = self.variables.get(var_name)
            if not data:
                raise ValueError(f"Variable {var_name} no encontrada")
            data = data.data if isinstance(data, Matriz) else data
            data_sets.append(data)
        for data in data_sets:
            if not all(isinstance(p, list) and len(p) == 2 for p in data):
                if all(isinstance(x, (int, float)) for x in data):
                    data[:] = [[i, x] for i, x in enumerate(data)]
                else:
                    raise ValueError(f"Datos inválidos para {plot_type}: {data}")
        symbols = ['o', '*', '+', 'x']
        if len(data_sets) > len(symbols):
            raise ValueError("Demasiados conjuntos de datos para los símbolos disponibles")
        graficar(data_sets, plot_type=plot_type, width=50, height=25, symbols=symbols[:len(data_sets)])
        return None

def main():
    try:
        import sys
        filename = sys.argv[1] if len(sys.argv) > 1 else "ejemplo.coru"
        input_stream = FileStream(filename, encoding='utf-8')
        lexer = ColRusLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ColRusParser(stream)
        tree = parser.program()
        # print(f"[DEBUG] Árbol de sintaxis:\n{Trees.toStringTree(tree, None, parser)}")
        # print(f"[DEBUG] Tokens: {[token.text for token in stream.tokens]}")
        interpreter = ColRusInterpreter(debug=True)
        interpreter.visit(tree)
    except Exception as e:
        print(f"Error durante la ejecución: {str(e)}")

if __name__ == '__main__':
    main()