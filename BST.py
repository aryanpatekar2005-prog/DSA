#BST using linkedlist
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,new_node):
        if self.root is None:
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right

    def Inorder(self,rt): #root=rt
        if rt is None:
            return
        else:
            self.Inorder(rt.left)
            print(rt.data,end=" ")
            self.Inorder(rt.right)

    def Preorder(self,rt): #root=rt
        if rt is None:
            return
        else:
            print(rt.data,end=" ")
            self.Preorder(rt.left)
            self.Preorder(rt.right)

    def Postorder(self,rt): #root=rt
        if rt is None:
            return
        else:
            self.Postorder(rt.left)
            self.Postorder(rt.right)
            print(rt.data,end=" ")
    
b1=BST()
b1.insert(Node(100))
b1.insert(Node(40))
b1.insert(Node(0))
b1.insert(Node(450))
b1.insert(Node(65))
b1.insert(Node(300))
b1.Inorder(b1.root)
print("\n")
b1.Preorder(b1.root)
print("\n")
b1.Postorder(b1.root)
print("\n")