import unittest
from src.stack import Node, Stack

class TestStack(unittest.TestCase):

    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)

    def test_empty_stack_pop(self):
        stack = Stack()
        with self.assertRaises(ValueError):
            stack.pop()

    def test_multiple_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
