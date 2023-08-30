from demo.filter.utils import get_value


def generate_code(expression):
    op = expression.get('op')
    args = expression.get('args')

    if op == 'and':
        and_funcs = [generate_code(arg) for arg in args]
        return lambda context: all(f(context) for f in and_funcs)

    if op == 'or':
        or_funcs = [generate_code(arg) for arg in args]
        return lambda context: any(f(context) for f in or_funcs)

    if op == 'eq':
        return lambda context: get_value(context, args[0]) == args[1]

    if op == 'lt':
        return lambda context: get_value(context, args[0]) < args[1]

    if op == 'gt':
        return lambda context: get_value(context, args[0]) > args[1]
