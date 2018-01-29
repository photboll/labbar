class Node(object):
    def __init__(self,value,parent=None, left = None, right = None):
        self.parent = parent
        self.val = value
        self.left_child = left
        self.right_child = right

    def hasleft(self):
        return not(self.left_child == None)

    def hasright(self):
        return not(self.right_child == None)

class Bintree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __contains__(self,value):
        return self.finns(self.root,value)

    def finns(self,p,value):
        if p == None:
            return False
        elif value == p.val:
            return True
        elif value < p.val:
            return self.finns(p.left_child,value)
        elif value > p.val:
            return self.finns(p.right_child,value)

    def write(self):
        self.inorder(self.root)

    def inorder(self,root):
        if root != None:
            self.inorder(root.left_child)
            print(root.val)
            self.inorder(root.right_child)

    def put(self, value):
        if self.root != None:
            self.__putta(self.root, Node(value))
        else:
            self.root = Node(value)
        self.size += 1

    def __putta(self, root, new_node):
        if new_node.val < root.val :
            if root.hasleft():
                self.__putta(root.left_child, new_node)
            else:
                root.left_child = new_node
                new_node.parent = root
        else:
            if root.hasright():
                self.__putta(root.right_child, new_node)
            else:
                root.right_child = new_node
                new_node.parent = root
