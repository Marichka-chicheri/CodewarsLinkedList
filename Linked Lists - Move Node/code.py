class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    # Your code goes here.
    if source is None:
        raise ValueError
        
    dest_node = Node(source.data)
    source = source.next
    
    dest_node.next = dest
    
    # Remember to return the context.
    return Context(source, dest_node)
