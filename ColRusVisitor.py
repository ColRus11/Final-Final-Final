# Generated from ColRus.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ColRusParser import ColRusParser
else:
    from ColRusParser import ColRusParser

# This class defines a complete generic visitor for a parse tree produced by ColRusParser.

class ColRusVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ColRusParser#program.
    def visitProgram(self, ctx:ColRusParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#statement.
    def visitStatement(self, ctx:ColRusParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#expressionStmt.
    def visitExpressionStmt(self, ctx:ColRusParser.ExpressionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#printStmt.
    def visitPrintStmt(self, ctx:ColRusParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#defStmt.
    def visitDefStmt(self, ctx:ColRusParser.DefStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#forStmt.
    def visitForStmt(self, ctx:ColRusParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#repeatStmt.
    def visitRepeatStmt(self, ctx:ColRusParser.RepeatStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#ifStmt.
    def visitIfStmt(self, ctx:ColRusParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#whileStmt.
    def visitWhileStmt(self, ctx:ColRusParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#mlpStmt.
    def visitMlpStmt(self, ctx:ColRusParser.MlpStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#kmeansStmt.
    def visitKmeansStmt(self, ctx:ColRusParser.KmeansStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#functionCallStmt.
    def visitFunctionCallStmt(self, ctx:ColRusParser.FunctionCallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#returnStmt.
    def visitReturnStmt(self, ctx:ColRusParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#block.
    def visitBlock(self, ctx:ColRusParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#params.
    def visitParams(self, ctx:ColRusParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#expression.
    def visitExpression(self, ctx:ColRusParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#relationalExpr.
    def visitRelationalExpr(self, ctx:ColRusParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:ColRusParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:ColRusParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#powerExpr.
    def visitPowerExpr(self, ctx:ColRusParser.PowerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#unaryExpr.
    def visitUnaryExpr(self, ctx:ColRusParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:ColRusParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#atom.
    def visitAtom(self, ctx:ColRusParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#memberAccess.
    def visitMemberAccess(self, ctx:ColRusParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#functionCall.
    def visitFunctionCall(self, ctx:ColRusParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#args.
    def visitArgs(self, ctx:ColRusParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#matrixExpr.
    def visitMatrixExpr(self, ctx:ColRusParser.MatrixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#matrix.
    def visitMatrix(self, ctx:ColRusParser.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#row.
    def visitRow(self, ctx:ColRusParser.RowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ColRusParser#graficarStmt.
    def visitGraficarStmt(self, ctx:ColRusParser.GraficarStmtContext):
        return self.visitChildren(ctx)



del ColRusParser