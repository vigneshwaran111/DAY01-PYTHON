########################## Dict ########################################

dict1 = {'a':20,'b':23,'c':56,'d':78}


dict1['e'] = 90

print dict1

dict1['b'] = 111

print dict1

del dict1['e']

print dict1

for key in dict:
    print "key is", key
    print "value is ", dict[key]

a = dict(one=1, two=2, three=3)

print a

dict1 = {1: 2, 3: 4, 5: 6}

print dict1.items() # [(1, 2), (3, 4), (5, 6)]
print dict1.keys() # [1, 3, 5]
print dict1.values() # [2, 4, 6]

for key, value in dict1.items():
    print "key : ", key
    print "value : ", value

print "--------------"

dict1 = {1:2, 3: 4, 5: 6,7:8}

print dict1.pop(1)

print dict1

print dict1.popitem()
print dict1

dict1.update({9:10,11:12,13:14})
print dict1


print {n: n**2 for n in range(5)}

list1 = ['a','b','c','d']

print enumerate(list1)
print dict(enumerate(list1))

list1 = [1,2,3,4]
list2 = [5,6,7,8]

print zip(list1,list2)

print dict(zip(list1,list2))


########################## set #########################################

dis2 = {'kumar', 'hari', 'raj'}

print dis2

dis2.add('tj')
print dis2

dis2.add('hari')
print dis2

dis2.remove('kumar')
print dis2

dis2.append('hari') # AttributeError: 'set' object has no attribute 'append'

print dis2[0] # TypeError: 'set' object does not support indexing


A = [1,3,2,4]
B = [2,4,7,8]

print set(A) - set(B) # A - set([1, 3])
print set(A) & set(B) # C - set([2, 4])
print set(B) - set(A) # B - set([8, 7])
print set(A) # A + C - set([1, 2, 3, 4])
print set(B) # B + C - set([8, 2, 4, 7])
print set(A) ^ set(B) # A + B - set([1, 3, 7, 8])
print set(A) | set(B) # A + B + C - set([1, 2, 3, 4, 7, 8])
