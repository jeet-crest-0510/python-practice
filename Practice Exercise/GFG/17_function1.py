# explicit function
def fun(a, b):
    return a**b

# import required modules 
import inspect 

# use signature() 
print(inspect.signature(fun)) 

print(fun.__name__)

global a; 
a=10

while True:
    z=1
    break

b = 20

print(locals().keys())  # Get local variables
print(globals().keys())  # Get global variables