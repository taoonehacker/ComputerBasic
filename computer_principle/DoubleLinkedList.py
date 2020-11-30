# -*- encoding=utf-8 -*-
from computer_principle.Node import Node


class DoubleLinkedList:
    def __init__(self, capacity=0xffff):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    def __remove_head(self):
        if not self.head:
            return
        node = self.head
        if node.next:
            node.next.prev = None
            self.head = node.next
        else:
            self.head = self.tail = None
        self.size -= 1
        return node

    def __remove_tail(self):
        if not self.tail:
            return
        node = self.tail
        if node.prev:
            node.prev.next = None
            self.tail = node.prev
        else:
            self.head = self.tail = None
        self.size -= 1
        return node

    def __remove(self, node):
        if not node:
            node = self.tail
        if node == self.head:
            return self.__remove_head()
        elif node == self.tail:
            return self.__remove_tail()
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.size -= 1
        return node

    def __append_head(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size += 1

    def __append_tail(self, node):
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def pop(self):
        return self.__remove_head()

    def append(self, node):
        self.__append_tail(node)

    def append_head(self, node):
        self.__append_head(node)

    def remove(self, node=None):
        return self.__remove(node)
