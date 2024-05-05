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

    def merge(self, l2):
        dummy = Node(0)  # Dummy node to simplify edge cases
        tail = dummy

        node1 = self.head
        node2 = l2.head

        while node1 and node2:
            if node1.value < node2.value:
                tail.next = node1
                node1 = node1.next
            else:
                tail.next = node2
                node2 = node2.next
            tail = tail.next

        # Connect the remaining part of whichever list is not exhausted
        tail.next = node1 or node2
        self.head = dummy.next  # Update head to the start of the merged list

        # Update tail to the last element
        while tail.next:
            tail = tail.next
        self.tail = tail



            
# l1 = LinkedList(1)
# l1.append(3)
# l1.append(5)
# l1.append(7)


# l2 = LinkedList(2)
# l2.append(4)
# l2.append(4)
# l2.append(6)
# l2.append(8)
# l2.append(9)



l1 = LinkedList(1)
l1.append(2)
l1.append(8)
l1.append(10)


l2 = LinkedList(2)
l2.append(6)
l2.append(11)
l2.append(13)
l2.append(15)


l1.merge(l2)

l1.print_list()
print(F'HEAD: {l1.head.value}')
print(F'TAIL: {l1.tail.value}')


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""