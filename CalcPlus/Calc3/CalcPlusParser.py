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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("h\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\35\n\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3%\n\3\f\3\16\3(\13")
        buf.write("\3\3\4\6\4+\n\4\r\4\16\4,\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5")
        buf.write("\5C\n\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5K\n\5\3\6\6\6N\n\6")
        buf.write("\r\6\16\6O\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\7\bZ\n\b\f")
        buf.write("\b\16\b]\13\b\3\b\3\b\3\t\6\tb\n\t\r\t\16\tc\3\t\3\t\3")
        buf.write("\t\2\3\4\n\2\4\6\b\n\f\16\20\2\5\3\2\3\4\3\2\5\6\3\2\17")
        buf.write("\24\2k\2\22\3\2\2\2\4\34\3\2\2\2\6*\3\2\2\2\bJ\3\2\2\2")
        buf.write("\nM\3\2\2\2\fS\3\2\2\2\16W\3\2\2\2\20a\3\2\2\2\22\23\5")
        buf.write("\4\3\2\23\24\7\2\2\3\24\3\3\2\2\2\25\26\b\3\1\2\26\35")
        buf.write("\7\30\2\2\27\35\7\31\2\2\30\31\7\7\2\2\31\32\5\4\3\2\32")
        buf.write("\33\7\b\2\2\33\35\3\2\2\2\34\25\3\2\2\2\34\27\3\2\2\2")
        buf.write("\34\30\3\2\2\2\35&\3\2\2\2\36\37\f\7\2\2\37 \t\2\2\2 ")
        buf.write("%\5\4\3\b!\"\f\6\2\2\"#\t\3\2\2#%\5\4\3\7$\36\3\2\2\2")
        buf.write("$!\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\5\3\2\2\2")
        buf.write("(&\3\2\2\2)+\5\b\5\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3")
        buf.write("\2\2\2-.\3\2\2\2./\7\2\2\3/\7\3\2\2\2\60\61\7\31\2\2\61")
        buf.write("\62\7\t\2\2\62\63\5\4\3\2\63\64\7\n\2\2\64K\3\2\2\2\65")
        buf.write("\66\7\31\2\2\66\67\7\t\2\2\678\7\13\2\289\7\7\2\29:\7")
        buf.write("\b\2\2:K\7\n\2\2;<\7\f\2\2<=\7\7\2\2=>\5\f\7\2>?\7\b\2")
        buf.write("\2?B\5\16\b\2@A\7\r\2\2AC\5\16\b\2B@\3\2\2\2BC\3\2\2\2")
        buf.write("CK\3\2\2\2DE\7\16\2\2EF\7\7\2\2FG\5\4\3\2GH\7\b\2\2HI")
        buf.write("\7\n\2\2IK\3\2\2\2J\60\3\2\2\2J\65\3\2\2\2J;\3\2\2\2J")
        buf.write("D\3\2\2\2K\t\3\2\2\2LN\5\b\5\2ML\3\2\2\2NO\3\2\2\2OM\3")
        buf.write("\2\2\2OP\3\2\2\2PQ\3\2\2\2QR\7\2\2\3R\13\3\2\2\2ST\5\4")
        buf.write("\3\2TU\t\4\2\2UV\5\4\3\2V\r\3\2\2\2W[\7\25\2\2XZ\5\b\5")
        buf.write("\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2")
        buf.write("][\3\2\2\2^_\7\26\2\2_\17\3\2\2\2`b\5\b\5\2a`\3\2\2\2")
        buf.write("bc\3\2\2\2ca\3\2\2\2cd\3\2\2\2de\3\2\2\2ef\7\2\2\3f\21")
        buf.write("\3\2\2\2\13\34$&,BJO[c")
        return buf.getvalue()


