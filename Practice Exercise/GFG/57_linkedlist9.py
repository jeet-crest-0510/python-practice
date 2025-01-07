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

def delete_begin(head, tail):
    if head == tail:
        del head
        del tail
        return None, None
    
    temp = head
    tail.next = head.next
    head = head.next
    del temp
    return head, tail

def delete_end(head, tail):
    temp = head
    while temp.next is not tail:
        temp = temp.next
    temp.next = head
    tail = temp
    del temp

    return head, tail

def delete_pos(head, tail, pos):
    if pos == 1:
        return delete_begin(head, tail)
    
    temp = head
    prev = temp
    p = 1

    while temp.next is not tail:
        if p == pos:
            prev.next = temp.next
            del temp
            return head, tail
        prev = temp
        temp = temp.next
        p += 1

    if temp.next == tail and p+1 == pos:
        return delete_end(head, tail)
    else:
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
    fifth = Node(5)
    fourth.next = fifth
    cl.tail = fifth
    cl.tail.next = cl.head

    traversal(cl.head, cl.tail)
    print(f"Head value: {cl.head.data}")
    print(f"Tail value: {cl.tail.data}")

    # cl.head, cl.tail = delete_begin(cl.head, cl.tail)
    # traversal(cl.head, cl.tail)
    # print(f"Head value: {cl.head.data}")
    # print(f"Tail value: {cl.tail.data}")

    # cl.head, cl.tail = delete_end(cl.head, cl.tail)
    # traversal(cl.head, cl.tail)
    # print(f"Head value: {cl.head.data}")
    # print(f"Tail value: {cl.tail.data}")

    print("Delete at pos 2: ")
    cl.head, cl.tail = delete_pos(cl.head, cl.tail, 2)
    traversal(cl.head, cl.tail)
    print(f"Head value: {cl.head.data}")
    print(f"Tail value: {cl.tail.data}")

    print("Delete at pos 1: ")
    cl.head, cl.tail = delete_pos(cl.head, cl.tail, 1)
    traversal(cl.head, cl.tail)
    print(f"Head value: {cl.head.data}")
    print(f"Tail value: {cl.tail.data}")

    print("Delete at pos 3: ")
    cl.head, cl.tail = delete_pos(cl.head, cl.tail, 3)
    traversal(cl.head, cl.tail)
    print(f"Head value: {cl.head.data}")
    print(f"Tail value: {cl.tail.data}")

    print("Delete at pos 3: ")
    cl.head, cl.tail = delete_pos(cl.head, cl.tail, 3)
    traversal(cl.head, cl.tail)
    print(f"Head value: {cl.head.data}")
    print(f"Tail value: {cl.tail.data}")