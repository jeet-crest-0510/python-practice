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

first = Node(1)
second = Node(2)
third = Node(3)

# print(f"First: {first.data}")
# print(f"Second: {second.data}")
# print(f"Third: {third.data}")

l = LinkedList()

l.head = first

first.next = second

second.next = third

traversal(l.head)

# Node Data
print(f"Head: {l.head.data}")
print(f"Second: {l.head.next.data}")
print(f"Third: {l.head.next.next.data}")

# Node Addresses
# print(f"Head: {l.head}")
# print(f"Second: {l.head.next}")
# print(f"Third: {l.head.next.next}")
