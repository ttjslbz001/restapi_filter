import unittest

from demo.filter.interpreter import evaluate

class TestEvaluator(unittest.TestCase):

    def test_evaluate(self):
        context = {'name': 'dale', 'age': 25}

        eq_expression = {'op': 'eq', 'args': ['name', 'dale']}
        and_expression = {'op': 'and', 'args': [eq_expression, {'op': 'gt', 'args': ['age', 20]}]}
        or_expression = {'op': 'or', 'args': [eq_expression, {'op': 'lt', 'args': ['age', 20]}]}

        self.assertTrue(evaluate(eq_expression, context))  # Output should be True
        self.assertTrue(evaluate(and_expression, context))  # Output should be True
        self.assertTrue(evaluate(or_expression, context))

    def test_evaluate_hierarchical_key(self):
        data = {'driver': {'name': 'dale', 'age': 24}}

        eq_expression = {'args': [{'type': 'hierarchical_key', 'value': 'driver.age'}, 24],  'op': 'eq'}
        lt_expression = {'args': [{'type': 'hierarchical_key', 'value': 'driver.age'}, 28],  'op': 'lt'}
        gt_expression = {'args': [{'type': 'hierarchical_key', 'value': 'driver.age'}, 22],  'op': 'gt'}

        self.assertTrue(evaluate(eq_expression, data))  # Output should be True
        self.assertTrue(evaluate(lt_expression, data))  # Output should be True
        self.assertTrue(evaluate(gt_expression, data))