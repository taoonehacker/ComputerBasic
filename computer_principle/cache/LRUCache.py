# -*- encoding=utf-8 -*-
from computer_principle.DoubleLinkedList import DoubleLinkedList
from computer_principle.Node import Node
from computer_principle.cache.ICache import ICache


class LRUCache(ICache):
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.list = DoubleLinkedList(self.capacity)

    def set(self, key, value):
        if self.capacity == 0:
            return
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value
            self.list.append_head(node)
        else:
            node = Node(key, value)
            if self.list.size >= self.list.capacity:
                old_node = self.list.remove()
                self.map.pop(old_node.key)

            self.map[key] = node
            self.list.append_head(node)

    def get(self, key):
        if key not in self.map:
            return -1
        else:
            node = self.map.get(key)
            self.list.remove(node)
            self.list.append_head(node)
            return node.value