class CalcPlusParser ( Parser ):

    grammarFileName = "CalcPlus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'('", "')'", 
                     "'='", "';'", "'read'", "'if'", "'else'", "'write'", 
                     "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "INT", "VAR" ]

    RULE_calc0 = 0
    RULE_expr = 1
    RULE_calc1 = 2
    RULE_stmt = 3
    RULE_calc2 = 4
    RULE_cond = 5
    RULE_block = 6
    RULE_calc3 = 7

    ruleNames =  [ "calc0", "expr", "calc1", "stmt", "calc2", "cond", "block", 
                   "calc3" ]

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
    T__18=19
    T__19=20
    WS=21
    INT=22
    VAR=23

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
            self.state = 16
            self.expr(0)
            self.state = 17
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
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalcPlusParser.INT]:
                localctx = CalcPlusParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 20
                self.match(CalcPlusParser.INT)
                pass
            elif token in [CalcPlusParser.VAR]:
                localctx = CalcPlusParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(CalcPlusParser.VAR)
                pass
            elif token in [CalcPlusParser.T__4]:
                localctx = CalcPlusParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(CalcPlusParser.T__4)
                self.state = 23
                self.expr(0)
                self.state = 24
                self.match(CalcPlusParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = CalcPlusParser.MulDivContext(self, CalcPlusParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 29
                        _la = self._input.LA(1)
                        if not(_la==CalcPlusParser.T__0 or _la==CalcPlusParser.T__1):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 30
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = CalcPlusParser.AddSubContext(self, CalcPlusParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 32
                        _la = self._input.LA(1)
                        if not(_la==CalcPlusParser.T__2 or _la==CalcPlusParser.T__3):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        self.expr(5)
                        pass

             
                self.state = 38
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
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                self.stmt()
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcPlusParser.T__9) | (1 << CalcPlusParser.T__11) | (1 << CalcPlusParser.VAR))) != 0)):
                    break

            self.state = 44
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



    class WriteContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcPlusParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcPlusParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


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


    class ReadAssignContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcPlusParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(CalcPlusParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadAssign" ):
                listener.enterReadAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadAssign" ):
                listener.exitReadAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadAssign" ):
                return visitor.visitReadAssign(self)
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
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = CalcPlusParser.ExprAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(CalcPlusParser.VAR)
                self.state = 47
                self.match(CalcPlusParser.T__6)
                self.state = 48
                self.expr(0)
                self.state = 49
                self.match(CalcPlusParser.T__7)
                pass

            elif la_ == 2:
                localctx = CalcPlusParser.ReadAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(CalcPlusParser.VAR)
                self.state = 52
                self.match(CalcPlusParser.T__6)
                self.state = 53
                self.match(CalcPlusParser.T__8)
                self.state = 54
                self.match(CalcPlusParser.T__4)
                self.state = 55
                self.match(CalcPlusParser.T__5)
                self.state = 56
                self.match(CalcPlusParser.T__7)
                pass

            elif la_ == 3:
                localctx = CalcPlusParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.match(CalcPlusParser.T__9)
                self.state = 58
                self.match(CalcPlusParser.T__4)
                self.state = 59
                self.cond()
                self.state = 60
                self.match(CalcPlusParser.T__5)
                self.state = 61
                localctx.thenBlock = self.block()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CalcPlusParser.T__10:
                    self.state = 62
                    self.match(CalcPlusParser.T__10)
                    self.state = 63
                    localctx.elseBlock = self.block()


                pass

            elif la_ == 4:
                localctx = CalcPlusParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.match(CalcPlusParser.T__11)
                self.state = 67
                self.match(CalcPlusParser.T__4)
                self.state = 68
                self.expr(0)
                self.state = 69
                self.match(CalcPlusParser.T__5)
                self.state = 70
                self.match(CalcPlusParser.T__7)
                pass


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
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.stmt()
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcPlusParser.T__9) | (1 << CalcPlusParser.T__11) | (1 << CalcPlusParser.VAR))) != 0)):
                    break

            self.state = 79
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
            self.state = 81
            self.expr(0)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcPlusParser.T__12) | (1 << CalcPlusParser.T__13) | (1 << CalcPlusParser.T__14) | (1 << CalcPlusParser.T__15) | (1 << CalcPlusParser.T__16) | (1 << CalcPlusParser.T__17))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 83
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
            self.state = 85
            self.match(CalcPlusParser.T__18)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcPlusParser.T__9) | (1 << CalcPlusParser.T__11) | (1 << CalcPlusParser.VAR))) != 0):
                self.state = 86
                self.stmt()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(CalcPlusParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Calc3Context(ParserRuleContext):
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
            return CalcPlusParser.RULE_calc3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalc3" ):
                listener.enterCalc3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalc3" ):
                listener.exitCalc3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalc3" ):
                return visitor.visitCalc3(self)
            else:
                return visitor.visitChildren(self)




    def calc3(self):

        localctx = CalcPlusParser.Calc3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_calc3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.stmt()
                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcPlusParser.T__9) | (1 << CalcPlusParser.T__11) | (1 << CalcPlusParser.VAR))) != 0)):
                    break

            self.state = 99
            self.match(CalcPlusParser.EOF)
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
         




