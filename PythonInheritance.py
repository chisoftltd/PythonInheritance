# Python Inheritance
# Create a Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firtsname = fname
        self.lastname = lname

    def printname(self):
        print(self.firtsname, self.lastname)

x = Person("Joy", "Chinwe")
x.printname()

# Create a Child Class
class Student(Person):
  pass

y = Student("Benjamin", "Uchenna")
y.printname()

# Add the __init__() Function
class Person1:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname1(self):
    print(self.firstname, self.lastname)

class Student1(Person1):
  def __init__(self, fname, lname):
    Person1.__init__(self, fname, lname)

x = Student1("Mike", "Olsen")
x.printname1()

# Use the super() Function
class Person2:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname2(self):
    print(self.firstname, self.lastname)

class Student2(Person2):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

xy = Student2("Shepherd", "Chinwe")
xy.printname2()

# Add Properties
class Person3:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname3(self):
    print(self.firstname, self.lastname)

class Student3(Person3):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduateionyear = 2017

xy = Student3("Uchenna", "Chinwe")
xy.printname3()
print(xy.graduateionyear)


class Person4:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname4(self):
    print(self.firstname, self.lastname)

class Student4(Person4):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduateionyear = year

xy = Student4("Uchenna", "Chinwe-Ben", 2018)
xy.printname4()
print(xy.graduateionyear)

# Add Methods
class Person5:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname5(self):
    print(self.firstname, self.lastname)

class Student5(Person5):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

xy = Student5("Uchenna", "Chi-Ben", 2018)
xy.printname5()
print(xy.graduationyear)
xy.welcome()