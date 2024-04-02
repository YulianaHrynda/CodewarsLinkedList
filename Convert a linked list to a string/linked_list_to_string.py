class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    current_node = node
    result = []

    while not current_node is None:
        result.append(str(current_node.data))
        current_node = current_node.next
    
    result.append("None")
    result = " -> ".join(result)
    return result
