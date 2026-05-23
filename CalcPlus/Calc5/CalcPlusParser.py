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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("\\\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16")
        buf.write("\n\2\r\2\16\2\17\3\2\3\2\3\3\3\3\3\3\3\3\7\3\30\n\3\f")
        buf.write("\3\16\3\33\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\66\n\3\3\3\5\39\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4B\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4J\n\4\f\4\16")
        buf.write("\4M\13\4\3\5\3\5\3\5\3\5\3\6\3\6\7\6U\n\6\f\6\16\6X\13")
        buf.write("\6\3\6\3\6\3\6\2\3\6\7\2\4\6\b\n\2\5\3\2\r\16\3\2\17\20")
        buf.write("\3\2\21\26\2c\2\r\3\2\2\2\48\3\2\2\2\6A\3\2\2\2\bN\3\2")
        buf.write("\2\2\nR\3\2\2\2\f\16\5\4\3\2\r\f\3\2\2\2\16\17\3\2\2\2")
        buf.write("\17\r\3\2\2\2\17\20\3\2\2\2\20\21\3\2\2\2\21\22\7\2\2")
        buf.write("\3\22\3\3\2\2\2\23\24\7\3\2\2\24\31\7\33\2\2\25\26\7\4")
        buf.write("\2\2\26\30\7\33\2\2\27\25\3\2\2\2\30\33\3\2\2\2\31\27")
        buf.write("\3\2\2\2\31\32\3\2\2\2\32\34\3\2\2\2\33\31\3\2\2\2\34")
        buf.write("9\7\5\2\2\35\36\7\33\2\2\36\37\7\6\2\2\37 \5\6\4\2 !\7")
        buf.write("\5\2\2!9\3\2\2\2\"#\7\33\2\2#$\7\6\2\2$%\7\7\2\2%&\7\b")
        buf.write("\2\2&\'\7\t\2\2\'9\7\5\2\2()\7\n\2\2)*\7\b\2\2*+\5\6\4")
        buf.write("\2+,\7\t\2\2,-\7\5\2\2-9\3\2\2\2./\7\13\2\2/\60\7\b\2")
        buf.write("\2\60\61\5\b\5\2\61\62\7\t\2\2\62\65\5\n\6\2\63\64\7\f")
        buf.write("\2\2\64\66\5\n\6\2\65\63\3\2\2\2\65\66\3\2\2\2\669\3\2")
        buf.write("\2\2\679\5\n\6\28\23\3\2\2\28\35\3\2\2\28\"\3\2\2\28(")
        buf.write("\3\2\2\28.\3\2\2\28\67\3\2\2\29\5\3\2\2\2:;\b\4\1\2;B")
        buf.write("\7\32\2\2<B\7\33\2\2=>\7\b\2\2>?\5\6\4\2?@\7\t\2\2@B\3")
        buf.write("\2\2\2A:\3\2\2\2A<\3\2\2\2A=\3\2\2\2BK\3\2\2\2CD\f\7\2")
        buf.write("\2DE\t\2\2\2EJ\5\6\4\bFG\f\6\2\2GH\t\3\2\2HJ\5\6\4\7I")
        buf.write("C\3\2\2\2IF\3\2\2\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2\2L\7\3")
        buf.write("\2\2\2MK\3\2\2\2NO\5\6\4\2OP\t\4\2\2PQ\5\6\4\2Q\t\3\2")
        buf.write("\2\2RV\7\27\2\2SU\5\4\3\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2")
        buf.write("\2VW\3\2\2\2WY\3\2\2\2XV\3\2\2\2YZ\7\30\2\2Z\13\3\2\2")
        buf.write("\2\n\17\31\658AIKV")
        return buf.getvalue()


