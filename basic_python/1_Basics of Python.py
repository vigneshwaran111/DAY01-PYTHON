# comment

############################ data types ####################################

# int
## int  ## float

# str


roll_no = 100114590
name = "sithiqu"
percentage = 78.5

print roll_no
print name
print percentage

print type(roll_no)

print type(name)

print type(percentage)


###################  data   structure  #################

tuple =(3,2,34.5,'a',66, "python",78,"how are you")

list = [3,2,34.5,'a',66, "python",78,"how are you"]

set = {3,2,34.5,'a',66, "python",78,"how are you"}

dict = {33:2000,'a':"orange",42:"python",'b':20,"good morning":"bye"}

print tuple
print list
print set
print dict

print type(tuple)

print type(list)

print type(set)
print type(dict)


########################### print ##########################################

print "python" # python
print "python" , "training" # python training

print "python" , 
print "training" # python training

print "python" + "python" # pythonpython

#print "python" + 3 # TypeError: cannot concatenate 'str' and 'int' objects

print # print empty

print ("python")  # python

print 54 # 54

print 54 + 6 # 60

print (56) # 56

a = "abc"
b = "xyz"

print a

print b

print a + b

print a,b

# format

print 'my name is {0} and my age is {2}'.format(name,age)

# Print name, age, location, percentage of mark 
# Print employee name, id, rating 
# Print in 2017 year temperature  of Mumbai  is 22.5 degree
# Train number, train name , platform 
# Month , year , dollar rate

################  arithemetic operation  ###########################

a = 10
b = 3

c = 2

print a + b # 13

print a / b # 3

print a // b # 3

print a / 3.0 # 3.33333333333
print a // 3.0 # 3.0


print a - b # 7
print b - a # -7
print type(b - a) # <type 'int'>

print a * c # 20

print a*'s' # ssssssssss


print a % b # 1

print a % c # 0

print 4 ** 2 # 16

# add, mul , divide
# given number odd or even ?

###### Comparison (Relational) Operator ##############
#Less than(<)
#Greater than(>)
#Less than or equal to(<=)
#Greater than or equal to(>=)
#Equal to(= =)
#Not equal to(!=)

## Logical Operators ########

# and or not in

######################### input_output #####################################


str1 = input("enter \n")
print type(str1)

try int
try str


str1 = raw_input("enter \n")
print type(str1)

# your name is ---
# print sqr

#################### Type Conversion ##############################

value = "5"

var = int(value)

print type(var) , var

value = 5

var = str(value)

print type(var) , var



tup = (1,2,3,4)

var =  list(tup)
print type(var) , var

list1 = [1,2,3,4]

var =  tuple(list1)
print type(var) , var

list2 = [(1,2),(3,4),(5,6)]

var =  dict(list2)
print type(var) , var


list2 = ((1,2),(3,4),(5,6))

var =  dict(list2)
print type(var) , var


list1 = [1,2,3,4]
list2 = [5,6,7,8]
var = enumerate(list1)
print dict(var) # dict from single list

print zip(list1,list2)


list2 = ((1,2),(3,4),(5,6))

var =  dict(list2)
print type(var) , var

# Find average for given mark 
# User input, price of fruit ? , number of  fruits ? , print total price
# User input : add , divide , multiply given numbers







