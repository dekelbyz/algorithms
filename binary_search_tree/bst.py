class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        
        if not self.root:
            self.root = new_node
            return True
        
        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def __r_contains(self, current_node, value):
        if not current_node:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        elif value > current_node.value:
            return self.__r_contains(current_node.right, value)
    

    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        
        else:
            if not current_node.left and not current_node.right:
                return None
            
            elif not current_node.left:
                current_node = current_node.right

            elif not current_node.right:
                current_node = current_node.left
            
            else:
                sub_tree_min = self.min_value(current_node)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        
        return current_node

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)
    
        
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
        
    def r_contains(self, value):
        if self.root == None:
            self.root = Node(value)
        return self.__r_contains(self.root, value)

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value) 

############ TRAVERSAL ##################
    def BFS(self):
        # BFS - Breadth First Search
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return results
    def dfs_pre_order(self):
        # DFS - Depth First Search
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return results
    

    def dfs_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
    def dfs_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return results
            

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.BFS()) # [47, 21, 76, 18, 27, 52, 82]
print(my_tree.dfs_pre_order()) # [47, 21, 18, 17, 76, 52, 82]
print(my_tree.dfs_post_order()) # [18, 27, 21, 52, 82, 76, 47]
print(my_tree.dfs_in_order()) # [18, 21, 27, 47, 52,76, 82]