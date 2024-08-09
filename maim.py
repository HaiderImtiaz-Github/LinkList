class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1
   
   
    def append(self, value):
        new_node = Node(value)
        
        if self.head is not None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.lenght += 1


    def my_pop(self):
        temp = self.head
        if temp is not None:
            while temp.next.next is not None:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
        else:
            pass



    def pop(self):
        if self.lenght == 0:
            return None
        temp = self.head
        pre = self.head
        
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.lenght-=1
        if self.lenght==0:
            self.head=self.tail=None
        return temp.value
    

   
   
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next



my_linklist = LinkList(0)
my_linklist.append(1)
my_linklist.append(2)
my_linklist.append(3)
my_linklist.append(4)
my_linklist.print_list()
print(my_linklist.pop())
print("---------------------")
my_linklist.print_list()
print(my_linklist.pop())
print("---------------------")
my_linklist.print_list()
print(my_linklist.pop())

print("---------------------")
my_linklist.print_list()
print(my_linklist.pop())

print("---------------------")
my_linklist.print_list()
print(my_linklist.pop())

print("---------------------")
my_linklist.print_list()
print(my_linklist.pop())

print("---------------------")
my_linklist.print_list()
print(my_linklist.pop())

print("---------------------")
my_linklist.print_list()
print(my_linklist.pop())

print("---------------------")
my_linklist.print_list()
