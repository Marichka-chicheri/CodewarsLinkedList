from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None

    list_repr = list_repr.split(" -> ")

    head = Node(int(list_repr[0]))
    prev_node = head

    for i in list_repr[1:]:
        if i == "None":
            break
        if (i.strip()).isdigit():
            data = int(i)
        else:
            data = i

        new_node = Node(data)
        prev_node.next = new_node
        prev_node = new_node
        
    return head
