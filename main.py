class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
   
    def append(self, value):
        new_node = Node(value)
        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        return f'Removing: {temp.value}'
    
    def pop_first(self):
        if self.length == 0:
            return False
        temp = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp 
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.length += 1
        return True

    def get(self, index):
        if 0 <= index < self.length:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            return False
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return temp
        else:
            return False

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        pre = self.get(index - 1)
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        
        if index == 0:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return True
        
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None   
        
        if index == self.length - 1:
            self.tail = pre
        
        self.length -= 1
        return True
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linklist = LinkList(0)
my_linklist.append(1)
my_linklist.append(2)
my_linklist.append(3)
my_linklist.append(4)
print("Original List:")
my_linklist.print_list()

my_linklist.reverse()
print("Reversed List:")
my_linklist.print_list()
