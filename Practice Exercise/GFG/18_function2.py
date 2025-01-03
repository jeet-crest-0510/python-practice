def info(name, age, marks=100):
    print('name: %s, age %d, marks %d' % (name,age,marks))

info('jeet',21)


def GFG(*args):
    for info in args:
        print(info)


GFG(["Hello from", "geeks", 25], ["Hello", "gfg", 26])


def GFG(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


GFG(name="geeks", n="- 25")
GFG(name="best", n="- 26")

# using kwargs
# in functions


def printValues(**kwargs):
	for key, value in kwargs.items():
		print("The value of {} is {}".format(key, value))


# driver code
if __name__ == '__main__':
	printValues(abbreviation="GFG", full_name="geeksforgeeks")
