# List Comprehensions ########

list1 = [3,4,2,7,1,9]

# in the list more then print 3 
# print sqr

string = "Hello 12345 World"

# print only numbers

# dict Comprehensions ########

list2 = ['Cisco','Aspire','Dell','Eta','Bits','Google','Hcl','Fedora']

# Dict Comprehensions ########

print {i:len(i) for i in list2}

######### lambda ########

# lambda arguments : expression

add = lambda x, y : x + y

print add(4,5) # 9

lambda x: x **2


#map(aFunction, aSequence)
#filter(aFunction, aSequence)
#reduce(aFunction, aSequence)

# map #####

items = [1, 2, 3, 4, 5]

def sqr(x):
    return x ** 2

print list(map(sqr, items))

print list(map(pow, [2, 3, 4], [10, 11, 12]))

# map will print all , filter prints only true (or val) , wont print None or false
# filter ###

def test(x):
    if x < 0 :
        return x
[-5, -4, -3, -2, -1,0,1,2,3,4,5]   

print list(filter(test, range(-5,5)))  # [-5, -4, -3, -2, -1]
print list(map(test, range(-5,5))) # [-5, -4, -3, -2, -1, None, None, None, None, None]

#  reduce ##

#print reduce(lambda x,y: x+y, [47,11,42,13])  # 113









