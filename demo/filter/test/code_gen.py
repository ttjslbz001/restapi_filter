def generate_code(expression):
    op = expression.get('op')
    args = expression.get('args')

    if op == 'eq':
        return lambda context: context[args[0]] == args[1]

    if op == 'and':
        and_funcs = [generate_code(arg) for arg in args]
        return lambda context: all(f(context) for f in and_funcs)

    if op == 'or':
        or_funcs = [generate_code(arg) for arg in args]
        return lambda context: any(f(context) for f in or_funcs)

    if op == 'lt':
        return lambda context: context[args[0]] < args[1]

    if op == 'gt':
        return lambda context: context[args[0]] > args[1]

    # ... 添加其他操作的处理逻辑 ...


from demo.filter.parser import parser
from demo.filter.evaluator import evaluate


# 测试生成的代码
if __name__ == "__main__":
    context = {'name': 'dale', 'age': 25}

    # eq_expression = {'op': 'eq', 'args': ['name', 'dale']}
    # and_expression = {'op': 'and', 'args': [eq_expression, {'op': 'gt', 'args': ['age', 20]}]}
    # or_expression = {'op': 'or', 'args': [eq_expression, {'op': 'lt', 'args': ['age', 20]}]}

    input_objs =[{'name': 'dale', 'age': 24},{'name': 'dale1', 'age': 22},{'name': 'dale', 'age': 26}]
    filter_query =  "and(eq(name,'dale'),or(lt(age,25)))"
    expression = parser.parse(filter_query)
    filter_func = generate_code(expression)

    print(filter_func(input_objs[0]))  # 输出应该是 True
    print(filter_func(input_objs[1]))  # 输出应该是 False
    print(filter_func(input_objs[2]))  # 输出应该是 False
