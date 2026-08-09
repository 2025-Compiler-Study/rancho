// Generated from grammar/RanchoLexer.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class RanchoLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LET=1, MUT=2, FN=3, RETURN=4, IF=5, ELSE=6, WHILE=7, FOR=8, IN=9, BREAK=10, 
		CONTINUE=11, MATCH=12, STRUCT=13, ENUM=14, IMPL=15, CONST=16, IMPORT=17, 
		AS=18, TRUE=19, FALSE=20, NULL=21, ARROW=22, DOUBLE_COLON=23, SPREAD=24, 
		RANGE_INCLUSIVE=25, RANGE_EXCLUSIVE=26, PLUS_ASSIGN=27, MINUS_ASSIGN=28, 
		STAR_ASSIGN=29, SLASH_ASSIGN=30, PERCENT_ASSIGN=31, AND_ASSIGN=32, OR_ASSIGN=33, 
		XOR_ASSIGN=34, LSHIFT_ASSIGN=35, RSHIFT_ASSIGN=36, INCREMENT=37, DECREMENT=38, 
		EQUAL=39, NOT_EQUAL=40, LESS_EQUAL=41, GREATER_EQUAL=42, LSHIFT=43, RSHIFT=44, 
		AND_AND=45, OR_OR=46, PLUS=47, MINUS=48, STAR=49, SLASH=50, PERCENT=51, 
		ASSIGN=52, LESS=53, GREATER=54, AND=55, OR=56, XOR=57, NOT=58, TILDE=59, 
		QUESTION=60, COLON=61, SEMICOLON=62, COMMA=63, DOT=64, AT=65, HASH=66, 
		LPAREN=67, RPAREN=68, LBRACE=69, RBRACE=70, LBRACK=71, RBRACK=72, IDENTIFIER=73, 
		INTEGER_LITERAL=74, HEX_LITERAL=75, OCT_LITERAL=76, BIN_LITERAL=77, FLOAT_LITERAL=78, 
		STRING_LITERAL=79, CHAR_LITERAL=80, WS=81, LINE_COMMENT=82, BLOCK_COMMENT=83;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LET", "MUT", "FN", "RETURN", "IF", "ELSE", "WHILE", "FOR", "IN", "BREAK", 
			"CONTINUE", "MATCH", "STRUCT", "ENUM", "IMPL", "CONST", "IMPORT", "AS", 
			"TRUE", "FALSE", "NULL", "ARROW", "DOUBLE_COLON", "SPREAD", "RANGE_INCLUSIVE", 
			"RANGE_EXCLUSIVE", "PLUS_ASSIGN", "MINUS_ASSIGN", "STAR_ASSIGN", "SLASH_ASSIGN", 
			"PERCENT_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LSHIFT_ASSIGN", 
			"RSHIFT_ASSIGN", "INCREMENT", "DECREMENT", "EQUAL", "NOT_EQUAL", "LESS_EQUAL", 
			"GREATER_EQUAL", "LSHIFT", "RSHIFT", "AND_AND", "OR_OR", "PLUS", "MINUS", 
			"STAR", "SLASH", "PERCENT", "ASSIGN", "LESS", "GREATER", "AND", "OR", 
			"XOR", "NOT", "TILDE", "QUESTION", "COLON", "SEMICOLON", "COMMA", "DOT", 
			"AT", "HASH", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
			"IDENTIFIER", "INTEGER_LITERAL", "HEX_LITERAL", "OCT_LITERAL", "BIN_LITERAL", 
			"FLOAT_LITERAL", "STRING_LITERAL", "CHAR_LITERAL", "WS", "LINE_COMMENT", 
			"BLOCK_COMMENT", "IDENT_START", "IDENT_CONT", "DEC_DIGIT", "HEX_DIGIT", 
			"OCT_DIGIT", "BIN_DIGIT", "EXPONENT", "ESC_SEQ"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'let'", "'mut'", "'fn'", "'return'", "'if'", "'else'", "'while'", 
			"'for'", "'in'", "'break'", "'continue'", "'match'", "'struct'", "'enum'", 
			"'impl'", "'const'", "'import'", "'as'", "'true'", "'false'", "'null'", 
			"'->'", "'::'", "'...'", "'..='", "'..'", "'+='", "'-='", "'*='", "'/='", 
			"'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", "'++'", "'--'", "'=='", 
			"'!='", "'<='", "'>='", "'<<'", "'>>'", "'&&'", "'||'", "'+'", "'-'", 
			"'*'", "'/'", "'%'", "'='", "'<'", "'>'", "'&'", "'|'", "'^'", "'!'", 
			"'~'", "'?'", "':'", "';'", "','", "'.'", "'@'", "'#'", "'('", "')'", 
			"'{'", "'}'", "'['", "']'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LET", "MUT", "FN", "RETURN", "IF", "ELSE", "WHILE", "FOR", "IN", 
			"BREAK", "CONTINUE", "MATCH", "STRUCT", "ENUM", "IMPL", "CONST", "IMPORT", 
			"AS", "TRUE", "FALSE", "NULL", "ARROW", "DOUBLE_COLON", "SPREAD", "RANGE_INCLUSIVE", 
			"RANGE_EXCLUSIVE", "PLUS_ASSIGN", "MINUS_ASSIGN", "STAR_ASSIGN", "SLASH_ASSIGN", 
			"PERCENT_ASSIGN", "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LSHIFT_ASSIGN", 
			"RSHIFT_ASSIGN", "INCREMENT", "DECREMENT", "EQUAL", "NOT_EQUAL", "LESS_EQUAL", 
			"GREATER_EQUAL", "LSHIFT", "RSHIFT", "AND_AND", "OR_OR", "PLUS", "MINUS", 
			"STAR", "SLASH", "PERCENT", "ASSIGN", "LESS", "GREATER", "AND", "OR", 
			"XOR", "NOT", "TILDE", "QUESTION", "COLON", "SEMICOLON", "COMMA", "DOT", 
			"AT", "HASH", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
			"IDENTIFIER", "INTEGER_LITERAL", "HEX_LITERAL", "OCT_LITERAL", "BIN_LITERAL", 
			"FLOAT_LITERAL", "STRING_LITERAL", "CHAR_LITERAL", "WS", "LINE_COMMENT", 
			"BLOCK_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public RanchoLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "RanchoLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2U\u023f\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
		"\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\3\2\3\2\3\2\3\3"+
		"\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3"+
		"\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17"+
		"\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30"+
		"\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34"+
		"\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3"+
		"!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'"+
		"\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/"+
		"\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3"+
		"\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3"+
		"A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\7J\u01ac\n"+
		"J\fJ\16J\u01af\13J\3K\6K\u01b2\nK\rK\16K\u01b3\3L\3L\3L\6L\u01b9\nL\r"+
		"L\16L\u01ba\3M\3M\3M\6M\u01c0\nM\rM\16M\u01c1\3N\3N\3N\6N\u01c7\nN\rN"+
		"\16N\u01c8\3O\6O\u01cc\nO\rO\16O\u01cd\3O\3O\7O\u01d2\nO\fO\16O\u01d5"+
		"\13O\3O\5O\u01d8\nO\3O\3O\6O\u01dc\nO\rO\16O\u01dd\3O\5O\u01e1\nO\3O\6"+
		"O\u01e4\nO\rO\16O\u01e5\3O\3O\5O\u01ea\nO\3P\3P\3P\7P\u01ef\nP\fP\16P"+
		"\u01f2\13P\3P\3P\3Q\3Q\3Q\5Q\u01f9\nQ\3Q\3Q\3R\6R\u01fe\nR\rR\16R\u01ff"+
		"\3R\3R\3S\3S\3S\3S\7S\u0208\nS\fS\16S\u020b\13S\3S\3S\3T\3T\3T\3T\7T\u0213"+
		"\nT\fT\16T\u0216\13T\3T\3T\3T\3T\3T\3U\3U\3V\3V\5V\u0221\nV\3W\3W\3X\3"+
		"X\3Y\3Y\3Z\3Z\3[\3[\5[\u022d\n[\3[\6[\u0230\n[\r[\16[\u0231\3\\\3\\\3"+
		"\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\5\\\u023e\n\\\3\u0214\2]\3\3\5\4\7\5\t"+
		"\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23"+
		"%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G"+
		"%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{"+
		"?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091"+
		"J\u0093K\u0095L\u0097M\u0099N\u009bO\u009dP\u009fQ\u00a1R\u00a3S\u00a5"+
		"T\u00a7U\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1\2\u00b3\2\u00b5\2\u00b7"+
		"\2\3\2\21\4\2ZZzz\4\2QQqq\4\2DDdd\6\2\f\f\17\17$$^^\6\2\f\f\17\17))^^"+
		"\5\2\13\f\17\17\"\"\4\2\f\f\17\17\5\2C\\aac|\3\2\62;\5\2\62;CHch\3\2\62"+
		"9\3\2\62\63\4\2GGgg\4\2--//\t\2$$))^^ddppttvv\2\u024d\2\3\3\2\2\2\2\5"+
		"\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2"+
		"\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33"+
		"\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2"+
		"\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2"+
		"\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2"+
		"\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K"+
		"\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2"+
		"\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2"+
		"\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q"+
		"\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2"+
		"\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087"+
		"\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2"+
		"\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099"+
		"\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2"+
		"\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\3\u00b9\3\2\2\2\5\u00bd"+
		"\3\2\2\2\7\u00c1\3\2\2\2\t\u00c4\3\2\2\2\13\u00cb\3\2\2\2\r\u00ce\3\2"+
		"\2\2\17\u00d3\3\2\2\2\21\u00d9\3\2\2\2\23\u00dd\3\2\2\2\25\u00e0\3\2\2"+
		"\2\27\u00e6\3\2\2\2\31\u00ef\3\2\2\2\33\u00f5\3\2\2\2\35\u00fc\3\2\2\2"+
		"\37\u0101\3\2\2\2!\u0106\3\2\2\2#\u010c\3\2\2\2%\u0113\3\2\2\2\'\u0116"+
		"\3\2\2\2)\u011b\3\2\2\2+\u0121\3\2\2\2-\u0126\3\2\2\2/\u0129\3\2\2\2\61"+
		"\u012c\3\2\2\2\63\u0130\3\2\2\2\65\u0134\3\2\2\2\67\u0137\3\2\2\29\u013a"+
		"\3\2\2\2;\u013d\3\2\2\2=\u0140\3\2\2\2?\u0143\3\2\2\2A\u0146\3\2\2\2C"+
		"\u0149\3\2\2\2E\u014c\3\2\2\2G\u014f\3\2\2\2I\u0153\3\2\2\2K\u0157\3\2"+
		"\2\2M\u015a\3\2\2\2O\u015d\3\2\2\2Q\u0160\3\2\2\2S\u0163\3\2\2\2U\u0166"+
		"\3\2\2\2W\u0169\3\2\2\2Y\u016c\3\2\2\2[\u016f\3\2\2\2]\u0172\3\2\2\2_"+
		"\u0175\3\2\2\2a\u0177\3\2\2\2c\u0179\3\2\2\2e\u017b\3\2\2\2g\u017d\3\2"+
		"\2\2i\u017f\3\2\2\2k\u0181\3\2\2\2m\u0183\3\2\2\2o\u0185\3\2\2\2q\u0187"+
		"\3\2\2\2s\u0189\3\2\2\2u\u018b\3\2\2\2w\u018d\3\2\2\2y\u018f\3\2\2\2{"+
		"\u0191\3\2\2\2}\u0193\3\2\2\2\177\u0195\3\2\2\2\u0081\u0197\3\2\2\2\u0083"+
		"\u0199\3\2\2\2\u0085\u019b\3\2\2\2\u0087\u019d\3\2\2\2\u0089\u019f\3\2"+
		"\2\2\u008b\u01a1\3\2\2\2\u008d\u01a3\3\2\2\2\u008f\u01a5\3\2\2\2\u0091"+
		"\u01a7\3\2\2\2\u0093\u01a9\3\2\2\2\u0095\u01b1\3\2\2\2\u0097\u01b5\3\2"+
		"\2\2\u0099\u01bc\3\2\2\2\u009b\u01c3\3\2\2\2\u009d\u01e9\3\2\2\2\u009f"+
		"\u01eb\3\2\2\2\u00a1\u01f5\3\2\2\2\u00a3\u01fd\3\2\2\2\u00a5\u0203\3\2"+
		"\2\2\u00a7\u020e\3\2\2\2\u00a9\u021c\3\2\2\2\u00ab\u0220\3\2\2\2\u00ad"+
		"\u0222\3\2\2\2\u00af\u0224\3\2\2\2\u00b1\u0226\3\2\2\2\u00b3\u0228\3\2"+
		"\2\2\u00b5\u022a\3\2\2\2\u00b7\u023d\3\2\2\2\u00b9\u00ba\7n\2\2\u00ba"+
		"\u00bb\7g\2\2\u00bb\u00bc\7v\2\2\u00bc\4\3\2\2\2\u00bd\u00be\7o\2\2\u00be"+
		"\u00bf\7w\2\2\u00bf\u00c0\7v\2\2\u00c0\6\3\2\2\2\u00c1\u00c2\7h\2\2\u00c2"+
		"\u00c3\7p\2\2\u00c3\b\3\2\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7g\2\2\u00c6"+
		"\u00c7\7v\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca\7p\2\2"+
		"\u00ca\n\3\2\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7h\2\2\u00cd\f\3\2\2\2"+
		"\u00ce\u00cf\7g\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2"+
		"\7g\2\2\u00d2\16\3\2\2\2\u00d3\u00d4\7y\2\2\u00d4\u00d5\7j\2\2\u00d5\u00d6"+
		"\7k\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7g\2\2\u00d8\20\3\2\2\2\u00d9\u00da"+
		"\7h\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7t\2\2\u00dc\22\3\2\2\2\u00dd\u00de"+
		"\7k\2\2\u00de\u00df\7p\2\2\u00df\24\3\2\2\2\u00e0\u00e1\7d\2\2\u00e1\u00e2"+
		"\7t\2\2\u00e2\u00e3\7g\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5\7m\2\2\u00e5"+
		"\26\3\2\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7p\2\2\u00e9"+
		"\u00ea\7v\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7w\2\2"+
		"\u00ed\u00ee\7g\2\2\u00ee\30\3\2\2\2\u00ef\u00f0\7o\2\2\u00f0\u00f1\7"+
		"c\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7e\2\2\u00f3\u00f4\7j\2\2\u00f4\32"+
		"\3\2\2\2\u00f5\u00f6\7u\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8\7t\2\2\u00f8"+
		"\u00f9\7w\2\2\u00f9\u00fa\7e\2\2\u00fa\u00fb\7v\2\2\u00fb\34\3\2\2\2\u00fc"+
		"\u00fd\7g\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff\7w\2\2\u00ff\u0100\7o\2\2"+
		"\u0100\36\3\2\2\2\u0101\u0102\7k\2\2\u0102\u0103\7o\2\2\u0103\u0104\7"+
		"r\2\2\u0104\u0105\7n\2\2\u0105 \3\2\2\2\u0106\u0107\7e\2\2\u0107\u0108"+
		"\7q\2\2\u0108\u0109\7p\2\2\u0109\u010a\7u\2\2\u010a\u010b\7v\2\2\u010b"+
		"\"\3\2\2\2\u010c\u010d\7k\2\2\u010d\u010e\7o\2\2\u010e\u010f\7r\2\2\u010f"+
		"\u0110\7q\2\2\u0110\u0111\7t\2\2\u0111\u0112\7v\2\2\u0112$\3\2\2\2\u0113"+
		"\u0114\7c\2\2\u0114\u0115\7u\2\2\u0115&\3\2\2\2\u0116\u0117\7v\2\2\u0117"+
		"\u0118\7t\2\2\u0118\u0119\7w\2\2\u0119\u011a\7g\2\2\u011a(\3\2\2\2\u011b"+
		"\u011c\7h\2\2\u011c\u011d\7c\2\2\u011d\u011e\7n\2\2\u011e\u011f\7u\2\2"+
		"\u011f\u0120\7g\2\2\u0120*\3\2\2\2\u0121\u0122\7p\2\2\u0122\u0123\7w\2"+
		"\2\u0123\u0124\7n\2\2\u0124\u0125\7n\2\2\u0125,\3\2\2\2\u0126\u0127\7"+
		"/\2\2\u0127\u0128\7@\2\2\u0128.\3\2\2\2\u0129\u012a\7<\2\2\u012a\u012b"+
		"\7<\2\2\u012b\60\3\2\2\2\u012c\u012d\7\60\2\2\u012d\u012e\7\60\2\2\u012e"+
		"\u012f\7\60\2\2\u012f\62\3\2\2\2\u0130\u0131\7\60\2\2\u0131\u0132\7\60"+
		"\2\2\u0132\u0133\7?\2\2\u0133\64\3\2\2\2\u0134\u0135\7\60\2\2\u0135\u0136"+
		"\7\60\2\2\u0136\66\3\2\2\2\u0137\u0138\7-\2\2\u0138\u0139\7?\2\2\u0139"+
		"8\3\2\2\2\u013a\u013b\7/\2\2\u013b\u013c\7?\2\2\u013c:\3\2\2\2\u013d\u013e"+
		"\7,\2\2\u013e\u013f\7?\2\2\u013f<\3\2\2\2\u0140\u0141\7\61\2\2\u0141\u0142"+
		"\7?\2\2\u0142>\3\2\2\2\u0143\u0144\7\'\2\2\u0144\u0145\7?\2\2\u0145@\3"+
		"\2\2\2\u0146\u0147\7(\2\2\u0147\u0148\7?\2\2\u0148B\3\2\2\2\u0149\u014a"+
		"\7~\2\2\u014a\u014b\7?\2\2\u014bD\3\2\2\2\u014c\u014d\7`\2\2\u014d\u014e"+
		"\7?\2\2\u014eF\3\2\2\2\u014f\u0150\7>\2\2\u0150\u0151\7>\2\2\u0151\u0152"+
		"\7?\2\2\u0152H\3\2\2\2\u0153\u0154\7@\2\2\u0154\u0155\7@\2\2\u0155\u0156"+
		"\7?\2\2\u0156J\3\2\2\2\u0157\u0158\7-\2\2\u0158\u0159\7-\2\2\u0159L\3"+
		"\2\2\2\u015a\u015b\7/\2\2\u015b\u015c\7/\2\2\u015cN\3\2\2\2\u015d\u015e"+
		"\7?\2\2\u015e\u015f\7?\2\2\u015fP\3\2\2\2\u0160\u0161\7#\2\2\u0161\u0162"+
		"\7?\2\2\u0162R\3\2\2\2\u0163\u0164\7>\2\2\u0164\u0165\7?\2\2\u0165T\3"+
		"\2\2\2\u0166\u0167\7@\2\2\u0167\u0168\7?\2\2\u0168V\3\2\2\2\u0169\u016a"+
		"\7>\2\2\u016a\u016b\7>\2\2\u016bX\3\2\2\2\u016c\u016d\7@\2\2\u016d\u016e"+
		"\7@\2\2\u016eZ\3\2\2\2\u016f\u0170\7(\2\2\u0170\u0171\7(\2\2\u0171\\\3"+
		"\2\2\2\u0172\u0173\7~\2\2\u0173\u0174\7~\2\2\u0174^\3\2\2\2\u0175\u0176"+
		"\7-\2\2\u0176`\3\2\2\2\u0177\u0178\7/\2\2\u0178b\3\2\2\2\u0179\u017a\7"+
		",\2\2\u017ad\3\2\2\2\u017b\u017c\7\61\2\2\u017cf\3\2\2\2\u017d\u017e\7"+
		"\'\2\2\u017eh\3\2\2\2\u017f\u0180\7?\2\2\u0180j\3\2\2\2\u0181\u0182\7"+
		">\2\2\u0182l\3\2\2\2\u0183\u0184\7@\2\2\u0184n\3\2\2\2\u0185\u0186\7("+
		"\2\2\u0186p\3\2\2\2\u0187\u0188\7~\2\2\u0188r\3\2\2\2\u0189\u018a\7`\2"+
		"\2\u018at\3\2\2\2\u018b\u018c\7#\2\2\u018cv\3\2\2\2\u018d\u018e\7\u0080"+
		"\2\2\u018ex\3\2\2\2\u018f\u0190\7A\2\2\u0190z\3\2\2\2\u0191\u0192\7<\2"+
		"\2\u0192|\3\2\2\2\u0193\u0194\7=\2\2\u0194~\3\2\2\2\u0195\u0196\7.\2\2"+
		"\u0196\u0080\3\2\2\2\u0197\u0198\7\60\2\2\u0198\u0082\3\2\2\2\u0199\u019a"+
		"\7B\2\2\u019a\u0084\3\2\2\2\u019b\u019c\7%\2\2\u019c\u0086\3\2\2\2\u019d"+
		"\u019e\7*\2\2\u019e\u0088\3\2\2\2\u019f\u01a0\7+\2\2\u01a0\u008a\3\2\2"+
		"\2\u01a1\u01a2\7}\2\2\u01a2\u008c\3\2\2\2\u01a3\u01a4\7\177\2\2\u01a4"+
		"\u008e\3\2\2\2\u01a5\u01a6\7]\2\2\u01a6\u0090\3\2\2\2\u01a7\u01a8\7_\2"+
		"\2\u01a8\u0092\3\2\2\2\u01a9\u01ad\5\u00a9U\2\u01aa\u01ac\5\u00abV\2\u01ab"+
		"\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2"+
		"\2\2\u01ae\u0094\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b2\5\u00adW\2\u01b1"+
		"\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2"+
		"\2\2\u01b4\u0096\3\2\2\2\u01b5\u01b6\7\62\2\2\u01b6\u01b8\t\2\2\2\u01b7"+
		"\u01b9\5\u00afX\2\u01b8\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01b8"+
		"\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u0098\3\2\2\2\u01bc\u01bd\7\62\2\2"+
		"\u01bd\u01bf\t\3\2\2\u01be\u01c0\5\u00b1Y\2\u01bf\u01be\3\2\2\2\u01c0"+
		"\u01c1\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u009a\3\2"+
		"\2\2\u01c3\u01c4\7\62\2\2\u01c4\u01c6\t\4\2\2\u01c5\u01c7\5\u00b3Z\2\u01c6"+
		"\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2"+
		"\2\2\u01c9\u009c\3\2\2\2\u01ca\u01cc\5\u00adW\2\u01cb\u01ca\3\2\2\2\u01cc"+
		"\u01cd\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01cf\3\2"+
		"\2\2\u01cf\u01d3\7\60\2\2\u01d0\u01d2\5\u00adW\2\u01d1\u01d0\3\2\2\2\u01d2"+
		"\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d7\3\2"+
		"\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d8\5\u00b5[\2\u01d7\u01d6\3\2\2\2\u01d7"+
		"\u01d8\3\2\2\2\u01d8\u01ea\3\2\2\2\u01d9\u01db\7\60\2\2\u01da\u01dc\5"+
		"\u00adW\2\u01db\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01db\3\2\2\2"+
		"\u01dd\u01de\3\2\2\2\u01de\u01e0\3\2\2\2\u01df\u01e1\5\u00b5[\2\u01e0"+
		"\u01df\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01ea\3\2\2\2\u01e2\u01e4\5\u00ad"+
		"W\2\u01e3\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5"+
		"\u01e6\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\5\u00b5[\2\u01e8\u01ea"+
		"\3\2\2\2\u01e9\u01cb\3\2\2\2\u01e9\u01d9\3\2\2\2\u01e9\u01e3\3\2\2\2\u01ea"+
		"\u009e\3\2\2\2\u01eb\u01f0\7$\2\2\u01ec\u01ef\5\u00b7\\\2\u01ed\u01ef"+
		"\n\5\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ed\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0"+
		"\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f3\3\2\2\2\u01f2\u01f0\3\2"+
		"\2\2\u01f3\u01f4\7$\2\2\u01f4\u00a0\3\2\2\2\u01f5\u01f8\7)\2\2\u01f6\u01f9"+
		"\5\u00b7\\\2\u01f7\u01f9\n\6\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f7\3\2\2"+
		"\2\u01f9\u01fa\3\2\2\2\u01fa\u01fb\7)\2\2\u01fb\u00a2\3\2\2\2\u01fc\u01fe"+
		"\t\7\2\2\u01fd\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff"+
		"\u0200\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0202\bR\2\2\u0202\u00a4\3\2"+
		"\2\2\u0203\u0204\7\61\2\2\u0204\u0205\7\61\2\2\u0205\u0209\3\2\2\2\u0206"+
		"\u0208\n\b\2\2\u0207\u0206\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207\3\2"+
		"\2\2\u0209\u020a\3\2\2\2\u020a\u020c\3\2\2\2\u020b\u0209\3\2\2\2\u020c"+
		"\u020d\bS\2\2\u020d\u00a6\3\2\2\2\u020e\u020f\7\61\2\2\u020f\u0210\7,"+
		"\2\2\u0210\u0214\3\2\2\2\u0211\u0213\13\2\2\2\u0212\u0211\3\2\2\2\u0213"+
		"\u0216\3\2\2\2\u0214\u0215\3\2\2\2\u0214\u0212\3\2\2\2\u0215\u0217\3\2"+
		"\2\2\u0216\u0214\3\2\2\2\u0217\u0218\7,\2\2\u0218\u0219\7\61\2\2\u0219"+
		"\u021a\3\2\2\2\u021a\u021b\bT\2\2\u021b\u00a8\3\2\2\2\u021c\u021d\t\t"+
		"\2\2\u021d\u00aa\3\2\2\2\u021e\u0221\5\u00a9U\2\u021f\u0221\t\n\2\2\u0220"+
		"\u021e\3\2\2\2\u0220\u021f\3\2\2\2\u0221\u00ac\3\2\2\2\u0222\u0223\t\n"+
		"\2\2\u0223\u00ae\3\2\2\2\u0224\u0225\t\13\2\2\u0225\u00b0\3\2\2\2\u0226"+
		"\u0227\t\f\2\2\u0227\u00b2\3\2\2\2\u0228\u0229\t\r\2\2\u0229\u00b4\3\2"+
		"\2\2\u022a\u022c\t\16\2\2\u022b\u022d\t\17\2\2\u022c\u022b\3\2\2\2\u022c"+
		"\u022d\3\2\2\2\u022d\u022f\3\2\2\2\u022e\u0230\5\u00adW\2\u022f\u022e"+
		"\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232"+
		"\u00b6\3\2\2\2\u0233\u0234\7^\2\2\u0234\u023e\t\20\2\2\u0235\u0236\7^"+
		"\2\2\u0236\u0237\7w\2\2\u0237\u0238\3\2\2\2\u0238\u0239\5\u00afX\2\u0239"+
		"\u023a\5\u00afX\2\u023a\u023b\5\u00afX\2\u023b\u023c\5\u00afX\2\u023c"+
		"\u023e\3\2\2\2\u023d\u0233\3\2\2\2\u023d\u0235\3\2\2\2\u023e\u00b8\3\2"+
		"\2\2\31\2\u01ad\u01b3\u01ba\u01c1\u01c8\u01cd\u01d3\u01d7\u01dd\u01e0"+
		"\u01e5\u01e9\u01ee\u01f0\u01f8\u01ff\u0209\u0214\u0220\u022c\u0231\u023d"+
		"\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}