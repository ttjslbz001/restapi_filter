def evaluate(expression, context):
    op = expression.get('op')
    args = expression.get('args')

    if op == 'eq':
        return context[args[0]] == args[1]

    if op == 'and':
        return all(evaluate(arg, context) for arg in args)

    if op == 'or':
        return any(evaluate(arg, context) for arg in args)

    if op == 'lt':
        return context[args[0]] < args[1]

    if op == 'gt':
        return context[args[0]] > args[1]

    # ... Implement other operations like 'le', 'ge', 'ne', etc. ...


# Test the evaluator
if __name__ == "__main__":
    context = {'name': 'dale', 'age': 25}

    eq_expression = {'op': 'eq', 'args': ['name', 'dale']}
    and_expression = {'op': 'and', 'args': [eq_expression, {'op': 'gt', 'args': ['age', 20]}]}
    or_expression = {'op': 'or', 'args': [eq_expression, {'op': 'lt', 'args': ['age', 20]}]}

    print(evaluate(eq_expression, context))  # Output should be True
    print(evaluate(and_expression, context))  # Output should be True
    print(evaluate(or_expression, context))  # Output should be True
