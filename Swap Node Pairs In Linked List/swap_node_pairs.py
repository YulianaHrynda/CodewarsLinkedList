class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    prev_node = None
    cur_node = head

    while cur_node is not None and cur_node.next is not None:
        next_node = cur_node.next
        if prev_node:
            prev_node.next = next_node
        else:
            head = next_node
        cur_node.next = next_node.next
        next_node.next = cur_node
        prev_node = cur_node
        cur_node = cur_node.next
    return head
