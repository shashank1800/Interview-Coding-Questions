
class Node:

    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):

        list1 = []
        list2 = []
        curr = self
        
        while(curr.next!= None):
            list1.append(curr.val)
            curr = curr.next
        list1.append(curr.val)
        while(curr!= None):
            list2.append(curr.val)
            curr = curr.prev
        
        return str(list1) + str(list2)

def reverse(head):

    mem = None
    curr = head
    while( curr != None):
        temp = curr.next
        curr.next = mem
        curr.prev = temp
        mem = curr
        curr = curr.prev
    
    return mem
    
head = Node(1)

head.next = Node(2)
head.next.prev = head

head.next.next = Node(3)
head.next.next.prev = head.next

print(head)
head = reverse(head)
print(head)

