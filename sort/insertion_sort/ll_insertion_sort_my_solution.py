class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # finally did it. 
    # not only that i've done it but i've switched the 
    # whole node instead of only the values
    def insertion_sort(self):
        if self.length < 2:
            return
        
        temp = self.head
        self.head = Node(0)
        self.head.next = temp

        current = self.head.next.next
        prev = self.head.next

        for _ in range(self.length - 1):
            if current.value < prev.value:
                prev.next = current.next

                watcher = self.head
                while watcher.value < current.value:
                    if watcher.next.value >= current.value:
                        current.next = watcher.next 
                        watcher.next = current
                    watcher = watcher.next
                current = prev.next
            else:
                prev = current
                current = prev.next

        temp = self.head
        self.head = self.head.next
        temp.next = None

        # track tail
        self.tail = self.head
        while self.tail.next:
            self.tail = self.tail.next




my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(2)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

# print("Linked List Before Sort:")
# my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

