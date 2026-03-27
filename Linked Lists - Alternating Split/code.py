class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    # Your code goes here.
    if not head or not head.next:
        raise ValueError

    n_head1 = Node(0)
    n_head2 = Node(0)
    
    probe = head
    prev1 = n_head1
    prev2 = n_head2
    count = 0

    while probe is not None:
        next_node = Node(probe.data)
        next_node.next = None

        if count % 2 == 0:
            prev1.next = next_node
            prev1 = next_node

        else:
            prev2.next = next_node
            prev2 = next_node

        probe = probe.next
        count += 1

        
    return Context(n_head1.next, n_head2.next)
