# importing important files
import json  #it is for storing students and if program ends not data should be deleted or vanished

# Student class for the storing the students
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
    
    def __str__(self):
        return f"""
                Name: {self.name}
                Age: {self.age}
                Student_ID: {self.student_id}"""
    
    # method for display the all students
    def display(self):
        print(self)

    # method for convert list object ot dictionary
    def to_dict(self):
        return self.__dict__

    # method for load dictionary to list object
    @classmethod
    def from_dict(cls, student_dict):
        name = student_dict["name"]
        age = student_dict["age"]
        student_id = student_dict["student_id"]

        return cls(name, age, student_id)

# Creating the student list
students = []

# function for saving data in json file.
def save_student(student):
    student_dict = []
    for student in students:
        student_dict.append(student.to_dict())

    with open("student.json", "w") as f:
        json.dump(student_dict, f)

# function for loading data from json file in list.
def load_students():
    with open("student.json", "r") as f:
        data = json.load(f)
    
    for student_dict in data:
        student_obj = Student.from_dict(student_dict)
        students.append(student_obj)

""" Student manger app. It manages the 
adding function, remove function, delete fuction, display fuction. 
or we can say all CRUD operations."""
class StudentManger:
    pass
   
# function for adding students
def add_student(name, age, student_id):
    student = Student(name, age, student_id)
    students.append(student)
    save_student(student)
    return student

# function for removing students
def remove_student(student_id):
    found = False

    for student in students:
        if student.student_id == student_id:
            found = True
            students.remove(student)
            save_student(student)
            print(f"Student {student} removed successfully!")
            return
    
    if not found:
        print("Invalid student_ID or student already removed or student not presnt in this ID")

# function for searching student
def search_student(search_id):
    found = False
    try:
        for student in students:
            if student.student_id == search_id:
                found = True
                print(student)
                return
        if not found:
            print(f"No student is present in this studend ID")

    except NameError:
        print("Some Error occured to featch the details of the student")

# function for update student
def update_student(update_student_id):
    found = False

    for student in students:
        if student.student_id == update_student_id:
            found = True
            val = input("Enter your choice to update(name, age): ")

            # for update the name.
            if val == "name":
                new_name = input("Enter Updated Name: ")
                student.name = new_name
                print("Name updated successfully!")
                break
    
            # for update age.
            elif val == "age":
                try:
                    new_age = int(input("Enter Updated age: "))
                    student.age = new_age
                    print("Age uupdated successfully!")
                    break
                
                except ValueError:
                    print("Enter Only integer.")
            
            else:
                print("Enter valid operation")

    save_student(student)
    
    if not found:
        print("No student found")
    
    return

        
# calling function for load student data in the list
load_students()

# Loop for doing again and again till no input of exit
while True:
    # Entering the methods like add, remove, display and exit
    methods = input("Enter a method (add, remove, display, search, update, exit): ")

    # it is for adding the student into database   
    if methods == "add":
        # adding credential
        name = input("Enter Student Name: ")
        try:
            age = int(input("Enter Student Age: "))
            student_id = int(input("Enter Student ID: "))
            
            #calling function for adding student
            student = add_student(name, age, student_id)
            print(f"Student {student.name} added successfully!")
        
        except ValueError:
            print("Only Interger value are allowed")
    
    # it is for deleating the student into database
    elif methods == "remove":
        student_id = int(input("Enter Student ID to remove: "))

        #calling removing function
        remove_student(student_id)
        
    # it is for display the student data
    elif methods == "display":
        if not students:
            print("No student present in the list`")
        
        else:
            for student in students:
            #calling display function
                student.display()
                print("---------------------")

    # searching by id
    elif methods == "search":
        try:
            search_id = int(input("Enter student ID: "))
    
            #calling the searching function
            search_student(search_id)

        except ValueError:
            print("Only interger values are allowed")
        
    # update student
    elif methods == "update":
        try:
            update_student_id = int(input("Enter student ID for you want to update: "))

            update_student(update_student_id)

        except ValueError:
            print("Enter only intger value.")

    # it is for exiting form the program
    elif methods == "exit":
        print("Exiting the program.")
        break
    else:
        print("Invalid method. Please try again.")