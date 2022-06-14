# converted the letters of "tamerelsawaf" to
# their respective hex values and printed them in
# order to spell correctly in preorder traversal


# implement postorder traversal of binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
 
# postorder tree traversal
def printPostorder(root):
 
    if root:
        # recursion for child nodes
        printPostorder(root.left)
        printPostorder(root.right)
        # print the data
        print(root.val),
 
 
# preorder tree traversal
def printPreorder(root):
 
    if root:
 
        # print data of node
        print(root.val),
 
        # recursion for child nodes
        printPreorder(root.left)
        printPreorder(root.right)
 
 

root = Node(format(ord("t"), "x"))
root.left = Node(format(ord("a"), "x"))
root.right = Node(format(ord("a"), "x"))
root.left.left = Node(format(ord("m"), "x"))
root.left.right = Node(format(ord("e"), "x"))
root.right.left = Node(format(ord("w"), "x"))
root.right.right = Node(format(ord("a"), "x"))
root.right.right.left = Node(format(ord("f"), "x"))
root.left.left.left = Node(format(ord("e"), "x"))
root.left.left.right = Node(format(ord("r"), "x"))
root.left.right.left = Node(format(ord("l"), "x")) 
root.left.right.right = Node(format(ord("s"), "x"))
print ("the preorder traversal of binary tree gives the name spelled correctly in hex:")
printPreorder(root)

# doesn't work for "tamerelsawaf"
# print ("the postorder traversal:")
# printPostorder(root)


 
