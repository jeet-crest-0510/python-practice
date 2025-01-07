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

def search(head, tail, val):
    temp = head
    pos = 1
    while temp is not tail and temp.data != val:
        temp = temp.next
        pos += 1
    
    if temp.data == val:
        print(f"Value: {val} found at position {pos}")
    else:
        print("Value not found!!")

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
    search(cl.head, cl.tail, 3)
    search(cl.head, cl.tail, 4)
    search(cl.head, cl.tail, 5)