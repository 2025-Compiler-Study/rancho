# Generated from CalcPlus.g4 by ANTLR 4.13.1
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
        4,1,21,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,1,1,1,1,1,
        1,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,2,4,2,39,8,2,11,2,12,2,
        40,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,57,
        8,3,3,3,59,8,3,1,4,4,4,62,8,4,11,4,12,4,63,1,4,1,4,1,5,1,5,1,5,1,
        5,1,6,1,6,5,6,74,8,6,10,6,12,6,77,9,6,1,6,1,6,1,6,0,1,2,7,0,2,4,
        6,8,10,12,0,3,1,0,1,2,1,0,3,4,1,0,11,16,82,0,14,1,0,0,0,2,24,1,0,
        0,0,4,38,1,0,0,0,6,58,1,0,0,0,8,61,1,0,0,0,10,67,1,0,0,0,12,71,1,
        0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,1,1,0,0,0,17,18,6,1,-1,0,18,
        25,5,20,0,0,19,25,5,21,0,0,20,21,5,5,0,0,21,22,3,2,1,0,22,23,5,6,
        0,0,23,25,1,0,0,0,24,17,1,0,0,0,24,19,1,0,0,0,24,20,1,0,0,0,25,34,
        1,0,0,0,26,27,10,5,0,0,27,28,7,0,0,0,28,33,3,2,1,6,29,30,10,4,0,
        0,30,31,7,1,0,0,31,33,3,2,1,5,32,26,1,0,0,0,32,29,1,0,0,0,33,36,
        1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,3,1,0,0,0,36,34,1,0,0,0,37,
        39,3,6,3,0,38,37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,
        0,41,42,1,0,0,0,42,43,5,0,0,1,43,5,1,0,0,0,44,45,5,21,0,0,45,46,
        5,7,0,0,46,47,3,2,1,0,47,48,5,8,0,0,48,59,1,0,0,0,49,50,5,9,0,0,
        50,51,5,5,0,0,51,52,3,10,5,0,52,53,5,6,0,0,53,56,3,12,6,0,54,55,
        5,10,0,0,55,57,3,12,6,0,56,54,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,
        0,58,44,1,0,0,0,58,49,1,0,0,0,59,7,1,0,0,0,60,62,3,6,3,0,61,60,1,
        0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,65,
        66,5,0,0,1,66,9,1,0,0,0,67,68,3,2,1,0,68,69,7,2,0,0,69,70,3,2,1,
        0,70,11,1,0,0,0,71,75,5,17,0,0,72,74,3,6,3,0,73,72,1,0,0,0,74,77,
        1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,0,
        78,79,5,18,0,0,79,13,1,0,0,0,8,24,32,34,40,56,58,63,75
    ]

