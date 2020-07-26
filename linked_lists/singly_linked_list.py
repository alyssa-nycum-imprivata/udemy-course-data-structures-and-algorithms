class LinkedListNode(object):

    def __init__(self,value):

        self.value = value
        self.nextnode = None

a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)

a.nextnode = b
b.nextnode = c

def cycle_check(node):

    marker1 = node
    marker2 = node
    
    while marker2 != None and marker2.nextnode != None:

        marker1 - marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return print(True)

    return print(False)