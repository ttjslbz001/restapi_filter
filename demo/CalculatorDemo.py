import ply.lex as lex
import ply.yacc as yacc

# 定义标记列表
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# 正则表达式规则
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# 更复杂的标记规则
def t_NUMBER(t):
    r'\d+'  # 匹配数字
    t.value = int(t.value)
    return t

# 跟踪行号
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# 忽略空格和制表符
t_ignore = ' \t'

# 错误处理
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# 构建词法分析器
lexer = lex.lex()

# 测试
data = "3 + 4 * (10 - 5)"
lexer.input(data)

for token in lexer:
    print(token)


# 定义语法规则
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ('+', p[1], p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = ('-', p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_multiply(p):
    'term : term MULTIPLY factor'
    p[0] = ('*', p[1], p[3])

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = ('/', p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# 测试
data = "3 + 4 * (10 - 5)"
result = parser.parse(data, lexer=lexer)
print(result)


def semantic_analysis(node):
    if isinstance(node, tuple):
        op, left, right = node
        left_type = semantic_analysis(left)
        right_type = semantic_analysis(right)

        if op in ['+', '-', '*', '/']:
            if left_type == 'int' and right_type == 'int':
                return 'int'
            else:
                raise TypeError(f"Unsupported operand types for {op}: '{left_type}' and '{right_type}'")
        # 其他操作可以在此添加
    else:
        # 假设所有的叶节点都是整数
        return 'int'

# 测试
tree = ('+', ('*', 3, 4), ('-', 10, 5))
result_type = semantic_analysis(tree)
print(result_type)


def evaluate(node):
    """Recursively evaluate the parse tree."""
    if isinstance(node, tuple):
        op, left, right = node
        if op == '+':
            return evaluate(left) + evaluate(right)
        elif op == '-':
            return evaluate(left) - evaluate(right)
        elif op == '*':
            return evaluate(left) * evaluate(right)
        elif op == '/':
            return evaluate(left) / evaluate(right)
    else:
        # Leaf node (number)
        return node


# ... [rest of the code]

if __name__ == "__main__":
    # Take input from the user
    data = input("Enter an arithmetic expression: ")

    # Tokenize the input data
    lexer.input(data)
    print("Tokens:")
    for token in lexer:
        print(token)

    # Parse the tokenized data
    result = parser.parse(data, lexer=lexer)
    print("\nParse Tree:")
    print(result)

    # Evaluate the parse tree
    evaluation_result = evaluate(result)
    print("\nEvaluation Result:")
    print(evaluation_result)

    # Perform semantic analysis (optional)
    try:
        result_type = semantic_analysis(result)
        print("\nResult Type:")
        print(result_type)
    except TypeError as e:
        print(f"Error: {e}")

