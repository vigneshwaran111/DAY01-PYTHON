########################## List ########################################

#CRUD

list1 = []

e = 5
i = 3       

list = [1,3,11,9,0,78,5,6]

list.insert(i,e) # [1, 3, 11, 5, 9, 0, 78, 5, 6]
list.append(e) # [1, 3, 11, 5, 9, 0, 78, 5, 6, 5]

list1 = [1,2,3,4,5,6,7,8]

print list1[1::2] 

#del

del list[2:4] # [1, 3, 0, 78, 5, 6] - modifed same list
list.pop(1) # [1, 11, 9, 0, 78, 5, 6] - index based modifed same list
list.remove(1) # [3, 11, 9, 0, 78, 5, 6] -  value based modifed same list

print list(filter(lambda a: a != 2, list1)) # will remove all 2 from list

list.sort()

list.reverse()

list = [1,2,3,4]
print list.index(4) # 3
print list.count(4) # 1

list2 = [2,7]
list.extend(list2) # [1, 2, 3, 4, 2, 7]

min()
max()

#max 

list2 = [3,5,2,56,6,8,18,44,21]

temp = list2[0]
for i in list2:
    if temp < i:
        temp = i
print "max is ", temp


######## sorting

list1 = [1,3,2,11,9,0,2,78,5,6,2,2]

list1.sort() # [0, 1, 2, 2, 2, 2, 3, 5, 6, 9, 11, 78]
list1.sort(reverse=True) # [78, 11, 9, 6, 5, 3, 2, 2, 2, 2, 1, 0]


# sorting

li = [5, 2, 3, 1, 4]

print li.sort() # output is "None" original list modified

print li # output is [1, 2, 3, 4, 5]

li = [5, 2, 3, 1, 4]
print li.sort(reverse = True) # this will reverse the output
print li

li = [5, 2, 3, 1, 4]

list.reverse()

print sorted(li) # output is [1, 2, 3, 4, 5] , original list wont changed 

print li # output is [5, 2, 3, 1, 4]



list2 = ['Cisco','Aspire','aspire','dell','Eta','Bits','Google','Hcl','Falcon','fedora']

list3 = [3,5,1,8,10,4,13]

print sorted(list2, key=len)  # sort based len of the string 

# key=str.lower  , key=str.upper

print sorted(list3, reverse = True )  # to reverse the order 

def chk(x):
    return len(x)
    
#print sorted(list2, key=chk)  # user define keys

########################## string ######################################
# .split()

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( )  # ['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
print str.split(' ', 1 ) # ['Line1-abcdef', '\nLine2-abc \nLine4-abcd']



# .strip()

str = "0000000this is string example.00...wow!!!0000000";
print str.strip('0')  # this is string example.00...wow!!!

# remove space in string

# str.join(sequence)

s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print s.join( seq )

list1 = ['a','b']
print '-'.join(list1)



str = "this is string example....wow!!! this is really string"
print str.replace("is", "was") # this is string example....wow!!! this is really string

print str.replace("is", "was", 2) # thwas was string example....wow!!! this is really string

Q# replace java with python

# len( str )
# str.lower()
# str.upper()

str.isdigit()

str = "123456";  # Only digit in this string
print str.isdigit()


# str.count

str = "this is string example....wow!!!";

sub = "i";
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow";
print "str.count(sub) : ", str.count(sub)

# str.count(sub, 4, 40) :  2
# str.count(sub) :  1


# str.find(str, beg=0, end=len(string))

str1 = "this is string example....wow!!!";
str2 = "exam";

print str1.find(str2)  # 15
print str1.find(str2, 10) # 15
print str1.find(str2, 10,13) # -1
print str1.find(str2, 40) # -1


# str.index(str, beg=0 end=len(string))

str1 = "this is string example....wow!!!";
str2 = "exam";

print str1.index(str2) # 15
print str1.index(str2, 10) # 15
print str1.index(str2, 40)
Traceback (most recent call last):
  File "C:/Users/che19744/Desktop/sa3.py", line 6, in <module>
    print str1.index(str2, 40)
ValueError: substring not found






