
# Parser
from demo.filter.lex import lexer,tokens
from demo.filter.lex import lexer
from ply import yacc


print(f"init tokens ${tokens}")


# Parser
def p_expression_eq(p):
    '''expression : EQ LPAREN arg_list RPAREN'''
    p[0] = {'op': 'eq', 'args': p[3]}


def p_expression_and(p):
    '''expression : AND LPAREN arg_list RPAREN'''
    p[0] = {'op': 'and', 'args': p[3]}


def p_expression_or(p):
    '''expression : OR LPAREN arg_list RPAREN'''
    p[0] = {'op': 'or', 'args': p[3]}


def p_expression_lt(p):
    '''expression : LT LPAREN arg_list RPAREN'''
    p[0] = {'op': 'lt', 'args': p[3]}


def p_expression_gt(p):
    '''expression : GT LPAREN arg_list RPAREN'''
    p[0] = {'op': 'gt', 'args': p[3]}


# ... Define other expression functions for 'NOT', 'ISNULL', etc ...

def p_arg_list_expr(p):
    '''arg_list : arg_list COMMA expression'''
    p[0] = p[1] + [p[3]]


def p_arg_list_base(p):
    '''arg_list : expression'''
    p[0] = [p[1]]


def p_expression_base(p):
    '''expression : arg'''
    p[0] = p[1]


def p_hierarchical_key(p):
    '''hierarchical_key : IDENTIFIER DOT IDENTIFIER'''
    p[0] = {'type': 'hierarchical_key', 'value': f"{p[1]}.{p[3]}"}


def p_arg(p):
    '''arg : NUMBER
           | STRING
           | TRUE
           | FALSE
           | NULL
           | hierarchical_key
           | IDENTIFIER'''
    p[0] = p[1]


def p_error(p):
    print("Syntax error!")


parser = yacc.yacc()

if __name__ == "__main__":
    # query = "eq(name,'dale')"
    # result = parser.parse(input=query, lexer=lexer)
    #
    # print(result)

    query2 = "and(eq(driver.name,'dale'),eq(format,'json'),or(bounded,lt(shipDate,8)))"
    result2 = parser.parse(query2, lexer=lexer)
    print(result2)
