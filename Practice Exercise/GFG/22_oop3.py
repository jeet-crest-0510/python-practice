students = []

class Student:
    def __init__(self, name, roll, marks1, marks2):
        self.name = name
        self.roll = roll
        self.marks1 = marks1
        self.marks2 = marks2

    def display(self):
        print('Name: ', self.name)
        print('Roll number: ', self.roll)
        print('Marks1: ', self.marks1)
        print('Marks2: ',self.marks2)

    @classmethod
    def search(cls, rn):
        for i in range(len(students)):
            if students[i].roll == rn:
                return i

    @classmethod            
    def delete(cls, rn):
        i = Student.search(rn)

        if i:
            del students[i]
        
    @classmethod
    def update(cls, rn, Rn):
        i = Student.search(rn)
        students[i].roll = Rn
        return i

def accept(name, roll, marks1, marks2):
    obj = Student(name, roll, marks1, marks2)
    students.append(obj)

print("Operations used,")
print("""
      1. Accept Student details
      2. Display Student Details
      3. Search Details of a Student
      4. Delete Details of Student
      5. Update Student Details
      other: Exit
""")

while True:
    choice = int(input("\nEnter choice:"))

    if(choice == 1):
        name = input('\nEnter the name: ')
        roll = int(input('Enter Rollno: '))
        marks1 = int(input('Enter marks1: '))
        marks2 = int(input('Enter marks2: '))
        accept(name, roll, marks1, marks2)
        print('Added Successfully!')
    
    elif(choice == 2):
        print("\nList of Students")
        for i in range(students.__len__()):
            students[i].display()
            print()
    
    elif(choice == 3):
        rollno = int(input('\nEnter roll no to search: '))
        i = Student.search(rollno)
        
        students[i].display()
    
    elif(choice == 4):
        rollno = int(input('\nEnter roll no to delete: '))
        Student.delete(rollno)
        print('Deleted Successfully!!')
        print("List of Students")
        for i in range(students.__len__()):
            students[i].display()
    
    elif(choice == 5):
        rollno = int(input('\nEnter roll no to update: '))
        Rollno = int(input('Enter the updated roll no: '))
        i = Student.update(rollno, Rollno)
        print('Updated Successfully!!')
        students[i].display()
    
    else:
        print("Thank You !")
        break