# Generated from Arithmetic.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,3,1,20,8,1,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,5,3,29,8,3,10,3,12,3,32,9,3,1,4,1,4,1,4,5,4,37,8,4,10,4,12,4,
        40,9,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,48,8,5,1,5,0,0,6,0,2,4,6,8,10,
        0,2,1,0,1,2,1,0,3,4,49,0,13,1,0,0,0,2,19,1,0,0,0,4,21,1,0,0,0,6,
        25,1,0,0,0,8,33,1,0,0,0,10,47,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,
        0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,20,3,
        4,2,0,18,20,3,6,3,0,19,17,1,0,0,0,19,18,1,0,0,0,20,3,1,0,0,0,21,
        22,5,8,0,0,22,23,5,9,0,0,23,24,3,6,3,0,24,5,1,0,0,0,25,30,3,8,4,
        0,26,27,7,0,0,0,27,29,3,8,4,0,28,26,1,0,0,0,29,32,1,0,0,0,30,28,
        1,0,0,0,30,31,1,0,0,0,31,7,1,0,0,0,32,30,1,0,0,0,33,38,3,10,5,0,
        34,35,7,1,0,0,35,37,3,10,5,0,36,34,1,0,0,0,37,40,1,0,0,0,38,36,1,
        0,0,0,38,39,1,0,0,0,39,9,1,0,0,0,40,38,1,0,0,0,41,48,5,5,0,0,42,
        48,5,8,0,0,43,44,5,6,0,0,44,45,3,6,3,0,45,46,5,7,0,0,46,48,1,0,0,
        0,47,41,1,0,0,0,47,42,1,0,0,0,47,43,1,0,0,0,48,11,1,0,0,0,5,15,19,
        30,38,47
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "<INVALID>", 
                     "'('", "')'", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MUL", "DIV", "INT", 
                      "LPAREN", "RPAREN", "VAR", "ASSIGN", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expr = 3
    RULE_term = 4
    RULE_factor = 5

    ruleNames =  [ "program", "statement", "assignment", "expr", "term", 
                   "factor" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    MUL=3
    DIV=4
    INT=5
    LPAREN=6
    RPAREN=7
    VAR=8
    ASSIGN=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.StatementContext,i)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ArithmeticParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.statement()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 352) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ArithmeticParser.AssignmentContext,0)


        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ArithmeticParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 19
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ArithmeticParser.VAR, 0)

        def ASSIGN(self):
            return self.getToken(ArithmeticParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ArithmeticParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(ArithmeticParser.VAR)
            self.state = 22
            self.match(ArithmeticParser.ASSIGN)
            self.state = 23
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.TermContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.PLUS)
            else:
                return self.getToken(ArithmeticParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MINUS)
            else:
                return self.getToken(ArithmeticParser.MINUS, i)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ArithmeticParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.term()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 26
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 27
                self.term()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.FactorContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MUL)
            else:
                return self.getToken(ArithmeticParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.DIV)
            else:
                return self.getToken(ArithmeticParser.DIV, i)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ArithmeticParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.factor()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 34
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 35
                self.factor()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ArithmeticParser.INT, 0)

        def VAR(self):
            return self.getToken(ArithmeticParser.VAR, 0)

        def LPAREN(self):
            return self.getToken(ArithmeticParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ArithmeticParser.RPAREN, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ArithmeticParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(ArithmeticParser.INT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(ArithmeticParser.VAR)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(ArithmeticParser.LPAREN)
                self.state = 44
                self.expr()
                self.state = 45
                self.match(ArithmeticParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





