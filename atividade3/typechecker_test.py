from astnodes import *
from exceptions import *
from lexer import *
from parser import *
from symboltable import *
from visitor import *
import pytest 

def test1(): 
    file = "data/error_alreadydeclaredvar.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(AlreadyDeclaredVariable) as e:
        visitor.typecheck()
    assert e.value.args[0] == 'y'

def test2(): 
    file = "data/error_block1.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(AlreadyDeclaredVariable) as e:
        visitor.typecheck()
    assert e.value.args[0] == 'i'

def test3(): 
    file = "data/error_block2.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(UndeclaredVariable) as e:
        visitor.typecheck()
    assert e.value.args[0] == 'x'

 
def test4(): 
    file = "data/error_block3.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(VarTypeMismatch) as e:
        visitor.typecheck()
    assert 'b' == e.value.args[0]
    assert '<BOOLEAN>' == e.value.args[1]
    assert '<INT>' == e.value.args[2]
    
def test5(): 
    file = "data/error_ifcondition.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(BooleanExpTypeMismatch) as e:
        visitor.typecheck()
    assert 'IF' == e.value.args[0]
    assert '<INT>' == e.value.args[1]
    
def test6(): 
    file = "data/error_whilecondition.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(BooleanExpTypeMismatch) as e:
        visitor.typecheck()
    assert 'WHILE' == e.value.args[0]
    assert '<STRING>' == e.value.args[1]
    
def test7(): 
    file = "data/error_typemismatch_bool1.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(VarTypeMismatch) as e:
        visitor.typecheck()
    assert 'b' == e.value.args[0]
    assert '<BOOLEAN>' == e.value.args[1]
    assert '<STRING>' == e.value.args[2]
    
def test8(): 
    file = "data/error_typemismatch_bool2.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(VarTypeMismatch) as e:
        visitor.typecheck()
    assert 'b' == e.value.args[0]
    assert '<BOOLEAN>' == e.value.args[1]
    assert '<INT>' == e.value.args[2]
    
def test9(): 
    file = "data/error_typemismatch_int1.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(VarTypeMismatch) as e:
        visitor.typecheck()
    assert 'y' == e.value.args[0]
    assert '<INT>' == e.value.args[1]
    assert '<STRING>' == e.value.args[2]
    
def test10(): 
    file = "data/error_typemismatch_int2.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(VarTypeMismatch) as e:
        visitor.typecheck()
    assert 'y' == e.value.args[0]
    assert '<INT>' == e.value.args[1]
    assert '<BOOLEAN>' == e.value.args[2]

def test11(): 
    file = "data/error_typemismatch_str1.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(VarTypeMismatch) as e:
        visitor.typecheck()
    assert 's' == e.value.args[0]
    assert '<STRING>' == e.value.args[1]
    assert '<BOOLEAN>' == e.value.args[2]
    
def test12(): 
    file = "data/error_typemismatch_str2.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(VarTypeMismatch) as e:
        visitor.typecheck()
    assert 's' == e.value.args[0]
    assert '<STRING>' == e.value.args[1]
    assert '<INT>' == e.value.args[2]

def test13(): 
    file = "data/error_undeclaredvar.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    with pytest.raises(UndeclaredVariable) as e:
        visitor.typecheck()
    assert 'y' == e.value.args[0]

def test14(): 
    file = "data/ok_block.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    visitor.typecheck()
    assert str(visitor.symbolTable.lookup("i").type) == "<INT>"
    assert str(visitor.symbolTable.lookup("b").type) == "<BOOLEAN>"
    assert str(visitor.symbolTable.lookup("s").type) == "<STRING>"

def test15(): 
    file = "data/ok_compare.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    visitor.typecheck()
    assert str(visitor.symbolTable.lookup("num").type) == "<INT>"

def test16(): 
    file = "data/ok_fib.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    visitor.typecheck()
    assert str(visitor.symbolTable.lookup("nums").type) == "<INT>"
    assert str(visitor.symbolTable.lookup("a").type) == "<INT>"
    assert str(visitor.symbolTable.lookup("b").type) == "<INT>"
    assert str(visitor.symbolTable.lookup("c").type) == "<INT>"
    assert str(visitor.symbolTable.lookup("d").type) == "<INT>"
    assert str(visitor.symbolTable.lookup("e").type) == "<STRING>"
    assert str(visitor.symbolTable.lookup("f").type) == "<BOOLEAN>"

def test17(): 
    file = "data/ok_nested.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    visitor.typecheck()
    assert str(visitor.symbolTable.lookup("num").type) == "<INT>"
    assert str(visitor.symbolTable.lookup("c1").type) == "<BOOLEAN>"
    assert str(visitor.symbolTable.lookup("c2").type) == "<BOOLEAN>"
    assert str(visitor.symbolTable.lookup("c3").type) == "<BOOLEAN>"

def test18(): 
    file = "data/ok_test.basic"
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    program = parser.parse()
    visitor = TypeCheckVisitor(program)
    visitor.typecheck()
    assert str(visitor.symbolTable.lookup("y").type) == "<INT>"
    assert str(visitor.symbolTable.lookup("x").type) == "<INT>"
    assert str(visitor.symbolTable.lookup("m").type) == "<INT>"
    assert str(visitor.symbolTable.lookup("b").type) == "<BOOLEAN>"
    assert str(visitor.symbolTable.lookup("s").type) == "<STRING>"
    assert str(visitor.symbolTable.lookup("z").type) == "<INT>"
    assert str(visitor.symbolTable.lookup("w").type) == "<INT>"
    assert str(visitor.symbolTable.lookup("u").type) == "<STRING>"

