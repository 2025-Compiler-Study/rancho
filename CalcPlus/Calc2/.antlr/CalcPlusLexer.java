// Generated from /home/jake/project/CS/compiler/rancho/CalcPlus/Calc2/CalcPlus.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CalcPlusLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, WS=19, INT=20, VAR=21;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "WS", "INT", "VAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'*'", "'/'", "'+'", "'-'", "'('", "')'", "'='", "';'", "'if'", 
			"'else'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, "WS", "INT", "VAR"
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


	public CalcPlusLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CalcPlus.g4"; }

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
		"\u0004\u0000\u0015h\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001"+
		"\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0004\u0012Y\b\u0012\u000b"+
		"\u0012\f\u0012Z\u0001\u0012\u0001\u0012\u0001\u0013\u0004\u0013`\b\u0013"+
		"\u000b\u0013\f\u0013a\u0001\u0014\u0004\u0014e\b\u0014\u000b\u0014\f\u0014"+
		"f\u0000\u0000\u0015\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t"+
		"\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f"+
		"\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014"+
		")\u0015\u0001\u0000\u0003\u0003\u0000\t\n\r\r  \u0001\u000009\u0002\u0000"+
		"AZazj\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000"+
		"\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000"+
		"\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000"+
		"\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000"+
		"\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000"+
		"\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000"+
		"\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000"+
		"\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000"+
		"!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001"+
		"\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000"+
		"\u0000\u0000\u0001+\u0001\u0000\u0000\u0000\u0003-\u0001\u0000\u0000\u0000"+
		"\u0005/\u0001\u0000\u0000\u0000\u00071\u0001\u0000\u0000\u0000\t3\u0001"+
		"\u0000\u0000\u0000\u000b5\u0001\u0000\u0000\u0000\r7\u0001\u0000\u0000"+
		"\u0000\u000f9\u0001\u0000\u0000\u0000\u0011;\u0001\u0000\u0000\u0000\u0013"+
		">\u0001\u0000\u0000\u0000\u0015C\u0001\u0000\u0000\u0000\u0017F\u0001"+
		"\u0000\u0000\u0000\u0019I\u0001\u0000\u0000\u0000\u001bK\u0001\u0000\u0000"+
		"\u0000\u001dN\u0001\u0000\u0000\u0000\u001fP\u0001\u0000\u0000\u0000!"+
		"S\u0001\u0000\u0000\u0000#U\u0001\u0000\u0000\u0000%X\u0001\u0000\u0000"+
		"\u0000\'_\u0001\u0000\u0000\u0000)d\u0001\u0000\u0000\u0000+,\u0005*\u0000"+
		"\u0000,\u0002\u0001\u0000\u0000\u0000-.\u0005/\u0000\u0000.\u0004\u0001"+
		"\u0000\u0000\u0000/0\u0005+\u0000\u00000\u0006\u0001\u0000\u0000\u0000"+
		"12\u0005-\u0000\u00002\b\u0001\u0000\u0000\u000034\u0005(\u0000\u0000"+
		"4\n\u0001\u0000\u0000\u000056\u0005)\u0000\u00006\f\u0001\u0000\u0000"+
		"\u000078\u0005=\u0000\u00008\u000e\u0001\u0000\u0000\u00009:\u0005;\u0000"+
		"\u0000:\u0010\u0001\u0000\u0000\u0000;<\u0005i\u0000\u0000<=\u0005f\u0000"+
		"\u0000=\u0012\u0001\u0000\u0000\u0000>?\u0005e\u0000\u0000?@\u0005l\u0000"+
		"\u0000@A\u0005s\u0000\u0000AB\u0005e\u0000\u0000B\u0014\u0001\u0000\u0000"+
		"\u0000CD\u0005=\u0000\u0000DE\u0005=\u0000\u0000E\u0016\u0001\u0000\u0000"+
		"\u0000FG\u0005!\u0000\u0000GH\u0005=\u0000\u0000H\u0018\u0001\u0000\u0000"+
		"\u0000IJ\u0005>\u0000\u0000J\u001a\u0001\u0000\u0000\u0000KL\u0005>\u0000"+
		"\u0000LM\u0005=\u0000\u0000M\u001c\u0001\u0000\u0000\u0000NO\u0005<\u0000"+
		"\u0000O\u001e\u0001\u0000\u0000\u0000PQ\u0005<\u0000\u0000QR\u0005=\u0000"+
		"\u0000R \u0001\u0000\u0000\u0000ST\u0005{\u0000\u0000T\"\u0001\u0000\u0000"+
		"\u0000UV\u0005}\u0000\u0000V$\u0001\u0000\u0000\u0000WY\u0007\u0000\u0000"+
		"\u0000XW\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000ZX\u0001\u0000"+
		"\u0000\u0000Z[\u0001\u0000\u0000\u0000[\\\u0001\u0000\u0000\u0000\\]\u0006"+
		"\u0012\u0000\u0000]&\u0001\u0000\u0000\u0000^`\u0007\u0001\u0000\u0000"+
		"_^\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000"+
		"\u0000ab\u0001\u0000\u0000\u0000b(\u0001\u0000\u0000\u0000ce\u0007\u0002"+
		"\u0000\u0000dc\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000\u0000fd\u0001"+
		"\u0000\u0000\u0000fg\u0001\u0000\u0000\u0000g*\u0001\u0000\u0000\u0000"+
		"\u0004\u0000Zaf\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}