file = open('Practice Exercise\GFG\dict.txt') 

content = file.readlines() 

print("second line") 
print(content[1]) 

print("first three lines") 
print(content[0:3]) 

file.close()