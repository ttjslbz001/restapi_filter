import ply.yacc as yacc
from demo.sql.lexer import  lexer

def p_query(p):
    'query : SELECT select_items FROM table_name where_clause'

def p_select_items(p):
    '''select_items : select_items COMMA column_name
                    | column_name'''

def p_where_clause(p):
    '''where_clause : WHERE condition
                    | empty'''

def p_condition(p):
    '''condition : expression relational_op expression
                 | condition AND condition
                 | condition OR condition'''

def p_relational_op(p):
    '''relational_op : GT
                     | LT
                     | EQ
                     | NEQ
                     | LTE
                     | GTE'''
    p[0] = p[1]

def p_expression(p):
    '''expression : Identifier
                  | String
                  | NUMBER'''

def p_empty(p):
    'empty :'
    pass

def p_table_name(p):
    'table_name : Identifier'

def p_column_name(p):
    'column_name : Identifier'

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()

query = "SELECT id, name FROM users WHERE age > 20 AND salary > 10000"
result = parser.parse(input=query,
                      lexer=lexer,
                      debug=True,
                      tracking=True)
print(result)

