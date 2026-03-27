def loop_size(node):
    fast = node
    slow = node

    while fast and fast.next:
        
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:

            count = 1
            fast = fast.next

            while fast != slow:
                fast = fast.next
                count += 1

            return count

    return 0
