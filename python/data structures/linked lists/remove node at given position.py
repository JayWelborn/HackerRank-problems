"""
 Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Delete(head, position):
    if position == 0:
        head = head.next

    else:
        node = head

        # move to 1 before node to be deleted
        for i in range(position - 1):
            node = node.next

        if node.next.next:
            new_next = node.next.next
            node.next = None
            node.next = new_next
        else:
            node.next = None

    return head
