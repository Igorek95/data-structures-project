import unittest

from src.queue import Node
class TestNodeMethods(unittest.TestCase):
    def test_str_method(self):
        node = Node(5, None)
        self.assertEqual(str(node), "5")