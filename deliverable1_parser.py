# Generated from deliverable1_parser.g4 by ANTLR 4.13.2
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
        4,1,15,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,39,8,1,1,2,1,2,1,3,
        1,3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,1,4,1,4,1,4,5,4,54,8,4,10,4,
        12,4,57,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,69,8,5,1,
        5,0,0,6,0,2,4,6,8,10,0,2,1,0,7,8,1,0,9,11,77,0,13,1,0,0,0,2,38,1,
        0,0,0,4,40,1,0,0,0,6,42,1,0,0,0,8,50,1,0,0,0,10,68,1,0,0,0,12,14,
        3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,
        16,17,1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,20,5,2,0,0,20,21,5,1,
        0,0,21,39,3,4,2,0,22,23,5,2,0,0,23,24,5,7,0,0,24,25,5,1,0,0,25,39,
        3,4,2,0,26,27,5,2,0,0,27,28,5,8,0,0,28,29,5,1,0,0,29,39,3,4,2,0,
        30,31,5,2,0,0,31,32,5,9,0,0,32,33,5,1,0,0,33,39,3,4,2,0,34,35,5,
        2,0,0,35,36,5,10,0,0,36,37,5,1,0,0,37,39,3,4,2,0,38,19,1,0,0,0,38,
        22,1,0,0,0,38,26,1,0,0,0,38,30,1,0,0,0,38,34,1,0,0,0,39,3,1,0,0,
        0,40,41,3,6,3,0,41,5,1,0,0,0,42,47,3,8,4,0,43,44,7,0,0,0,44,46,3,
        8,4,0,45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,
        7,1,0,0,0,49,47,1,0,0,0,50,55,3,10,5,0,51,52,7,1,0,0,52,54,3,10,
        5,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,9,
        1,0,0,0,57,55,1,0,0,0,58,69,5,3,0,0,59,69,5,4,0,0,60,69,5,2,0,0,
        61,69,5,5,0,0,62,69,5,6,0,0,63,69,5,13,0,0,64,65,5,14,0,0,65,66,
        3,4,2,0,66,67,5,15,0,0,67,69,1,0,0,0,68,58,1,0,0,0,68,59,1,0,0,0,
        68,60,1,0,0,0,68,61,1,0,0,0,68,62,1,0,0,0,68,63,1,0,0,0,68,64,1,
        0,0,0,69,11,1,0,0,0,5,15,38,47,55,68
    ]

