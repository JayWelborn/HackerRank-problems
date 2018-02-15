"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

# This is a "method-only" submission.
# You only need to complete this method.


def InsertNth(head, data, position):
    if not head:
        return Node(data=data)
    elif position == 0:
        return Node(data=data, next_node=head)
    else:
        current_node = head
        for i in range(position - 1):
            current_node = current_node.next
        if current_node.next:
            current_node.next = Node(data=data, next_node=current_node.next)
        else:
            current_node.next = Node(data=data)
        return head
