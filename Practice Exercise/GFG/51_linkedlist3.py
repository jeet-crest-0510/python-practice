class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

def length(head):
    temp = head
    count = 0

    while temp is not None:
        count+=1
        temp = temp.next
    
    print(f"Length of LinkedList: {count}")


if __name__ == "__main__":
    first = Node(1)
    second = Node(2)
    third = Node(3)

    l = LinkedList()
    l.head = first
    first.next = second
    second.next = third

    length(head= l.head)
