class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def right_View(root):
    
    que = [root]

    while que:
        temp_que = que
        que = []

        for ele in temp_que:
            if ele.left != None:
                que.append(ele.left)
            if ele.right != None:
                que.append(ele.right)

        print(temp_que[0].data)
        
        


root = Node(20)

root.left = Node(10)
root.left.left = Node(5)
root.left.right = Node(11)
root.left.right.right = Node(12)

root.right = Node(30)
root.right.left = Node(25)
root.right.right = Node(35)
root.right.left.left = Node(24)

right_View(root)
