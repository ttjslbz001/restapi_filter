import unittest

from demo.filter.lex import lexer


class TestLex(unittest.TestCase):

    def testLex(self):
        query = "and(eq(driver.name,'dale'),eq(format,'json'),or(bounded,lt(shipDate,8)))"
        lexer.input(query)
        tokenTypes = []
        for token in lexer:
            tokenTypes.append(token.type)

        self.assertEqual(['AND',
                          'LPAREN',
                          'EQ',
                          'LPAREN',
                          'IDENTIFIER',
                          'DOT',
                          'IDENTIFIER',
                          'COMMA',
                          'STRING',
                          'RPAREN',
                          'COMMA',
                          'EQ',
                          'LPAREN',
                          'IDENTIFIER',
                          'COMMA',
                          'STRING',
                          'RPAREN',
                          'COMMA',
                          'OR',
                          'LPAREN',
                          'IDENTIFIER',
                          'COMMA',
                          'LT',
                          'LPAREN',
                          'IDENTIFIER',
                          'COMMA',
                          'NUMBER',
                          'RPAREN',
                          'RPAREN',
                          'RPAREN'], tokenTypes, "check token result")
