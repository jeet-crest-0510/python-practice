import re 

filenames = ["gfg.html", "geeks.xml", 
			"computer.txt", "geeksforgeeks.jpg"] 

for file in filenames: 
	match = re.search("\.xml$", file) 

	if match: 
		print("The file ending with .xml is:", 
			file) 
