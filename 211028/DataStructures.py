# class Node:
#     def __init__(self, data, left=None, right=None):
#         self.left = left
#         self.right= right
#         self.data=data
#     def __repr__(self):
#         return str(self.data)
#
#
# n3=Node(3)
# n4=Node(4)
# n1=Node(1,n3,n4)
# n5=Node(5)
# n2=Node(2,n5)
# n0=Node(0,n1,n2)
#
def preOrderTraversal(node):
    print(node.data)
    if node.left:
        preOrderTraversal(node.left)
    if node.right:
        preOrderTraversal(node.right)

    return
#
# preOrderTraversal(n0)
#
# def inOrderTraversal(node):
#     if node.left:
#         inOrderTraversal(node.left)
#     print(node)
#     if node.right:
#         inOrderTraversal(node.right)
#
# print()
# inOrderTraversal(n0)
#
# def postOrderTraversal(node):
#     if node.left:
#         postOrderTraversal(node.left)
#     if node.right:
#         postOrderTraversal(node.right)
#     print(node)
#
# print()
# postOrderTraversal(n0)

class BinarySearchTree:
    def __init__(self):
        self.root=None
    def insert(self, node, data):
        if node == None:
            return Node(data)
        if data == node.data:
            return node
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def search(self, node, value):
        if node.data == value:
            print(value)
            return node
        elif node.data > value:
            if node.left:
                return self.search(node.left, value)
            return None
        elif node.data < value:
            if node.right:
                return self.search(node.right, value)
            return None
        return

    def delete(self, node, value):

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

bst = BinarySearchTree()
data = [10,4,11,2,7,1,3,5,6]
for i in data:
    bst.root = bst.insert(bst.root, i)

print(bst.search(bst.root, 8))