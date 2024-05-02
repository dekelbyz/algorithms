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

    # the least efficient thing i've done in my life. dont judge.
    def merge(self, l2):
        node1 = self.head 
        node2 = l2.head 

        while node1 and node2:
            if not node1.next:
                node1.next = node2
                break

            if node1.value < node2.value:
                while node1.next and node1.next.value < node2.value:
                    node1 = node1.next
                l2.head = node2.next
                node2.next = node1.next
                node1.next = node2
                node1 = node2.next
            else:
                if node1 == self.head:
                    self.head = node2
                l2.head = node2.next

                prev = self.head
                while prev:
                    if prev.next != node1:
                        prev = prev.next
                    else:
                        prev.next = node2
                        break
                        
                node2.next = node1
            node2 = l2.head

        last_item = self.head
        while last_item:
            if not last_item.next:
                self.tail = last_item 
            last_item = last_item.next

        # take care of rest of list
        if node2 and node2 != self.tail and node2.next != self.tail:
            self.tail.next = node2
            self.tail = l2.tail


            
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