class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):

    def recursive(probe):
        if probe is None or not probe.next:
            return probe

        new_head = recursive(probe.next)

        probe.next.next = probe

        probe.next = None

        return new_head

    return recursive(head)
