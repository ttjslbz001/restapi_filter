from ply import lex

# Lexer
tokens = (
    'EQ', 'AND', 'OR', 'NOT', 'ISNULL', 'NE', 'LT', 'LE', 'GT', 'GE', 'IN',
    'LPAREN', 'RPAREN', 'COMMA', 'DOT',
    'NUMBER', 'STRING', 'TRUE', 'FALSE', 'NULL', 'IDENTIFIER'
)

# Reserved words
reserved = {
    'eq': 'EQ',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'isNull': 'ISNULL',
    'ne': 'NE',
    'lt': 'LT',
    'le': 'LE',
    'gt': 'GT',
    'ge': 'GE',
    'in': 'IN',
    'true': 'TRUE',
    'false': 'FALSE',
    'null': 'NULL'
}

# Symbols
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_DOT = r'.'


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def p_expression_dot(p):
    '''expression : IDENTIFIER DOT IDENTIFIER'''
    p[0] = {'op': 'dot', 'left': p[1], 'right': p[3]}


def t_STRING(t):
    r'\'[^\']*\''
    t.value = t.value[1:-1]  # Remove the single quotes from the string
    return t


# Ignored characters
t_ignore = ' \t\n'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

