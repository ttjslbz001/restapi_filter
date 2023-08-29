from ply import lex, yacc

# Token definitions
tokens = ('AND', 'OR', 'NOT', 'EQ', 'GT', 'LT', 'IDENTIFIER', 'NUMBER', 'LPAREN', 'RPAREN', 'STRING')

reserved = {
    'AND': 'AND',
    'OR': 'OR',
    'NOT': 'NOT'
}

t_EQ = r'='
t_GT = r'>'
t_LT = r'<'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STRING = r'\".*?\"'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

t_NUMBER = r'\d+'

# Ignored characters
t_ignore = " \t"

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parsing rules
def p_expression_binop(p):
    '''expression : expression EQ expression
                  | expression GT expression
                  | expression LT expression
                  | expression AND expression
                  | expression OR expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = (p[1], p[2])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_id(p):
    'expression : IDENTIFIER'
    p[0] = p[1]

def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = int(p[1])

def p_error(p):
    print(f"Syntax error at '{p.value}'")




# Test

# tokens

filter_query = 'age > 25 AND status = "active"'
# Tokenize the input data


lexer.input(filter_query)
print("Tokens:")
for token in lexer:
    print(token)

parser = yacc.yacc()
result = parser.parse(filter_query)
print(result)
