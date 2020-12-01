# -*- encoding=utf-8 -*-
from computer_principle.DoubleLinkedList import DoubleLinkedList
from computer_principle.Node import Node
from computer_principle.cache.ICache import ICache


class LFUNode(Node):
    def __init__(self, key, value):
        super(LFUNode, self).__init__(key, value)
        self.freq = 0


class LFUCache(ICache):
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}  # key与node的映射关系
        self.freq_map = {}  # 频率和链表的映射关系
        self.size = 0

    # 更新节点
    def __update_freq(self, node):
        freq = node.freq

        # 删除
        self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]

        # 更新
        freq += 1
        node.freq = freq
        if freq not in self.freq_map:
            self.freq_map[freq] = DoubleLinkedList()
        self.freq_map[freq].append(node)

    def set(self, key, value):
        if self.capacity == 0:
            return
        # 缓存命中
        if key in self.map:
            node = self.map.get(key)
            node.value = value
            self.__update_freq(node)
        # 缓存没命中
        else:
            if self.capacity == self.size:
                min_freq = min(self.freq_map)
                node = self.freq_map[min_freq].pop()
                del self.map[node.key]
                self.size -= 1
            node = LFUNode(key, value)
            node.freq = 1
            self.map[key] = node
            if node.freq not in self.freq_map:
                self.freq_map[node.freq] = DoubleLinkedList()
            self.freq_map[node.freq].append(node)
            self.size += 1

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map.get(key)
        self.__update_freq(node)
        return node.value
