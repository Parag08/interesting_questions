class Node:
    def __init__(self, value):
        self.left = self.right = None
        self.value = value

dict = {}

def zizagtraversal(root, level):
    if root is not None:
        if level in dict:
            dict[level].append(str(root.value))
        else:
            dict[level] = [str(root.value)]
        zizagtraversal(root.right, level + 1)
        zizagtraversal(root.left, level + 1)
    else:
        return

root = Node(1)
root.right = Node(2)
root.left = Node(3)
root.left.left = Node(7) 
root.left.right = Node(6) 
root.right.left = Node(5) 
root.right.right = Node(4) 
print("Zigzag Order traversal of binary tree is") 
zizagtraversal(root, 0)
str = ''
for level in dict:
    str = str + ' ' + ' '.join(dict[level][::-1])
print(str)