class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    if head is None:
        new_node = Node(data)
        new_node.next = None
        return new_node
    
    cur_node = head

    while True:
        if cur_node.next is None:
            new_node = Node(data)
            new_node.next = None
            cur_node.next = new_node
            return head

        if cur_node == head and data < cur_node.data:
            new_node = Node(data)
            new_node.next = head
            return new_node

        if cur_node.data < data < cur_node.next.data:
            new_node = Node(data)
            new_node.next = cur_node.next
            cur_node.next = new_node
            return head
        
        cur_node = cur_node.next
