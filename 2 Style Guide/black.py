dict = {1: "a", 2: "b", 3: "c"}


class Computer:

    # Constructor for Initializing
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(f"Config is: {self.cpu}, {self.ram}GB Ram, 512GB Rom")


comp1 = Computer("i7", 16)
comp1.config()

a = [3, 4, 5]
b = a

# assign the variable "a" to a new list without changing "b"
a = [i + 3 for i in a]

print(a)
print(b)