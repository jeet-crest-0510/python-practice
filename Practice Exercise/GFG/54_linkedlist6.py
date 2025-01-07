class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def forward_traversal(head):
  
    curr = head

    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def backward_traversal(tail):
  
    curr = tail
 
    while curr is not None:
        print(curr.data, end=" ")       
        curr = curr.prev       
    print()

def search(head, val):
    temp = head
    p = 1

    while temp and temp.data != val:
        temp = temp.next
        p += 1

    if temp is not None and temp.data == val:
        print(f"Value: {val} found at position {p}")
    else:
        print("Value not found!!")


if __name__ == "__main__":
  
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    print("Forward Traversal:")
    forward_traversal(head)

    print("Backward Traversal:")
    backward_traversal(third)

    search(head, 2)
    search(head, 3)
    search(head, 4)