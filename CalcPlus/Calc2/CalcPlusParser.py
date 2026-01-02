# Generated from CalcPlus.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("S\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\33\n")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3#\n\3\f\3\16\3&\13\3\3\4")
        buf.write("\6\4)\n\4\r\4\16\4*\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5;\n\5\5\5=\n\5\3\6\6\6@\n\6")
        buf.write("\r\6\16\6A\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\7\bL\n\b\f")
        buf.write("\b\16\bO\13\b\3\b\3\b\3\b\2\3\4\t\2\4\6\b\n\f\16\2\5\3")
        buf.write("\2\3\4\3\2\5\6\3\2\r\22\2T\2\20\3\2\2\2\4\32\3\2\2\2\6")
        buf.write("(\3\2\2\2\b<\3\2\2\2\n?\3\2\2\2\fE\3\2\2\2\16I\3\2\2\2")
        buf.write("\20\21\5\4\3\2\21\22\7\2\2\3\22\3\3\2\2\2\23\24\b\3\1")
        buf.write("\2\24\33\7\26\2\2\25\33\7\27\2\2\26\27\7\7\2\2\27\30\5")
        buf.write("\4\3\2\30\31\7\b\2\2\31\33\3\2\2\2\32\23\3\2\2\2\32\25")
        buf.write("\3\2\2\2\32\26\3\2\2\2\33$\3\2\2\2\34\35\f\7\2\2\35\36")
        buf.write("\t\2\2\2\36#\5\4\3\b\37 \f\6\2\2 !\t\3\2\2!#\5\4\3\7\"")
        buf.write("\34\3\2\2\2\"\37\3\2\2\2#&\3\2\2\2$\"\3\2\2\2$%\3\2\2")
        buf.write("\2%\5\3\2\2\2&$\3\2\2\2\')\5\b\5\2(\'\3\2\2\2)*\3\2\2")
        buf.write("\2*(\3\2\2\2*+\3\2\2\2+,\3\2\2\2,-\7\2\2\3-\7\3\2\2\2")
        buf.write("./\7\27\2\2/\60\7\t\2\2\60\61\5\4\3\2\61\62\7\n\2\2\62")
        buf.write("=\3\2\2\2\63\64\7\13\2\2\64\65\7\7\2\2\65\66\5\f\7\2\66")
        buf.write("\67\7\b\2\2\67:\5\16\b\289\7\f\2\29;\5\16\b\2:8\3\2\2")
        buf.write("\2:;\3\2\2\2;=\3\2\2\2<.\3\2\2\2<\63\3\2\2\2=\t\3\2\2")
        buf.write("\2>@\5\b\5\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B")
        buf.write("C\3\2\2\2CD\7\2\2\3D\13\3\2\2\2EF\5\4\3\2FG\t\4\2\2GH")
        buf.write("\5\4\3\2H\r\3\2\2\2IM\7\23\2\2JL\5\b\5\2KJ\3\2\2\2LO\3")
        buf.write("\2\2\2MK\3\2\2\2MN\3\2\2\2NP\3\2\2\2OM\3\2\2\2PQ\7\24")
        buf.write("\2\2Q\17\3\2\2\2\n\32\"$*:<AM")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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
            if token in [CalcPlusParser.INT]:
                localctx = CalcPlusParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 18
                self.match(CalcPlusParser.INT)
                pass
            elif token in [CalcPlusParser.VAR]:
                localctx = CalcPlusParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                self.match(CalcPlusParser.VAR)
                pass
            elif token in [CalcPlusParser.T__4]:
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
                        if not(_la==CalcPlusParser.T__0 or _la==CalcPlusParser.T__1):
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
                        if not(_la==CalcPlusParser.T__2 or _la==CalcPlusParser.T__3):
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
                if not (_la==CalcPlusParser.T__8 or _la==CalcPlusParser.VAR):
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



    def stmt(self):

        localctx = CalcPlusParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalcPlusParser.VAR]:
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
            elif token in [CalcPlusParser.T__8]:
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
                if _la==CalcPlusParser.T__9:
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
                if not (_la==CalcPlusParser.T__8 or _la==CalcPlusParser.VAR):
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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcPlusParser.T__10) | (1 << CalcPlusParser.T__11) | (1 << CalcPlusParser.T__12) | (1 << CalcPlusParser.T__13) | (1 << CalcPlusParser.T__14) | (1 << CalcPlusParser.T__15))) != 0)):
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
            while _la==CalcPlusParser.T__8 or _la==CalcPlusParser.VAR:
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
         




