
class Person(object):

   
  def __init__(self, name, id):
    self.name = name
    self.id = id
 
  
  def Display(self):
    print(self.name, self.id)
 
 

emp = Person("vanakam", 102)
emp.Display()


class Emp(Person):
   
  def Print(self):
    print("Emp class called")
     
Emp_details = Emp("good", 103)
 

Emp_details.Display()



Emp_details.Print()


 
class Person(object):
 
    
    def __init__(self, name):
        self.name = name
 
    
    def getName(self):
        return self.name
 
    
    def isEmployee(self):
        return False
 
 

class Employee(Person):
 

    def isEmployee(self):
        return True
 
 

emp = Person("hello")
print(emp.getName(), emp.isEmployee())
 
emp = Employee("world")
print(emp.getName(), emp.isEmployee())




class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def display(self):
    print(self.name, self.age)
 

class Student(Person):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age

    super().__init__("Rahul", age)
 
  def displayInfo(self):
    print(self.sName, self.sAge)
 
obj = Student("vijay", 23)
obj.display()
obj.displayInfo()
