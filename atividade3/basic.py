from lexer import *
from parser import *
from visitor import *
import sys

def main(): 
    if len(sys.argv) != 2:
        sys.exit("Erro: Precisamos de um arquivo como argumento.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()

    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    print(program)
    visitor = TypeCheckVisitor(program)
    print(visitor.symbolTable)
    visitor.typecheck()
    print(visitor.symbolTable)

main()