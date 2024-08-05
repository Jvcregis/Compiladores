from symboltable import *
from exceptions import *

class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

class GenericVisitor(NodeVisitor):
    def __init__(self,tree):
        self.ast = tree

    def traverse(self):
        self.visit(self.ast)
    
    def erro(self,msg):
        raise Exception(msg)

    def undeclaredVariable(self,name):
        raise UndeclaredVariable(name)

    def alreadyDeclaredVariable(self,name):
        raise AlreadyDeclaredVariable(name)

    def varTypeMismatch(self,name, expected, actual):
        raise VarTypeMismatch(name, expected, actual)

    def booleanExpTypeMismatch(self, stmt, actual):
        raise BooleanExpTypeMismatch(stmt, actual)

    def arithExpTypeMismatch(self, left_type, right_type):
        raise ArithExpTypeMismatch(left_type, right_type)

    def relExpTypeMismatch(self, left_type, right_type):
        raise RelExpTypeMismatch(left_type, right_type)

    def visit_Program(self,node):
        for stmt in node.stmts:
            self.visit(stmt)
    def visit_LetStmt(self, node):
        self.visit(node.exp)
    def visit_VarDeclStmt(self,node):
        pass
    def visit_PrintStmt(self,node):
        self.visit(node.exp)
    def visit_InputStmt(self,node):
        pass
    def visit_BlockStmt(self,node):
        for stm in node.body: 
            self.visit(stm)
    def visit_WhileStmt(self,node):
        self.visit(node.cond)
        for stm in node.body: 
            self.visit(stm)
    def visit_IfStmt(self,node):
        self.visit(node.cond)
        for stm in node.body: 
            self.visit(stm)

    def visit_NumExpr(self, node):
        pass
    def visit_IdExpr(self,node):
        pass
    def visit_StringExpr(self, node):
        pass    
    def visit_GreaterThanExpr(self,node):
        self.visit(node.left)
        self.visit(node.right)
    def visit_GreaterThanEqualsExpr(self,node):
        self.visit(node.left)
        self.visit(node.right)
    def visit_LessThanExpr(self,node):
        self.visit(node.left)
        self.visit(node.right)
    def visit_LessThanEqualsExpr(self,node):
        self.visit(node.left)
        self.visit(node.right)
    def visit_EqualsExpr(self,node):
        self.visit(node.left)
        self.visit(node.right)
    def visit_NotEqualsExpr(self,node):
        self.visit(node.left)
        self.visit(node.right)
    def visit_UnaryPlusExpr(self,node):
        self.visit(node.exp)
    def visit_UnaryMinusExpr(self,node):
        self.visit(node.exp)    
    def visit_SumExpr(self,node):
        self.visit(node.left)
        self.visit(node.right)
    def visit_SubExpr(self,node):
        self.visit(node.left)
        self.visit(node.right)
    def visit_MulExpr(self,node):
        self.visit(node.left)
        self.visit(node.right)
    def visit_DivExpr(self,node):
        self.visit(node.left)
        self.visit(node.right)

        
