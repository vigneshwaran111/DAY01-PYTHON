

########## Class declaration and Creating object  ######################3
class A():
    def __init__(self):
        print "Class A"
    def sample(self):
        print "Sample in Class A"

class B(object):
    def __init__(self):
        print "Class B"
    def sample(self):
        print "Sample in Class B"

class C:
    def __init__(self):
        print "Class C"

    def sample(self):
        print "Sample in Class C"

obj1 = B
print obj1 # <class '__main__.B'>
obj2 = B() # Class B
print obj2 # <__main__.B object at 0x038B1B10>
obj3 = C() # Class C


######### variables scope #######################

class school(object):
    total_student = 0
    def __init__(self,name, mark1,mark2):
        school.total_student = school.total_student + 1
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        
    def average(self):
        avg = (self.mark1 + self.mark2) / float(2)
        return avg

    def details(self):
        print "Name :", self.name, "avg is ", self.average()

print "total student", school.total_student
student1 = school('Raj',88,45)
student1.details()
print "total student", school.total_student
student2 = school('Kumar',55,56)
student2.details()
print "total student",school.total_student
print "student 1", student1.average()
print "student 2", student2.average()




print school.total_student
student1 = school('Raj',88,45)
print student1.average()
print school.total_student
student1 = school('Raj',88,45)
print student1.average()
print school.total_student


######### Public, protected and private member variables #######################

class sample(object):
    def __init__(self):
        self.public = 5
        self._protected = 10
        self.__private = 15

    def test(self):
        print self.public
        print self._protected
        print self.__private
        
    def mod(self):
        self.public = self.public + 100
        self._protected = self._protected  +100
        self.__private = self.__private  +100

obj= sample()

print obj.public
print obj._protected
# print obj.__private  # Error
obj.test()
obj.mod()
obj.test()


######### Public, protected and private methods #######################

class Parent(object):
    def _protected(self):
        print "protected"

    def __private(self):
        print "private"

    def sample(self):
        self.__private()

class Child(Parent):
    def sample1(self):
        self._protected()   

    def sample2(self):
        self.__private()    
        
#obj = Child()
obj2 = Parent()
#obj.sample1()
#obj.sample2()  # Error
#obj.sample()
obj2._protected()
#obj2.__private() # Error

##################Class Type of methods ############################

class A(object):
    var1 = 5
    def __init__(self):
        self.var2 = 10

    def sample(self,x):
        print "executing sample(%s,%s)"%(self,x)
        print  self.var2     

    @classmethod
    def class_sample(cls,x):
        print "executing class_sample(%s,%s)"%(cls,x)
        print  cls.var1     

    @staticmethod
    def static_sample(x):
        print "executing static_sample(%s)"%x
        # print  cls.var1  # Error
        # print  self.var2  # Error   

a=A()

a.sample(1)
a.class_sample(1)
A.class_sample(1)
a.static_sample(1)
A.static_sample(1)

##################Class Varibales ############################

class A():
    var1 = 5
    def __init__(self):
        self.var2 = 10
        var3 = 15

print A.var1 # Class variable
#print A.var2
obj = A()
print obj.var2 # Instance variable , object variable 
print obj.var3  # AttributeError: A instance has no attribute 'var3'
"""
