import json

f1 = open('Practice Exercise\GFG\dict.txt','w')

dict = {
    "name": "jeet",
    "age": 21
}

f1.write(json.dumps(dict))

for d in dict:
    f1.write('\n%s: %s\n' % (d, dict[d]))

f1.write(str(dict))
f1.close()