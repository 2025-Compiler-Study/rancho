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
        buf.write("Q\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3&\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\5\3.\n\3\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\7\5\66\n\5\f\5\16\59\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\6D\n\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6L\n\6\f\6")
        buf.write("\16\6O\13\6\3\6\2\3\n\7\2\4\6\b\n\2\5\3\2\13\20\3\2\23")
        buf.write("\24\3\2\25\26\2U\2\r\3\2\2\2\4-\3\2\2\2\6/\3\2\2\2\b\63")
        buf.write("\3\2\2\2\nC\3\2\2\2\f\16\5\4\3\2\r\f\3\2\2\2\16\17\3\2")
        buf.write("\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\21\3\2\2\2\21\22\7")
        buf.write("\2\2\3\22\3\3\2\2\2\23\24\7\31\2\2\24\25\7\3\2\2\25\26")
        buf.write("\5\n\6\2\26\27\7\4\2\2\27.\3\2\2\2\30\31\7\31\2\2\31\32")
        buf.write("\7\3\2\2\32\33\7\5\2\2\33\34\7\6\2\2\34\35\7\7\2\2\35")
        buf.write(".\7\4\2\2\36\37\7\b\2\2\37 \7\6\2\2 !\5\6\4\2!\"\7\7\2")
        buf.write("\2\"%\5\b\5\2#$\7\t\2\2$&\5\b\5\2%#\3\2\2\2%&\3\2\2\2")
        buf.write("&.\3\2\2\2\'(\7\n\2\2()\7\6\2\2)*\5\n\6\2*+\7\7\2\2+,")
        buf.write("\7\4\2\2,.\3\2\2\2-\23\3\2\2\2-\30\3\2\2\2-\36\3\2\2\2")
        buf.write("-\'\3\2\2\2.\5\3\2\2\2/\60\5\n\6\2\60\61\t\2\2\2\61\62")
        buf.write("\5\n\6\2\62\7\3\2\2\2\63\67\7\21\2\2\64\66\5\4\3\2\65")
        buf.write("\64\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28:\3")
        buf.write("\2\2\29\67\3\2\2\2:;\7\22\2\2;\t\3\2\2\2<=\b\6\1\2=D\7")
        buf.write("\30\2\2>D\7\31\2\2?@\7\6\2\2@A\5\n\6\2AB\7\7\2\2BD\3\2")
        buf.write("\2\2C<\3\2\2\2C>\3\2\2\2C?\3\2\2\2DM\3\2\2\2EF\f\7\2\2")
        buf.write("FG\t\3\2\2GL\5\n\6\bHI\f\6\2\2IJ\t\4\2\2JL\5\n\6\7KE\3")
        buf.write("\2\2\2KH\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\13\3\2")
        buf.write("\2\2OM\3\2\2\2\t\17%-\67CKM")
        return buf.getvalue()


class CalcPlusParser ( Parser ):

    grammarFileName = "CalcPlus.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'read'", "'('", "')'", 
                     "'if'", "'else'", "'write'", "'=='", "'!='", "'>'", 
                     "'>='", "'<'", "'<='", "'{'", "'}'", "'*'", "'/'", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "INT", "VAR" ]

    RULE_calc3 = 0
    RULE_stmt = 1
    RULE_cond = 2
    RULE_block = 3
    RULE_expr = 4

    ruleNames =  [ "calc3", "stmt", "cond", "block", "expr" ]

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
        self.enterRule(localctx, 0, self.RULE_calc3)
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcPlusParser.T__5) | (1 << CalcPlusParser.T__7) | (1 << CalcPlusParser.VAR))) != 0)):
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
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = CalcPlusParser.ExprAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(CalcPlusParser.VAR)
                self.state = 18
                self.match(CalcPlusParser.T__0)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(CalcPlusParser.T__1)
                pass

            elif la_ == 2:
                localctx = CalcPlusParser.ReadAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(CalcPlusParser.VAR)
                self.state = 23
                self.match(CalcPlusParser.T__0)
                self.state = 24
                self.match(CalcPlusParser.T__2)
                self.state = 25
                self.match(CalcPlusParser.T__3)
                self.state = 26
                self.match(CalcPlusParser.T__4)
                self.state = 27
                self.match(CalcPlusParser.T__1)
                pass

            elif la_ == 3:
                localctx = CalcPlusParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.match(CalcPlusParser.T__5)
                self.state = 29
                self.match(CalcPlusParser.T__3)
                self.state = 30
                self.cond()
                self.state = 31
                self.match(CalcPlusParser.T__4)
                self.state = 32
                localctx.thenBlock = self.block()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CalcPlusParser.T__6:
                    self.state = 33
                    self.match(CalcPlusParser.T__6)
                    self.state = 34
                    localctx.elseBlock = self.block()


                pass

            elif la_ == 4:
                localctx = CalcPlusParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.match(CalcPlusParser.T__7)
                self.state = 38
                self.match(CalcPlusParser.T__3)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(CalcPlusParser.T__4)
                self.state = 41
                self.match(CalcPlusParser.T__1)
                pass


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
        self.enterRule(localctx, 4, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.expr(0)
            self.state = 46
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcPlusParser.T__8) | (1 << CalcPlusParser.T__9) | (1 << CalcPlusParser.T__10) | (1 << CalcPlusParser.T__11) | (1 << CalcPlusParser.T__12) | (1 << CalcPlusParser.T__13))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 47
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
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(CalcPlusParser.T__14)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcPlusParser.T__5) | (1 << CalcPlusParser.T__7) | (1 << CalcPlusParser.VAR))) != 0):
                self.state = 50
                self.stmt()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(CalcPlusParser.T__15)
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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalcPlusParser.INT]:
                localctx = CalcPlusParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 59
                self.match(CalcPlusParser.INT)
                pass
            elif token in [CalcPlusParser.VAR]:
                localctx = CalcPlusParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.match(CalcPlusParser.VAR)
                pass
            elif token in [CalcPlusParser.T__3]:
                localctx = CalcPlusParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(CalcPlusParser.T__3)
                self.state = 62
                self.expr(0)
                self.state = 63
                self.match(CalcPlusParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 73
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = CalcPlusParser.MulDivContext(self, CalcPlusParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 67
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 68
                        _la = self._input.LA(1)
                        if not(_la==CalcPlusParser.T__16 or _la==CalcPlusParser.T__17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 69
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = CalcPlusParser.AddSubContext(self, CalcPlusParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 70
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 71
                        _la = self._input.LA(1)
                        if not(_la==CalcPlusParser.T__18 or _la==CalcPlusParser.T__19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 72
                        self.expr(5)
                        pass

             
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
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
         




