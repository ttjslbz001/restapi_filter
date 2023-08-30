import ply.lex as lex

tokens = (
    'SELECT', 'FROM', 'WHERE', 'AND', 'OR',
    'Identifier', 'String', 'COMMA','GT',
    'LT',
    'EQ',
    'NEQ',
    'LTE',
    'GTE',
    'NUMBER'
)


t_SELECT = r'\bSELECT\b'
t_FROM = r'\bFROM\b'
t_WHERE = r'\bWHERE\b'
t_AND = r'\bAND\b'
t_OR = r'\bOR\b'
t_COMMA = r','
t_GT = r'>'
t_LT = r'<'
t_EQ = r'='
t_NEQ = r'!='
t_LTE = r'<='
t_GTE = r'>='
t_NUMBER = r'\d+'

def t_Identifier(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_String(t):
    r'\'.*\''
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Invalid token %s" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


