import unittest


from demo.filter.parser import parser
from demo.filter.lex import lexer


class TestParser(unittest.TestCase):

    def test_parser(self):
        query = "eq(name,'dale')"
        result = parser.parse(input=query, lexer=lexer)
        self.assertEquals({'op': 'eq', 'args': ['name', 'dale']},result)


    def test_path(self):

        query = "eq(driver.name,'dale')"
        result = parser.parse(input=query,lexer = lexer)
        self.assertEquals({'args': [{'type': 'hierarchical_key', 'value': 'driver.name'}, 'dale'],  'op': 'eq'}, result)