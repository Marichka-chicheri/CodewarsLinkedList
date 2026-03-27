from preloaded import Node

def get_nth(node, index):
    if index < 0 or node is None:
        raise ValueError
    
    counter = 0
    probe = node
    while probe is not None:
        counter += 1
        probe = probe.next
        
    if counter-1 < index:
        raise ValueError
    
    while index > 0:
        node = node.next
        index -= 1
    
    return node
