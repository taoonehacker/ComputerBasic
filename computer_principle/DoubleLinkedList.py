#! -*- encoding=uft-8 -*-

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        val = '{%d:%d}' % (self.key, self.value)
        return val

    def __repr__(self):
        val = '{%d:%d}' % (self.key, self.value)
        return val


class DoubleLinkedList:
    def __init__(self, capacity=0xffff):
        self.capacity = capacity
        self.head = None
        self.tail = Node
        self.size = 0

    # 向头部增加节点
    def __add_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.head.prev = None
            self.head.next = None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        self.size += 1

    # 从尾部添加节点
    def __add_tail(self, node):
        if not self.tail:
            self.tail = node
            self.head = node
            self.tail.next = None
            self.tail.prev = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None

        self.size += 1

    def __del__tail(self):
        pass

    def __del__head(self):
        pass

    # 任意节点删除
    def __remove(self, node):
        if not node:
            node = self.tail
        if node == self.tail:
            self.__del__tail()
        elif node == self.head:
            self.__del_head()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        return node