class TypeCheckVisitor(GenericVisitor):
    def __init__(self, tree):
        super().__init__(tree)
        self.symbolTable = ScopedSymbolTable(
            scope_name='program',
            scope_level=1
        )

    def typecheck(self):
        self.traverse()
    
    def BOOLEAN(self):
        return self.symbolTable.lookup('BOOLEAN')
    def INT(self):
        return self.symbolTable.lookup('INT')
    def STRING(self):
        return self.symbolTable.lookup('STRING')

    def visit_InputStmt(self, node):
        input_id = node.id
        
        # Verificar se a variável que vai receber o input já foi declarada
        if self.symbolTable.lookup(input_id) is None:
            self.undeclaredVariable(input_id)

    def visit_LetStmt(self, node):
        let_id = node.id
        let_exp = node.exp
        
        
        # Verificar se a variável que vai receber o valor já foi declarada
        symbol = self.symbolTable.lookup(let_id)
        if symbol is None:
            self.undeclaredVariable(let_id)
        else:              
            # Verificar se o tipo condiz com o tipo declarado da variável
            let_exp_type = self.visit(let_exp)
            if symbol.type != let_exp_type:
                self.varTypeMismatch(symbol.name, str(symbol.type), str(let_exp_type))
        
    def visit_VarDeclStmt(self, node):
        decl_id = node.id
        
        # Verificar se a variável a ser declarada já existe NO MESMO ESCOPO!
        if self.symbolTable.lookup(decl_id, True) is None:
            decl_type = self.symbolTable.lookup(node.type)
            var_symbol = VarSymbol(decl_id, decl_type)
            self.symbolTable.insert(decl_id, var_symbol)
        else:
            self.alreadyDeclaredVariable(decl_id)
            

    def visit_WhileStmt(self, node):
        cond = node.cond
        body = node.body
        
        # Verificar se o tipo da cond é booleano
        cond_type = self.visit(cond)
        if cond_type != self.BOOLEAN():
            self.booleanExpTypeMismatch("WHILE", str(cond_type))
        else:
            # Visitando todos os statements do bloco WHILE
            for stmt in body:
                self.visit(stmt)

    def visit_IfStmt(self, node):
        cond = node.cond
        body = node.body
        
        # Verificar se o tipo da cond é booleano
        cond_type = self.visit(cond)
        if cond_type != self.BOOLEAN():
            self.booleanExpTypeMismatch("IF", str(cond_type))
        else:
            # Visitando todos os statements do bloco IF
            for stmt in body:
                self.visit(stmt)

    def visit_BlockStmt(self, node):
        name = node.name
        body = node.body
        
        # Entrando em um novo bloco precisamos definir um novo escopo
        new_scope = ScopedSymbolTable(name, self.symbolTable.scope_level + 1, self.symbolTable)
        
        # Temporariamente entrando no escopo
        self.symbolTable = new_scope
        
        # Visitando todos os statements do bloco
        for stmt in body:
            self.visit(stmt)
            
        self.symbolTable = self.symbolTable.enclosing_scope
        

    def visit_NumExpr(self, node):
        return self.INT()

    def visit_StringExpr(self, node):
        return self.STRING()

    def visit_IdExpr(self, node):
        symbol = self.symbolTable.lookup(node.id)
        if symbol is None:
            self.undeclaredVariable(node.id)
        else:
            return symbol.type

    def visit_SumExpr(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if left != self.INT() or right != self.INT():
            self.arithExpTypeMismatch(str(left), str(right))
            
        return self.INT()
    
    def visit_SubExpr(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if left != self.INT() or right != self.INT():
            self.arithExpTypeMismatch(str(left), str(right))
            
        return self.INT()
    
    def visit_DivExpr(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if left != self.INT() or right != self.INT():
            self.arithExpTypeMismatch(str(left), str(right))
            
        return self.INT()
    
    def visit_MulExpr(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if left != self.INT() or right != self.INT():
            self.arithExpTypeMismatch(str(left), str(right))
            
        return self.INT()
    
    def visit_GreaterThanExpr(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if left != self.INT() or right != self.INT():
            self.relExpTypeMismatch(str(left), str(right))
            
        return self.BOOLEAN()

    def visit_GreaterThanEqualsExpr(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if left != self.INT() or right != self.INT():
            self.relExpTypeMismatch(str(left), str(right))
            
        return self.BOOLEAN()

    def visit_LessThanEqualsExpr(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if left != self.INT() or right != self.INT():
            self.relExpTypeMismatch(str(left), str(right))
            
        return self.BOOLEAN()

    def visit_LessThanExpr(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if left != self.INT() or right != self.INT():
            self.relExpTypeMismatch(str(left), str(right))
            
        return self.BOOLEAN()

    def visit_EqualsExpr(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if left != right: # Verificar se funciona
            self.relExpTypeMismatch(str(left), str(right))
        
        return self.BOOLEAN()

    def visit_NotEqualsExpr(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if left != right: # Verificar se funciona
            self.relExpTypeMismatch(str(left), str(right))
        
        return self.BOOLEAN()
