# -*- encoding=utf-8 -*-
from computer_principle.DoubleLinkedList import DoubleLinkedList
from computer_principle.Node import Node
from computer_principle.cache.ICache import ICache


class FIFOCache(ICache):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}  # key 和 node的映射关系
        self.list = DoubleLinkedList(self.capacity)

    def set(self, key, value):
        if self.capacity == 0:
            return

        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value
            self.list.append(node)
        else:
            if self.size == self.capacity:
                node = self.list.pop()
                del self.map[node.key]
                self.size -= 1
            node = Node(key, value)
            self.list.append(node)
            self.map[key] = node
            self.size += 1

    def get(self, key):
        if key not in self.map:
            return -1
        else:
            node = self.map.get(key)
            return node.value
