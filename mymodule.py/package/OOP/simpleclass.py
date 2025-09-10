# Simple class program 
class Person:
    def __init__(self, name, age):   
        self.name = name
        self.age = age

    def myfunc(self):              
        print("Hello this is " + self.name)

p1 = Person("Riya", 21)

print(p1.name)  
print(p1.age)   
p1.myfunc()     

    


    
  