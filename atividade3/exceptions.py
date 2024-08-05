class TypeCheckError(Exception):
    pass

class UndeclaredVariable(TypeCheckError):
    """Exceção que deve ser lançada quando o typechecker encontrar uma variável não declarada.

    Atributos:
        name -- nome da variável que não foi declarada
    """

    def __init__(self, name):
        self.name = name
        self.message = "Variável não declarada: %s" % name

class AlreadyDeclaredVariable(TypeCheckError):
    """Exceção que deve ser lançada quando o typechecker encontrar uma declaração de variável que já foi declarada antes no mesmo escopo.

    Atributos:
        name -- nome da variável que não foi declarada
    """

    def __init__(self, name):
        self.name = name
        self.message = "Variável já foi declarada antes: %s" % name

class VarTypeMismatch(TypeCheckError):
    """Exceção lançada quando uma variável é de tipo X mas recebe valor de tipo Y!=X.

    Attributes:
        name -- nome da variável
        expected_type -- tipo de dados esperado
        actual_type -- tipo do valor que foi atribuído à variável
    """

    def __init__(self, name, expected_type, actual_type):
        self.name = name
        self.expected_type = expected_type
        self.actual_type = actual_type
        self.message = 'Variável ' + name + ' espera por valor de tipo ' + expected_type + ', mas recebeu valor de tipo ' + actual_type

class BooleanExpTypeMismatch(TypeCheckError):
    """Exceção lançada quando uma expressão deveria ser de tipo BOOLEAN mas recebe valor de tipo diferente.

    Attributes:
        statement_type -- tipo de statement (IF ou WHILE)
        actual_type -- tipo do valor que foi atribuído à expressão
    """

    def __init__(self, statement_type, actual_type):
        self.statement_type = statement_type
        self.actual_type = actual_type
        self.message = 'Condição do ' + statement_type + ' deveria ser BOOLEAN, ao invés de ' + actual_type

class ArithExpTypeMismatch(TypeCheckError):
    """Exceção lançada quando uma expressão aritmética envolve expressões de tipo diferente de inteiros.

    Attributes:
        left_type -- tipo do lado esquerdo da expressão
        right_type -- tipo do lado direito da expressão
    """

    def __init__(self, left_type, right_type):
        self.left_type = left_type
        self.right_type = right_type
        self.message = 'Operação aritmética deveria envolver apenas inteiros, ao invés de ' + left_type + ' & ' + right_type

class RelExpTypeMismatch(TypeCheckError):
    """Exceção lançada quando uma expressão relacional envolve expressões de tipos diferentes.

    Attributes:
        left_type -- tipo do lado esquerdo da expressão
        right_type -- tipo do lado direito da expressão
    """

    def __init__(self, left_type, right_type):
        self.left_type = left_type
        self.right_type = right_type
        self.message = 'Operação relacional deveria envolver apenas elementos do mesmo tipo, ao invés de ' + left_type + ' & ' + right_type
