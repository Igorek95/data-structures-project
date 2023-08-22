import unittest

from src.queue import Node, Queue
class TestNodeMethods(unittest.TestCase):
    def test_str_method(self):
        node = Node(5, None)
        self.assertEqual(str(node), "5")

    def test_enqueue_and_dequeue(self):
        queue = Queue()

        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')

        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertIsNone(queue.dequeue())