class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        # temp = self.head
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def pop(self):
        temp = self.head
        val = temp.data
        self.head = self.head.next
        self.head.prev = None
        del temp
        return val

    def print(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    def isempty(self):
        return self.head is None

    def top(self):
        if self.isempty():
            return False
        return self.head.data
    
    def size(self):
        c = 0
        temp = self.head
        while temp:
            c+=1
            temp = temp.next

        return c

if __name__ == "__main__":
    s1 = Stack()

    print(f"Is stack Empty? {s1.isempty()}")
    print(f"Size of stack: {s1.size()}")

    print("Push elements: ")
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(4)
    s1.print()

    print(f"Size of stack: {s1.size()}")

    print(f"Is stack Empty? {s1.isempty()}")

    val = s1.top()
    if val:
        print(f"Top Element: {val}")
    else:
        print("Stack is empty")

    val = s1.pop()
    print(f"Pop Element: {val}")
    val = s1.pop()
    print(f"Pop Element: {val}")
    s1.print()
