

import unittest
from demo.filter.codegen import generate_code
from demo.filter.parser import parser
from demo.filter.lex import lexer

class TestCodeGen(unittest.TestCase):

    def test_code_gen(self):
        input_objs = [{'name': 'dale', 'age': 24}, {'name': 'dale1', 'age': 22}, {'name': 'dale', 'age': 26}]
        filter_query = "and(eq(name,'dale'),or(lt(age,25)))"
        expression = parser.parse(filter_query)
        filter_func = generate_code(expression)

        self.assertEqual(True,filter_func(input_objs[0]))  # 输出应该是 True
        self.assertEqual(False,filter_func(input_objs[1]))  # 输出应该是 False
        self.assertEqual(False ,filter_func(input_objs[2]))

    def test_parser_path_with_dot(self):
        input_objs = [{'driver':{'name': 'dale', 'age': 24}}, {'driver':{'name': 'dale1', 'age': 24}},{'driver':{'name': 'dale', 'age': 26}}]
        filter_query = "and(eq(driver.name,'dale'),or(lt(driver.age,25)))"
        expression = parser.parse(filter_query)
        filter_func = generate_code(expression)

        self.assertEqual(True, filter_func(input_objs[0]))  # 输出应该是 True
        self.assertEqual(False, filter_func(input_objs[1]))  # 输出应该是 False
        self.assertEqual(False, filter_func(input_objs[2]))
        # 输出应该是 False