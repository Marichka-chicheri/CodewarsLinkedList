from preloaded import Node

def swap_pairs(head):

    if not head or not head.next:
        return head
    
    empty = Node(0)
    empty.next = head
    last_node = empty
    
    while last_node.next is not None and last_node.next.next is not None:

        node1 = last_node.next
        node2 = last_node.next.next

        last_node.next = node2
        
        node1.next = node2.next
        node2.next = node1
        
        last_node = node1
        
    return empty.next
