""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    if head is None:
        return Node(data)

    probe = head
    prev_data = probe.data
    prev_node = probe

    if data < prev_data:
        new_node = Node(data)
        new_node.next = probe
        head = new_node
        return head

    while probe is not None:
        if prev_data < data < probe.data:
            new_node = Node(data)
            prev_node.next = new_node
            new_node.next = probe
            break
            
        prev_node = probe
        prev_data = probe.data
        probe = probe.next
    
    if probe is None:
        prev_node.next = Node(data)
        
    return head
