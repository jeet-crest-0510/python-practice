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

def delete_begin(head):
    temp = head
    head = head.next
    del temp
    return head

def delete_end(head):
    temp = head
    prev = temp
    while temp.next is not None:
        prev = temp
        temp = temp.next
    prev.next = None
    del temp
    return head

def delete_pos(head, pos):
    temp = head
    prev = head
    p = 1

    while temp.next is not None and p != pos:
        prev = temp                
        temp = temp.next           
        p += 1
    
    if p != pos:
        print("Position is not Valid")
    else:
        prev.next = prev.next.next
        # del temp
    return head

if __name__ == "__main__":
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    l = LinkedList()
    l.head = first
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = None

    traversal(l.head)

    # print("Deleting value at begin: ")
    # l.head = delete_begin(l.head)
    # traversal(l.head)

    # print("Deleting value at end: ")
    # l.head = delete_end(l.head)
    # traversal(l.head)

    print("Deleting value at position 2: ")
    l.head = delete_pos(l.head, 2)
    traversal(l.head)
    print("Deleting value at position 4: ")
    l.head = delete_pos(l.head, 4)
    traversal(l.head)
    print("Deleting value at position 3: ")
    l.head = delete_pos(l.head, 3)
    traversal(l.head)