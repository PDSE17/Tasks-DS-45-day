# Mini project-1 

# Student Data Manager
# Build a Student Record System Using OOP
# Features: Add, Update, Delete, Search Records

# CLASS STUDENT 
class Student:
    def __init__(self,roll_no,name,age,branch):
     self.roll_no = roll_no
     self.name = name
     self.age = age
     self.branch = branch
    

    def display(self):
        print("Roll No:",self.roll_no)
        print("Name",self.name)
        print("Age",self.age)
        print("Branch:",self.branch)

students = []

# ADD STUDENT
def add_student():
 roll_no = int(input("Enter roll no: "))


# DUPLICATE ROLL NUMBER CHECK
 for student in students:
    if student.roll_no == roll_no:
       print("Roll Number Already Exists!")
       return
    

 name = input("Enter name: ")
 age = int(input("Enter age: "))
 branch = input("Enter branch: ")

 student = Student(roll_no,name,age,branch)
 students.append(student)

 print("Student Added Successfully!")


# SEARCH STUDENT BY ROLL NUMBER:
def search_student():
   roll = int(input("Enter roll number to search: "))

   for student in students:
      if student.roll_no == roll:
         print("Student Found!")
         student.display()
         return

   print("Student Not Found!")  
         

# UPDATE STUDENT 
def update_student():
    roll = int(input("Enter roll number to update: "))

    for student in students:
        if student.roll_no == roll:
            student.name = input("Enter New Name: ")
            student.age = int(input("Enter New Age: "))
            student.branch = input("Enter New Branch: ")
            
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")

# DELETE STUDENT
def delete_student():
   roll = int(input("Enter roll no to delete: "))

   for student in students:
      if student.roll_no == roll:
         students.remove(student)
         print("Student Deleted Successfully!")
         return
      
   print("Student Not Found!")
   

   
def display_students():
   if len(students) ==0:
      print("No Students Found!")
      return

   for student in students:
      student.display()
      print()


# MAKE A CHOICE 
while True:
   print("\n==== STUDENT DATA MANAGER ====")
   print("1.Add Student")
   print("2.Display Students")
   print("3.Search Student")
   print("4.Update Student")
   print("5.Delete Student")
   print("6.Exit")

   choice = int(input("Enter your choice: "))

   if choice == 1:
      num = int(input("How many students do you want to add? "))

      for i in range(num):
         print(f"\nEnter details of student {i+1}")
         add_student()
               
   elif choice == 2:
      display_students()

   elif choice == 3:
      search_student()

   elif choice == 4:
      update_student()
      
   elif choice == 5:
      delete_student()

   elif choice == 6:
      print("Thank You!")
      break

   else:
      print("Invalid Choice!")
        