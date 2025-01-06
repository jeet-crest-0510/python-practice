f1 = open("Practice Exercise\GFG\input.txt", 'r')
# text = f1.readlines()
# print(text)

f2 = open("Practice Exercise\GFG\output.txt", 'w')
for r in f1:
    f2.write(r)

f1.close()
f2.close()