class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):

        s = ''
        temp = self.head
        while temp.next:
            s += str(temp.data) + ' -> '
            temp = temp.next
        s += str(temp.data)

        return s

if __name__ == "__main__":
    l1 = LinkedList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    l1.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4

    print(l1)