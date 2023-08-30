from demo.filter.parser import parser
from demo.filter.interpreter import evaluate

'''
test use the expression check result on context to filter result
'''

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


    input_objs =[{'driver.name': 'dale', 'age': 24},{'driver.name': 'dale1', 'age': 22},{'driver.name': 'dale', 'age': 26}]
    filter_query =  "and(eq(driver.name,'dale'),or(lt(age,25)))"

    results = []

    expression = parser.parse(filter_query)
    for obj in input_objs:
        match: bool = evaluate(expression,obj)
        if match:
            results.append((obj))
    print(results)



