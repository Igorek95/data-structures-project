import unittest

from src.stack import Stack


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

    def test_str_method(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(str(stack), "Stack: 3, 2, 1")

    def test_is_empty_method(self):
        empty_stack = Stack()
        non_empty_stack = Stack()
        non_empty_stack.push(1)

        self.assertTrue(empty_stack.is_empty())
        self.assertFalse(non_empty_stack.is_empty())
