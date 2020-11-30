import unittest

from computer_principle.DoubleLinkedList import DoubleLinkedList
from computer_principle.Node import Node
from computer_principle.cache.FIFOCache import FIFOCache
from computer_principle.cache.LRUCache import LRUCache


class DoubleLinkedListTestCase(unittest.TestCase):
    def test_node(self):
        node = Node(1, 1)
        self.assertEqual(node.key, 1)
        self.assertEqual(node.value, 1)

    def test_node(self):
        node1 = Node(1, 1)
        node2 = Node(2, 2)
        node1.next = node2
        node2.prev = node1
        self.assertEqual(node1.next.value, 2)
        self.assertEqual(node2.prev.value, 1)

    def test_double_linked_list(self):
        double_linked_list = DoubleLinkedList(10)
        self.assertEqual(double_linked_list.capacity, 10)
        self.assertEqual(double_linked_list.size, 0)

    def test_double_linked_list_pop_append(self):
        double_linked_list = DoubleLinkedList(10)
        for i in range(10):
            double_linked_list.append(Node(i, i))
        self.assertEqual(double_linked_list.pop().value, 0)

    def test_double_linked_list_append_head(self):
        double_linked_list = DoubleLinkedList(10)
        for i in range(10):
            double_linked_list.append(Node(i, i))
        node = Node(11, 11)
        double_linked_list.append_head(node)
        self.assertEqual(double_linked_list.pop().value, 11)

    def test_double_linked_list_remove(self):
        l = DoubleLinkedList(10)
        nodes = []
        for i in range(10):
            node = Node(i, i)
            nodes.append(node)
            l.append(node)
        node = l.remove(nodes[3])
        self.assertEqual(node.value, 3)

    def test_fifo_cache_set(self):
        fifo_cache = FIFOCache(2)
        fifo_cache.set(1, 1)
        fifo_cache.set(2, 2)
        self.assertEqual(fifo_cache.size, 2)
        self.assertEqual(fifo_cache.capacity, 2)

    def test_fifo_cache_get(self):
        fifo_cache = FIFOCache(2)
        fifo_cache.set(1, 1)
        fifo_cache.set(2, 2)
        self.assertEqual(fifo_cache.get(1), 1)
        fifo_cache.set(3, 3)
        self.assertEqual(fifo_cache.get(1), -1)
        self.assertEqual(fifo_cache.get(2), 2)
        self.assertEqual(fifo_cache.get(3), 3)
        fifo_cache.set(4, 4)
        self.assertEqual(fifo_cache.get(3), 3)
        self.assertEqual(fifo_cache.get(2), -1)

    def test_lru_cache_test(self):
        lru_cache = LRUCache(2)
        lru_cache.set(1, 1)
        lru_cache.set(2, 2)
        self.assertEqual(lru_cache.get(1), 1)
        lru_cache.set(3, 3)
        self.assertEqual(lru_cache.get(2), -1)
        self.assertEqual(lru_cache.get(1), 1)
        lru_cache.set(4, 4)
        self.assertEqual(lru_cache.get(3), -1)


if __name__ == '__main__':
    unittest.main()
