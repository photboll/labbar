
class Node:
    def __init__(self,value,next=None):
        self.val = value
        self.next = next
class LinkedQ:
    def __init__(self,first_node,last_node):
        self.__first = first_node
        self.__last = last_node

    def is_empty(self):
        return (self.__first == None and self.__last == None)

    def enqueue(self,val):
        new_node = Node(val)
        if self.is_empty():
            self.__first = new_node
            self.__last = new_node
        else:
            new_node.next = self.__last

    def dequeue(self):
        current_node = self.__last
        if self.__first == self.__last:
            self.__first = None
            self.__last = None
            return current_node.val
        else:
            while current_node.next.next != None :
                current_node = current_node.next
            first_node = current_node.next
            current_node.next = None
            self.__first = current_node
            return first_node.val
