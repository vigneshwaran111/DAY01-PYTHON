########################  memory management ############################
# is operator

#run time stack and heep mem

a = [1,2,3,4,5]

b = a

print a
print b

a.append(8)

print a
print b


from sys import getsizeof
var1 = 'a'
var2 = 5
print getsizeof(var1) # 22
print getsizeof(var2) # 12


x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

a = 1

print x1 is y1 


print x2 is y2 


print id(x3[0]), id(y3[0]), id(a)
