class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError

    first_head = None
    second_head = None
    first_tail = None
    second_tail = None

    current = head
    count = 1

    while current:
        new_node = Node(current.data)

        if count % 2 == 1:
            if first_head is None:
                first_head = new_node
                first_tail = new_node
            else:
                first_tail.next = new_node
                first_tail = new_node
        else:
            if second_head is None:
                second_head = new_node
                second_tail = new_node
            else:
                second_tail.next = new_node
                second_tail = new_node

        current = current.next
        count += 1

    return Context(first_head, second_head)
