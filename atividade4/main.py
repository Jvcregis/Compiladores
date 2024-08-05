from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser
import sys

class ArithmeticVisitor:
    def __init__(self) -> None:
        self.memory = {}
        
    def visit(self, ctx):
        if isinstance(ctx, ArithmeticParser.ProgramContext):
            return self.visitProgram(ctx)
        elif isinstance(ctx, ArithmeticParser.StatementContext):
            return self.visitStatement(ctx)
        elif isinstance(ctx, ArithmeticParser.AssignmentContext):
            return self.visitAssignment(ctx)
        elif isinstance(ctx, ArithmeticParser.ExprContext):
            return self.visitExpr(ctx)
        elif isinstance(ctx, ArithmeticParser.TermContext):
            return self.visitTerm(ctx)
        elif isinstance(ctx, ArithmeticParser.FactorContext):
            return self.visitFactor(ctx)
        
    def visitProgram(self, ctx):
        results = []
        for statement in ctx.statement():
            results.append(self.visit(statement))
        return results
    
    def visitStatement(self, ctx):
        return self.visit(ctx.getChild(0))
    
    def visitAssignment(self, ctx):
        var_name = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitExpr(self, ctx):
        result = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            op = ctx.getChild(i * 2 - 1).getText()
            if op == '+':
                result += self.visit(ctx.term(i))
            elif op == '-':
                result -= self.visit(ctx.term(i))
            else:
                raise Exception(f"Símbolo {op} não pode ser usado em uma expressão.")
        return result

    def visitTerm(self, ctx):
        result = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(i * 2 - 1).getText()
            if op == '*':
                result *= self.visit(ctx.factor(i))
            elif op == '/':
                next_factor = self.visit(ctx.factor(i))
                if next_factor != 0:
                    result /= next_factor
                else:
                    raise Exception("Division by zero")  # Tratamento de erro para divisão por zero
        return result

    def visitFactor(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.VAR():
            var_name = ctx.VAR().getText()
            if var_name in self.memory:
                return self.memory[var_name]
            else:
                raise Exception(f"Undefined variable: {var_name}")
        else:
            return self.visit(ctx.expr())


def main():
    visitor = ArithmeticVisitor()
    print("REPL de Aritmética. Digite 'exit' para sair.")
    
    while True:
        try:
            expression = input(">>> ")
            if expression.strip().lower() == 'exit':
                print("Saindo do REPL...")
                break

            lexer = ArithmeticLexer(InputStream(expression))
            stream = CommonTokenStream(lexer)
            parser = ArithmeticParser(stream)
            tree = parser.program()
            result = visitor.visit(tree)
            if result is not None:
                print("Resultado:", result)
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == '__main__':
    main()