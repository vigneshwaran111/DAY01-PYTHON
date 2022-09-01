
try:
    print var
    
except:
    print "except"

else:
    print "else"

finally:
    print "finally"
	

---------------------------------
while True:
    var = raw_input("Enter name:mark : ")
    try:
        var2 = var.split(':')
        print var2
        name = var2[0]
        mark = int(var2[1])
    except:
        continue
    else:
        if mark > 50:
            print "{} is pass".format(name)
        else:
            print "{} is fail".format(name)
        break

		
a = raw_input("enter\n")
try:
    name = a.split(":")[0]
    mark = a.split(":")[1]
    mark = int(mark)
    print name
    print mark/2
    
except IndexError as err:
    print "enter in name:mark format"
except ValueError as err:
    print "pls enter the mark"
except Exception as err:
    print "pls enter the mark"

# IndexError:  for only name
# ValueError: for invalid mark
	
a = raw_input("enter\n")
a = int(a)
print a <= 100
assert a <= 100

a = raw_input("enter password \n")

if len(a) != 6:
    raise Warning("its not 6")
else:
    print "your logged in"
    
a = raw_input("enter\n")
a = int(a)
print a <= 100
assert a <= 100


list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'\
         'q','r','s','t','u','v','w','x','y','z']

a = raw_input("enter number \n")

if a > len(list1):
    raise Exception("give the index between 0 to 4")
else:
    print list1[a]

raise NameError("its my error")

raise Warning("warning")