class deliverable1_parser ( Parser ):

    grammarFileName = "deliverable1_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "<INVALID>", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "EQ", "VAR", "INT", "FLOAT", "CHAR", 
                      "BOOL", "PLUS", "MINUS", "MULT", "DIV", "REMAINDER", 
                      "WS", "ARRAY", "LPAREN", "RPAREN" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_additiveExpr = 3
    RULE_multiplicativeExpr = 4
    RULE_primary = 5

    ruleNames =  [ "start", "statement", "expr", "additiveExpr", "multiplicativeExpr", 
                   "primary" ]

    EOF = Token.EOF
    EQ=1
    VAR=2
    INT=3
    FLOAT=4
    CHAR=5
    BOOL=6
    PLUS=7
    MINUS=8
    MULT=9
    DIV=10
    REMAINDER=11
    WS=12
    ARRAY=13
    LPAREN=14
    RPAREN=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(deliverable1_parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliverable1_parser.StatementContext)
            else:
                return self.getTypedRuleContext(deliverable1_parser.StatementContext,i)


        def getRuleIndex(self):
            return deliverable1_parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = deliverable1_parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
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
                if not (_la==2):
                    break

            self.state = 17
            self.match(deliverable1_parser.EOF)
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

        def VAR(self):
            return self.getToken(deliverable1_parser.VAR, 0)

        def EQ(self):
            return self.getToken(deliverable1_parser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(deliverable1_parser.ExprContext,0)


        def PLUS(self):
            return self.getToken(deliverable1_parser.PLUS, 0)

        def MINUS(self):
            return self.getToken(deliverable1_parser.MINUS, 0)

        def MULT(self):
            return self.getToken(deliverable1_parser.MULT, 0)

        def DIV(self):
            return self.getToken(deliverable1_parser.DIV, 0)

        def getRuleIndex(self):
            return deliverable1_parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = deliverable1_parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(deliverable1_parser.VAR)
                self.state = 20
                self.match(deliverable1_parser.EQ)
                self.state = 21
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(deliverable1_parser.VAR)
                self.state = 23
                self.match(deliverable1_parser.PLUS)
                self.state = 24
                self.match(deliverable1_parser.EQ)
                self.state = 25
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.match(deliverable1_parser.VAR)
                self.state = 27
                self.match(deliverable1_parser.MINUS)
                self.state = 28
                self.match(deliverable1_parser.EQ)
                self.state = 29
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.match(deliverable1_parser.VAR)
                self.state = 31
                self.match(deliverable1_parser.MULT)
                self.state = 32
                self.match(deliverable1_parser.EQ)
                self.state = 33
                self.expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.match(deliverable1_parser.VAR)
                self.state = 35
                self.match(deliverable1_parser.DIV)
                self.state = 36
                self.match(deliverable1_parser.EQ)
                self.state = 37
                self.expr()
                pass


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

        def additiveExpr(self):
            return self.getTypedRuleContext(deliverable1_parser.AdditiveExprContext,0)


        def getRuleIndex(self):
            return deliverable1_parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = deliverable1_parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.additiveExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliverable1_parser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(deliverable1_parser.MultiplicativeExprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(deliverable1_parser.PLUS)
            else:
                return self.getToken(deliverable1_parser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(deliverable1_parser.MINUS)
            else:
                return self.getToken(deliverable1_parser.MINUS, i)

        def getRuleIndex(self):
            return deliverable1_parser.RULE_additiveExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)




    def additiveExpr(self):

        localctx = deliverable1_parser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.multiplicativeExpr()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 43
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 44
                self.multiplicativeExpr()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(deliverable1_parser.PrimaryContext)
            else:
                return self.getTypedRuleContext(deliverable1_parser.PrimaryContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(deliverable1_parser.MULT)
            else:
                return self.getToken(deliverable1_parser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(deliverable1_parser.DIV)
            else:
                return self.getToken(deliverable1_parser.DIV, i)

        def REMAINDER(self, i:int=None):
            if i is None:
                return self.getTokens(deliverable1_parser.REMAINDER)
            else:
                return self.getToken(deliverable1_parser.REMAINDER, i)

        def getRuleIndex(self):
            return deliverable1_parser.RULE_multiplicativeExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)




    def multiplicativeExpr(self):

        localctx = deliverable1_parser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.primary()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0):
                self.state = 51
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 52
                self.primary()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(deliverable1_parser.INT, 0)

        def FLOAT(self):
            return self.getToken(deliverable1_parser.FLOAT, 0)

        def VAR(self):
            return self.getToken(deliverable1_parser.VAR, 0)

        def CHAR(self):
            return self.getToken(deliverable1_parser.CHAR, 0)

        def BOOL(self):
            return self.getToken(deliverable1_parser.BOOL, 0)

        def ARRAY(self):
            return self.getToken(deliverable1_parser.ARRAY, 0)

        def LPAREN(self):
            return self.getToken(deliverable1_parser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(deliverable1_parser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(deliverable1_parser.RPAREN, 0)

        def getRuleIndex(self):
            return deliverable1_parser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = deliverable1_parser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primary)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(deliverable1_parser.INT)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(deliverable1_parser.FLOAT)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.match(deliverable1_parser.VAR)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.match(deliverable1_parser.CHAR)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 62
                self.match(deliverable1_parser.BOOL)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 63
                self.match(deliverable1_parser.ARRAY)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 64
                self.match(deliverable1_parser.LPAREN)
                self.state = 65
                self.expr()
                self.state = 66
                self.match(deliverable1_parser.RPAREN)
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





