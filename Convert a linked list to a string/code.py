def stringify(node):
    new_str = ""
    while node is not None:
        new_str += str(node.data) + " -> "
        node = node.next
        
    return new_str + "None"
