######## Type conversion ################3

a = 'a'
print type(a)
print isinstance(a, str)


li = [1,2,3,4]
dic = {1:2,4:7}
tu = (1,2,3,4)
se = {1,2,3,4}


"""
print int('4') # 4
print int(4.5) # 4
#print int('4.5') # ValueError
#print int('a') # ValueError
print type(int(10000000000000000000000000000000000)) # long
#print int(li) # TypeError: int() argument must be a string or a number,


print str(3)
print str(3.5)
print str(1000000000000000000000000000000000)
print str('ab')
print str(li) # string as "[1,2,3,4]"
print str(dic) # string as "{1:2,4:7}"
print str(tu) # string as "(1,2,3,4)"
print str(se) # string as "{1,2,3,4}"

print float(6)
print float("4.5") # 4.5
print float(4.5) # 4.5
print float(10000000000) # 10000000000.0 type float
#print float('a') # ValueError
#print float(li) # TypeError: float() argument must be a string or a number


print long(3) # 3 type as long
print long('6') # 6 type as long
#print long('5.6') # ValueError
print long(5.6) # 5 type as long
#print long('a') # ValueError
#print long(li) # TypeError: long() argument must be a string or a number

#print list(tu) # [1,2,3,4]
#print list(dic) # [1, 4] list of keys
#print list(se) # [1, 2, 3, 4]
#print list('a') # ['a']
#print list(5) # TypeError: 'int' object is not iterable
#print list(5.8) # TypeError

print tuple(li) # (1, 2, 3, 4)
print tuple(dic) # (1, 4) tuple od keys
print tuple(se) # (1, 2, 3, 4)
print tuple('a') # ('a',)
#print tuple(5) # TypeError
#print tuple(5.6) # TypeError


seq = [(1,2),(3,4),(4,5)]
print dict(seq) # {1: 2, 3: 4, 4: 5}

#print dict(li) # TypeError: cannot convert dictionary update sequence element #0 to a sequence
#print dict(tu) # TypeError
#print dict(se) # TypeError
#print dict(5) # TypeError: 'int' object is not iterable
# print dict(5.5) # TypeError
#print dict('ab') # ValueError:

print set(li) # set([1, 2, 3, 4])   <type 'set'> will remove the dublicates
print set(dic) # set([1, 4])
print set(se) # set([1, 2, 3, 4])
print set('a') # set(['a'])
#print set(3) # TypeError
#print set(3.6) # TypeError

"""
