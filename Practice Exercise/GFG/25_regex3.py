import re

def check(str, pattern):
	if re.search(pattern, str):
		print("Valid String")
	else:
		print("Invalid String")
		
pattern = re.compile('^[102345]+$')

check('52301', pattern)
check('6987', pattern)
