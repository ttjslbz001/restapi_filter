from parser import parser
from evaluator import evaluate

if __name__=='__main__':

    input_objs =[{'name': 'dale', 'age': 24},{'name': 'dale1', 'age': 22},{'name': 'dale', 'age': 26}]
    filter_query =  "and(eq(name,'dale'),or(lt(age,25)))"

    results = []

    expression = parser.parse(filter_query)
    for obj in input_objs:
        match: bool = evaluate(expression,obj)
        if match:
            results.append((obj))
    print(results)



