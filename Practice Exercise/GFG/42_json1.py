import json 

class Student: 
	def __init__(self, roll_no, name, batch): 
		self.roll_no = roll_no 
		self.name = name 
		self.batch = batch 


class Car: 
	def __init__(self, brand, name, batch): 
		self.brand = brand 
		self.name = name 
		self.batch = batch 


if __name__ == "__main__": 
	
	s1 = Student("85", "Jeet", "Intern2025") 
	s2 = Student("124", "Jay", "Intern2025") 

	c1 = Car("Honda", "city", "2005") 
	c2 = Car("Honda", "Amaze", "2011") 

	jsonstr1 = json.dumps(s1.__dict__)    #Python object has an attribute which is denoted by __dict__ and this stores the object’s attributes. 
	jsonstr2 = json.dumps(s2.__dict__) 
	jsonstr3 = json.dumps(c1.__dict__) 
	jsonstr4 = json.dumps(c2.__dict__) 

	print(jsonstr1) 
	print(jsonstr2) 
	print(jsonstr3) 
	print(jsonstr4) 
