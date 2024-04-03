class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def loop_size(node):
    fast_node = node.next.next
    slow_node = node.next

    while fast_node != slow_node:
        fast_node = fast_node.next.next
        slow_node = slow_node.next
    
    counter = 1
    slow_node = slow_node.next
    while slow_node != fast_node:
        slow_node = slow_node.next
        counter += 1
    return counter
