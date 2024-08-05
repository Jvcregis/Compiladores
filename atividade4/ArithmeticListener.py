# Generated from Arithmetic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArithmeticParser import ArithmeticParser
else:
    from ArithmeticParser import ArithmeticParser

# This class defines a complete listener for a parse tree produced by ArithmeticParser.
class ArithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by ArithmeticParser#program.
    def enterProgram(self, ctx:ArithmeticParser.ProgramContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#program.
    def exitProgram(self, ctx:ArithmeticParser.ProgramContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#statement.
    def enterStatement(self, ctx:ArithmeticParser.StatementContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#statement.
    def exitStatement(self, ctx:ArithmeticParser.StatementContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#assignment.
    def enterAssignment(self, ctx:ArithmeticParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#assignment.
    def exitAssignment(self, ctx:ArithmeticParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#expr.
    def enterExpr(self, ctx:ArithmeticParser.ExprContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#expr.
    def exitExpr(self, ctx:ArithmeticParser.ExprContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#term.
    def enterTerm(self, ctx:ArithmeticParser.TermContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#term.
    def exitTerm(self, ctx:ArithmeticParser.TermContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#factor.
    def enterFactor(self, ctx:ArithmeticParser.FactorContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#factor.
    def exitFactor(self, ctx:ArithmeticParser.FactorContext):
        pass



del ArithmeticParser