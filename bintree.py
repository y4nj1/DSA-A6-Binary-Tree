class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exists

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
    
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

letters = ["G", "I", "A", "N", "C", "A", "R", "L", "O", "B", "I", "R", "O", "N", "E", "S", "T", "R", "E", "L", "L", "A"]
letters_tree = build_tree(letters)

numbers = [53, 59, 63, 91, 64, 57, 39, 78, 18, 9, 17, 30, 45, 33, 39, 27, 22, 10, 19, 15, 40, 47]
numbers_tree = build_tree(numbers)


print("The sample letter list is:",letters)
print('='*30)
print("In-order traversal gives this sorted list:",letters_tree.in_order_traversal())
print('='*30)
print("Post-order traversal gives this sorted list:",letters_tree.post_order_traversal())
print('='*30)
print("Pre-order traversal gives this sorted list:",letters_tree.pre_order_traversal())
print('='*30)
print("Is the letter E included in the list?",letters_tree.search("E"))
print('='*30)
print("Is the letter Y included in the list?",letters_tree.search("Y"))
print('='*30)
print("Minimum Letter:",letters_tree.find_min())
print('='*30)
print("Maximum Letter:",letters_tree.find_max())
print('='*30)
print()
print()
print("The sample number list is:",numbers)
print('='*30)
print("Minimum Number:",numbers_tree.find_min())
print('='*30)
print("Maximum Number:",numbers_tree.find_max())
print('='*30)
print("Sum:", numbers_tree.calculate_sum())
print('='*30)