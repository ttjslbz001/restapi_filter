from demo.filter.parser import parser
from demo.filter.codegen import generate_code

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
