

# super is a shortcut to access a base class without having to
know its type or name.

# In Python 3 and above, the syntax for super is:
super().methoName(args)

# normal way to call super (in older builds of Python) is:  super(subClass, instance).method(args)


super(subClass, instance).method(args)

# With super last in each method
class Parent(object):
    def __init__(self):
        print "parent"
        super(Parent, self).__init__()

class Left(Parent):
    def __init__(self):
        print "left"
        super(Left, self).__init__()

class Right(Parent):
    def __init__(self):
        print "right"
        super(Right, self).__init__()

class Child(Left, Right):
    def __init__(self):
        print "child"
        super(Child, self).__init__()

print Child.__mro__  # Method Resolution Order
Child()
# output 
    # child
    # left
    # right
    # parent

# With super first in each method

class Parent(object):
    def __init__(self):
        super(Parent, self).__init__()
        print "parent"

class Left(Parent):
    def __init__(self):
        super(Left, self).__init__()
        print "left"

class Right(Parent):
    def __init__(self):
        super(Right, self).__init__()
        print "right"

class Child(Left, Right):
    def __init__(self):
        super(Child, self).__init__()
        print "child"


# Child()
# output 
    # parent
    # right
    # left
    # child

"""

####### super class ###############

class First(object):
  def __init__(self):
    super(First, self).__init__()
    print "first"

class Second(object):
  def __init__(self):
    super(Second, self).__init__()
    print "second"

class Third(First, Second):
  def __init__(self):
    super(Third, self).__init__()
    print "that's it"

# __mro__  Method Resolution Order
print Third.__mro__
obj = Third()


######## mutiple inheritance ################

class A(object):
    def f(self):
        print "from A"
        return self.g()

    def g(self):
        print 'A'

class C(object):
    def f(self):
        print "from C"
        return self.g()

    def g(self):
        print 'C'

class B(A,C):

    def g(self):
        print "B"

obj = B()
obj.f()
