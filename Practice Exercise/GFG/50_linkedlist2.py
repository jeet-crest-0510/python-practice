class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def traversal(head):
    while head.next != None:
        print(head.data)
        head = head.next
    print(head.data)

def search(head, value):
    p = 1
    temp = head
    while temp.next != None:
        if temp.data == value:
            print(f"Value: {value} found at position {p}")
            return
        temp = temp.next
        p+=1

    if temp.data == value:
        print(f"Value: {value} found at position {p}")
    else:
        print(f"Value: {value} does not exist!!")        

if __name__ == "__main__":
    first = Node(1)
    second = Node(2)
    third = Node(3)

    l = LinkedList()
    l.head = first
    first.next = second
    second.next = third

    search(l.head, 1)
    search(l.head, 2)
    search(l.head, 3)
    search(l.head, 5)

