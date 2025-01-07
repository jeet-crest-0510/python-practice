class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def traversal(head):
    temp = head
    while temp is not None:
        print(temp.data)
        temp = temp.next

def insert_begin(head, value):
    node = Node(value)
    node.next = head
    head = node

    return head

def insert_end(head, value):
    node = Node(value)
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = node

    return head  #

def insert_pos(head, value, pos):
    node = Node(value)
    temp = head
    prev = temp
    p = 1

    while temp is not None and p != pos:
        prev = temp
        temp = temp.next
        p+=1
    
    if p!=pos:
        print("Position doesn't Exist!!")
    else:
        node.next = temp
        prev.next = node

    return head


if __name__ == "__main__":
    first = Node(1)
    second = Node(2)
    third = Node(3)

    l = LinkedList()
    l.head = first
    first.next = second
    second.next = third

    traversal(l.head)

    print("Inserting value at begin: ")
    l.head = insert_begin(l.head, 5)
    traversal(l.head)

    print("Inserting value at end: ")
    l.head = insert_end(l.head, 10)
    traversal(l.head)

    print("Inserting value at Position 4: ")
    l.head = insert_pos(l.head, 20, 4)
    traversal(l.head)
    print("Inserting value at Position 10: ")
    l.head = insert_pos(l.head, 20, 10)
    traversal(l.head)