class CalcPlusParser ( Parser ):

    grammarFileName = "CalcPlus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "','", "';'", "'='", "'read'", 
                     "'('", "')'", "'write'", "'if'", "'else'", "'*'", "'/'", 
                     "'+'", "'-'", "'=='", "'!='", "'>'", "'>='", "'<'", 
                     "'<='", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "INT", 
                      "VAR" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_cond = 3
    RULE_block = 4

    ruleNames =  [ "program", "stmt", "expr", "cond", "block" ]

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
    T__20=21
    T__21=22
    WS=23
    INT=24
    VAR=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):
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
            return CalcPlusParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CalcPlusParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stmt()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcPlusParser.T__0) | (1 << CalcPlusParser.T__7) | (1 << CalcPlusParser.T__8) | (1 << CalcPlusParser.T__20) | (1 << CalcPlusParser.VAR))) != 0)):
                    break

            self.state = 15
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


    class StmtBlockContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcPlusParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(CalcPlusParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtBlock" ):
                listener.enterStmtBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtBlock" ):
                listener.exitStmtBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtBlock" ):
                return visitor.visitStmtBlock(self)
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


    class DeclareContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcPlusParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(CalcPlusParser.VAR)
            else:
                return self.getToken(CalcPlusParser.VAR, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare" ):
                listener.enterDeclare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare" ):
                listener.exitDeclare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare" ):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = CalcPlusParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = CalcPlusParser.DeclareContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(CalcPlusParser.T__0)
                self.state = 18
                self.match(CalcPlusParser.VAR)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CalcPlusParser.T__1:
                    self.state = 19
                    self.match(CalcPlusParser.T__1)
                    self.state = 20
                    self.match(CalcPlusParser.VAR)
                    self.state = 25
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 26
                self.match(CalcPlusParser.T__2)
                pass

            elif la_ == 2:
                localctx = CalcPlusParser.ExprAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(CalcPlusParser.VAR)
                self.state = 28
                self.match(CalcPlusParser.T__3)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(CalcPlusParser.T__2)
                pass

            elif la_ == 3:
                localctx = CalcPlusParser.ReadAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(CalcPlusParser.VAR)
                self.state = 33
                self.match(CalcPlusParser.T__3)
                self.state = 34
                self.match(CalcPlusParser.T__4)
                self.state = 35
                self.match(CalcPlusParser.T__5)
                self.state = 36
                self.match(CalcPlusParser.T__6)
                self.state = 37
                self.match(CalcPlusParser.T__2)
                pass

            elif la_ == 4:
                localctx = CalcPlusParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.match(CalcPlusParser.T__7)
                self.state = 39
                self.match(CalcPlusParser.T__5)
                self.state = 40
                self.expr(0)
                self.state = 41
                self.match(CalcPlusParser.T__6)
                self.state = 42
                self.match(CalcPlusParser.T__2)
                pass

            elif la_ == 5:
                localctx = CalcPlusParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.match(CalcPlusParser.T__8)
                self.state = 45
                self.match(CalcPlusParser.T__5)
                self.state = 46
                self.cond()
                self.state = 47
                self.match(CalcPlusParser.T__6)
                self.state = 48
                localctx.thenBlock = self.block()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CalcPlusParser.T__9:
                    self.state = 49
                    self.match(CalcPlusParser.T__9)
                    self.state = 50
                    localctx.elseBlock = self.block()


                pass

            elif la_ == 6:
                localctx = CalcPlusParser.StmtBlockContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 53
                self.block()
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalcPlusParser.INT]:
                localctx = CalcPlusParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 57
                self.match(CalcPlusParser.INT)
                pass
            elif token in [CalcPlusParser.VAR]:
                localctx = CalcPlusParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                self.match(CalcPlusParser.VAR)
                pass
            elif token in [CalcPlusParser.T__5]:
                localctx = CalcPlusParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(CalcPlusParser.T__5)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(CalcPlusParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = CalcPlusParser.MulDivContext(self, CalcPlusParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 66
                        _la = self._input.LA(1)
                        if not(_la==CalcPlusParser.T__10 or _la==CalcPlusParser.T__11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = CalcPlusParser.AddSubContext(self, CalcPlusParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 69
                        _la = self._input.LA(1)
                        if not(_la==CalcPlusParser.T__12 or _la==CalcPlusParser.T__13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 70
                        self.expr(5)
                        pass

             
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 6, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.expr(0)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcPlusParser.T__14) | (1 << CalcPlusParser.T__15) | (1 << CalcPlusParser.T__16) | (1 << CalcPlusParser.T__17) | (1 << CalcPlusParser.T__18) | (1 << CalcPlusParser.T__19))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 78
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
        self.enterRule(localctx, 8, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(CalcPlusParser.T__20)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcPlusParser.T__0) | (1 << CalcPlusParser.T__7) | (1 << CalcPlusParser.T__8) | (1 << CalcPlusParser.T__20) | (1 << CalcPlusParser.VAR))) != 0):
                self.state = 81
                self.stmt()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self.match(CalcPlusParser.T__21)
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
        self._predicates[2] = self.expr_sempred
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
         




