import math

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def my_find_middle_node(self):
        pri = temp = self.head
        i = 0
        while temp:
            temp = temp.next
            i += 1
        
        if i % 2 != 0:
            iteration = math.ceil(i / 2)
        else:
            iteration = i // 2 + 1
        
        for _ in range(iteration - 1):
            pri = pri.next
        
        return pri
    
    def find_middle_node(self):
        pri = temp = self.head
        i = 0
        while temp is not None and temp.next is not None:
            pri = pri.next
            temp = temp.next.next
        return pri
    def has_loop(self):
        slow=fast=self.head
        while fast is not None and fast.next is not None:
            slow =slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False






my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)




print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""