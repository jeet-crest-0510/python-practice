import json
from collections import namedtuple

data = '{"Name": "Jeet", "Age": 21}'

print(data)
print(type(data))

d = json.loads(data)
print(d)
print(type(d))

x = json.loads(data, object_hook =
               lambda d : namedtuple('X', d.keys())
               (*d.values()))
print(x)
print(x.Name, x.Age)
print(type(x))