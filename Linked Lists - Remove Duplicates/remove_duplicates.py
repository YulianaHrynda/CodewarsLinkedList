class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    prev_node = head
    cur_node = prev_node.next

    while cur_node is not None:
        if prev_node.data == cur_node.data:
            prev_node.next = cur_node.next
            cur_node = prev_node.next
        else:
            prev_node = cur_node
            cur_node = cur_node.next

    return head
