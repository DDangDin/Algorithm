class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self): # create tree
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root is not None

    def _insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        return node
    
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            node.data = BinarySearchTree._get_min_data(node.right)
            node.right = self._delete(node.right, node.data)

        return node

    @classmethod
    def _get_min_val(cls, node):
        min_val = node.data
        while node.left:
            min_val = node.left.data
            node = node.left
        return min_val

    # traversal
    # 중위 순회
    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(n.data, '', end='') # visit node
            if n.right:
                self.inorder(n.right)

    def preorder(self, n):
        if n != None:
            print(n.data, '', end='') # visit node
            if n.left:
                self.preorder(n.left) # traversal left sub tree
            if n.right:
                self.preorder(n.right) # traversal right sub tree

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(n.data, '', end='') # visit node




n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)


tree = BST()
tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8

# in-order
print(tree.inorder(tree.root))
# pre-order
print(tree.preorder(tree.root))
# post-order
print(tree.postorder(tree.root))



