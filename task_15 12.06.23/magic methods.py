#Class and objects

#Example code:

class boys:
    def __init__(self):
        print("hello")
x=boys()


#Example code:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#Example code:

class GFG:
    def __init__(somename, name, company):
        somename.name = name
        somename.company = company
 
    def show(somename):
        print("Hello my name is " + somename.name +
              " and I work in "+somename.company+".")
 
 
obj = GFG("John", "GeeksForGeeks")
obj.show()



#Example code:
class Dog:
 
    animal = 'dog'
 
    
    def __init__(self, breed):
 
        
        self.breed = breed
 
    
    def setColor(self, color):
        self.color = color
 
    
    def getColor(self):
        return self.color
 
 

Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())
        
        
