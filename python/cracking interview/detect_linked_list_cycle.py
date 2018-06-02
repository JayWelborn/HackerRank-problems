"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    node = head
    nodes = set()
    while node:
        if node in nodes:
            return True
        nodes.add(node)
        node = node.next
    return False
    