class CalcPlusParser ( Parser ):

    grammarFileName = "CalcPlus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'('", "')'", 
                     "'='", "';'", "'if'", "'else'", "'=='", "'!='", "'>'", 
                     "'>='", "'<'", "'<='", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "INT", 
                      "VAR" ]

    RULE_calc0 = 0
    RULE_expr = 1
    RULE_calc1 = 2
    RULE_stmt = 3
    RULE_calc2 = 4
    RULE_cond = 5
    RULE_block = 6

    ruleNames =  [ "calc0", "expr", "calc1", "stmt", "calc2", "cond", "block" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    WS=19
    INT=20
    VAR=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Calc0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CalcPlusParser.ExprContext,0)


        def EOF(self):
            return self.getToken(CalcPlusParser.EOF, 0)

        def getRuleIndex(self):
            return CalcPlusParser.RULE_calc0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalc0" ):
                listener.enterCalc0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalc0" ):
                listener.exitCalc0(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalc0" ):
                return visitor.visitCalc0(self)
            else:
                return visitor.visitChildren(self)




    def calc0(self):

        localctx = CalcPlusParser.Calc0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_calc0)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.expr(0)
            self.state = 15
            self.match(CalcPlusParser.EOF)
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


        def getRuleIndex(self):
            return CalcPlusParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcPlusParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcPlusParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcPlusParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcPlusParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcPlusParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcPlusParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcPlusParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(CalcPlusParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcPlusParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcPlusParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcPlusParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalcPlusParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcPlusParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = CalcPlusParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 18
                self.match(CalcPlusParser.INT)
                pass
            elif token in [21]:
                localctx = CalcPlusParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                self.match(CalcPlusParser.VAR)
                pass
            elif token in [5]:
                localctx = CalcPlusParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(CalcPlusParser.T__4)
                self.state = 21
                self.expr(0)
                self.state = 22
                self.match(CalcPlusParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 32
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = CalcPlusParser.MulDivContext(self, CalcPlusParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 27
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 28
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = CalcPlusParser.AddSubContext(self, CalcPlusParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 30
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        self.expr(5)
                        pass

             
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Calc1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CalcPlusParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcPlusParser.StmtContext)
            else:
                return self.getTypedRuleContext(CalcPlusParser.StmtContext,i)


        def getRuleIndex(self):
            return CalcPlusParser.RULE_calc1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalc1" ):
                listener.enterCalc1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalc1" ):
                listener.exitCalc1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalc1" ):
                return visitor.visitCalc1(self)
            else:
                return visitor.visitChildren(self)




    def calc1(self):

        localctx = CalcPlusParser.Calc1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_calc1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 37
                self.stmt()
                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9 or _la==21):
                    break

            self.state = 42
            self.match(CalcPlusParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcPlusParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfElseContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcPlusParser.StmtContext
            super().__init__(parser)
            self.thenBlock = None # BlockContext
            self.elseBlock = None # BlockContext
            self.copyFrom(ctx)

        def cond(self):
            return self.getTypedRuleContext(CalcPlusParser.CondContext,0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcPlusParser.BlockContext)
            else:
                return self.getTypedRuleContext(CalcPlusParser.BlockContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)


    class ExprAssignContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcPlusParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(CalcPlusParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcPlusParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAssign" ):
                listener.enterExprAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAssign" ):
                listener.exitExprAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAssign" ):
                return visitor.visitExprAssign(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = CalcPlusParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                localctx = CalcPlusParser.ExprAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(CalcPlusParser.VAR)
                self.state = 45
                self.match(CalcPlusParser.T__6)
                self.state = 46
                self.expr(0)
                self.state = 47
                self.match(CalcPlusParser.T__7)
                pass
            elif token in [9]:
                localctx = CalcPlusParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(CalcPlusParser.T__8)
                self.state = 50
                self.match(CalcPlusParser.T__4)
                self.state = 51
                self.cond()
                self.state = 52
                self.match(CalcPlusParser.T__5)
                self.state = 53
                localctx.thenBlock = self.block()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 54
                    self.match(CalcPlusParser.T__9)
                    self.state = 55
                    localctx.elseBlock = self.block()


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


    class Calc2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CalcPlusParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcPlusParser.StmtContext)
            else:
                return self.getTypedRuleContext(CalcPlusParser.StmtContext,i)


        def getRuleIndex(self):
            return CalcPlusParser.RULE_calc2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalc2" ):
                listener.enterCalc2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalc2" ):
                listener.exitCalc2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalc2" ):
                return visitor.visitCalc2(self)
            else:
                return visitor.visitChildren(self)




    def calc2(self):

        localctx = CalcPlusParser.Calc2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_calc2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.stmt()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9 or _la==21):
                    break

            self.state = 65
            self.match(CalcPlusParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcPlusParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcPlusParser.ExprContext,i)


        def getRuleIndex(self):
            return CalcPlusParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = CalcPlusParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.expr(0)
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 69
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcPlusParser.StmtContext)
            else:
                return self.getTypedRuleContext(CalcPlusParser.StmtContext,i)


        def getRuleIndex(self):
            return CalcPlusParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = CalcPlusParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(CalcPlusParser.T__16)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==21:
                self.state = 72
                self.stmt()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(CalcPlusParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




