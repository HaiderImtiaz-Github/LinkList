# import math

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node

        
#     def append(self, value):
#         new_node = Node(value)
#         if self.head == None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         return True
        

#     def my_find_middle_node(self):
#         pri = temp = self.head
#         i = 0
#         while temp:
#             temp = temp.next
#             i += 1
        
#         if i % 2 != 0:
#             iteration = math.ceil(i / 2)
#         else:
#             iteration = i // 2 + 1
        
#         for _ in range(iteration - 1):
#             pri = pri.next
        
#         return pri
    
#     def find_middle_node(self):
#         pri = temp = self.head
#         i = 0
#         while temp is not None and temp.next is not None:
#             pri = pri.next
#             temp = temp.next.next
#         return pri
#     def has_loop(self):
#         slow=fast=self.head
#         while fast is not None and fast.next is not None:
#             slow =slow.next
#             fast = fast.next.next
#             if slow==fast:
#                 return True
#         return False






# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)




# print( my_linked_list.find_middle_node().value )



# """
#     EXPECTED OUTPUT:
#     ----------------
#     3
    
# """
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        difference = end_index - start_index
        pri =temp = fwd = self.head
        for _ in range(difference):
            fwd = fwd.next
        if difference < 2:
            return
        else:
            for index in range(self.length):
                if index > start_index and index <end_index:
                    temp_pri = pri
                    temp_start = temp
                    temp_end = fwd
                    temp_pri.next = fwd
                    temp_end.next = temp_start.next 
                    temp_start.next = fwd.next
                pri = temp
                temp=temp.next
                if fwd.next:
                    fwd = fwd.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
