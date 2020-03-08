
class Node:

    def __init__(self,val):
        self.val = val
        self.next = None

    def __str__(self):

        list_ = []
        curr = self
        while(curr!= None):
            list_.append(curr.val)
            curr = curr.next
        return str(list_)

def reverse(head):

    prev = None
    curr = head
    while( curr != None):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print(head)
head = reverse(head)
print(head)
