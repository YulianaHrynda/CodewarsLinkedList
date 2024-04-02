class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    input_ = s.split(' -> ')
    initial_node = Node(int(input_[0])) if input_[0] != "None" else None
    cur_node = initial_node
    
    for item in input_[1:]:
        if item == "None":
            cur_node.next = None
        else:
            cur_node.next = Node(int(item))
            cur_node = cur_node.next
    return initial_node
