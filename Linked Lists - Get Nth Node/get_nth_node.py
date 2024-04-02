class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None:
        raise ValueError
    
    if index < 0:
        raise IndexError

    for ind in range(1, index + 1):
        if not node and ind < index:
            raise IndexError
        node = node.next

    if not node:
        raise IndexError
    return node
