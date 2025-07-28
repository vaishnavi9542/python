from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
arr=[3,5,6,7,8,4,12,45]
def create_Binary(arr,root,i,n):
    if i<=n:
        temp=Node(arr[i-1])
        root=temp
        root.left=create_Binary(arr,root.left,2*i,n)
        root.right=create_Binary(arr,root.right,2*i+1,n)
        return root
def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
def levelorder(root):
    if root is None:
        return
    result=[]
    queue=[]
    queue.append(root)
    while queue:
        result.append(queue[0].data)
        root=queue.pop(0)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    return result
def search_pre(root,val):
    if root is None:
        return False
    if root.data==val:
        return True
    return search_pre(root.left,val) or search_pre(root.right,val)
def search_post(root,val):
    if root is None:
        return False
    if root.left.data==val:
        return True
    return search_pre(root.right,val) or search_pre(root,val)
def search_in(root,val):
    if root is None:
        return False
    if root.left==val:
        return True
    return search_pre(root,val) or search_pre(root.right,val)

def search_levelorder(root,val):
    if root is None:
        return False
    queue=[]
    queue.append(root)
    while queue:
        root=queue.pop(0)
        if root.data==val:
            return True
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    return False
root=None
binary_tree=create_Binary(arr,root,1,len(arr))
print(preorder(binary_tree))
print(postorder(binary_tree))
print(inorder(binary_tree))
print(levelorder(binary_tree))
print(search_pre(binary_tree,6))
print(search_post(binary_tree,6))
print(search_in(binary_tree,6))
print(search_levelorder(binary_tree,6))
