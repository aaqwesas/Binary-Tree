
class Node:
    def __init__(self,val = 0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
        
def inorder2(node):
    if node is None:
        return
    inorder2(node.left)
    print(node.val)
    inorder2(node.right)
    
def preorder2(node):
    if node is None:
        return
    print(node.val)
    preorder2(node.left)
    preorder2(node.right)

def postorder2(node):
    if node is None:
        return
    postorder2(node.left)
    postorder2(node.right)
    print(node.val)
    
def inorder(root):
    res = []
    def ino(node):
        if node is None:
            return
        res.append(node.val)
        inorder2(node.left)
        ino(node.right)
    ino(root)
    return res

def preorder(root):
    res = []
    def pre(node):
        if node is None:
            return
        res.append(node.val)
        pre(node.left)
        pre(node.right)
    pre(root)
    return res
    
def postorder(root):
    res = []
    def post(node):
        if node is None:
            return
        post(node.left)
        post(node.right)
        res.append(node.val)
    post(root)
    return res
    
def inorder_iterative(node):
    res = []
    curr = root
    stack = []
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack.pop()
            res.append(temp.val)
            curr = temp.right
    return res
            
def preorder_iterative(node):
    res = []
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr:
            res.append(curr.val)
            stack.append(curr.right)
            stack.append(curr.left)
    return res

def postorder_iterative(node):
    res = []
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr:
            res.append(curr.val)
            stack.append(curr.left)
            stack.append(curr.right)
    return res[::-1]
            
def morris_preorder(node):
    answer = []
    curr = root  
    while curr:
        if not curr.left:
            answer.append(curr.val)
            curr = curr.right
        else:
            last = curr.left
            while last.right and last.right != curr:
                last = last.right
            if not last.right:
                answer.append(curr.val)
                last.right = curr
                curr = curr.left
            else:
                last.right = None
                curr = curr.right
    return answer

def morris_inorder(node):
    ans = []
    curr = root
    while curr:
        if not curr.left:
            ans.append(curr.val)
            curr = curr.right
        else:
            pointer = curr.left
            while pointer.right != curr and pointer.right != None:
                pointer = pointer.right
            if not pointer.right:
                pointer.right = curr
                curr = curr.left
            else:
                pointer.right = None
                ans.append(curr.val)
                curr = curr.right
    return ans
            
def morris_postorder(node):
    ans = []
    curr = root  
    while curr:
        if not curr.right:
            ans.append(curr.val)
            curr = curr.left
        else:
            last = curr.right
            while last.left and last.left != curr:
                last = last.left
            if not last.left:
                ans.append(curr.val)
                last.left = curr
                curr = curr.right
            else:
                last.left = None
                curr = curr.left
    return ans[::-1]
            
root = Node(12)
root.left = Node(6)
root.right = Node(4)
