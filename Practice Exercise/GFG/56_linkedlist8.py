class Node:
    def __init__(self,data): 
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def traversal(head, tail):
    temp = head
    while temp is not tail:
        print(temp.data)
        temp = temp.next
    print(temp.data)

def insert_begin(head, tail, val):

    node = Node(val)

    if head is None:
        return node
    
    tail.next = node
    node.next = head
    head = node

    return head, tail

def insert_end(head, tail, val):
    node = Node(val)
    temp = head

    tail.next = node
    node.next = head
    tail = node

    return head, tail

def insert_pos(head, tail, val, pos):
    node = Node(val)
    temp = head
    prev = temp
    p = 1

    if pos == 1:
        return insert_begin(head, tail, val)

    while temp is not tail:
        if p == pos:
            node.next = temp
            prev.next = node
            return head, tail
        prev = temp
        temp = temp.next
        p += 1

    # if pos > 10:
    #     print(f"P: {p}")

    if temp is tail and p == pos:
        node.next = temp
        prev.next = node
        return head, tail
    elif p+1 == pos:
        return insert_end(head, tail, val)
    elif pos > p:
        print("Invalid Position!!")
    
    return head, tail

if __name__ == "__main__":
    cl = CircularLinkedList()
    cl.head = Node(1)
    second = Node(2)
    cl.head.next = second
    third = Node(3)
    second.next = third
    fourth = Node(4)
    third.next = fourth
    cl.tail = fourth
    cl.tail.next = cl.head

    traversal(cl.head, cl.tail)

    print("Inserting 5 at begin: ")
    cl.head, cl.tail = insert_begin(cl.head, cl.tail, 5)
    traversal(cl.head, cl.tail)
    print("Inserting 6 at begin: ")
    cl.head, cl.tail = insert_begin(cl.head, cl.tail, 6)
    traversal(cl.head, cl.tail)

    print("Inserting 7 at end: ")
    cl.head, cl.tail = insert_end(cl.head, cl.tail, 7)
    traversal(cl.head, cl.tail)
    print("Inserting 8 at end: ")
    cl.head, cl.tail = insert_end(cl.head, cl.tail, 8)
    traversal(cl.head, cl.tail)

    print("Inserting 9 at pos 1: ")
    cl.head, cl.tail = insert_pos(cl.head, cl.tail, 9, 1)
    traversal(cl.head, cl.tail)
    print("Inserting 10 at pos 3: ")
    cl.head, cl.tail = insert_pos(cl.head, cl.tail, 10, 3)
    traversal(cl.head, cl.tail)
    print("Inserting 11 at pos 11: ")
    cl.head, cl.tail = insert_pos(cl.head, cl.tail, 11, 11)
    traversal(cl.head, cl.tail)
    print("Inserting 12 at pos 11: ")
    cl.head, cl.tail = insert_pos(cl.head, cl.tail, 12, 11)
    traversal(cl.head, cl.tail)
    print("Inserting 13 at pos 14: ")
    cl.head, cl.tail = insert_pos(cl.head, cl.tail, 13, 14)
    traversal(cl.head, cl.tail)

    print(f"Head value: {cl.head.data}")
    print(f"Tail value: {cl.tail.data}")