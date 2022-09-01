########################## loops #######################################

list1 = ['a','b','c','d','e','f']

list1 = [1,2,3,4,5,6]

for value in range(6):
    print value

for value in list1:
    print value

# print grater then 
# print odd 
# print even

while True:
  stuff()
  if fail_condition:
    break

x = "bye"
while x != "log_out":
    print "enter loop"
    x =  raw_input("enter str \n")
    print x
	

for i in range(10):
    print i 
    if i > 5:
        break

    
		

for i in range(10):
    
    if i > 5:
        break
    elif i == 4:
        continue

    print i 

for i in range(10):
    if i == 4:
        continue
    print i 
	
# print only the odd number till 12 from 20

for i in range(20):
    if i > 12:
        break
    elif i % 2 != 0:
        continue
    print i 

		

import sys
a = 5
if a == 5:
    for i in range(4):
        print "2nd for"
        if i > 2:
            print i
            sys.exit()
            
    print "for loop done"



	


fruits = ['apple','orange','banana','lemon','mango','papaya']

for fruit in fruits:
    print "checking character 'o' in", fruit
    for char in fruit:
        if char == 'o':
            print "character 'o' present in", fruit
            break
    else:
        print "character 'o' not in", fruit



############### ref ####################################

while list2:
    temp = list2[0]
    for i in list2:
        if temp > i:  # len(temp) > len(i) will sort based on length , temp[1] > i[1] will sort based on second letter 
            temp = i
    list3.append(temp)
    list2.remove(temp)


	
print list3

# sort one list 
list2 = ['Cisco','Aspire','Dell','Eta','Bits','Google','Hcl','Fedora']
j = 0
while list2[j:]:
    temp = list2[j]
    
    for i in list2[j:]:
        if temp > i:    # len(temp) > len(i) will sort based on length , temp[1] > i[1] will sort based on second letter   and so on 
            temp = i

    list2.remove(temp)
    list2.insert(j,temp)
    j = j + 1
    
print list2


list2 = [5,3,1,8,7,2,9,4,6]

for i in list2:
    temp = i
    index = list2.index(i)
    for j in list2[index:]:
        if temp > j:
            temp = j
    list2.remove(temp)
    list2.insert(index,temp)

print list2


# sort two list

list2 = ['Cisco','Aspire','Dell','Eta','Bits','Google','Hcl','Fedora']
list3 = []




list2 = [3,5,2,56,6,8,18, 44,21]
list3 = []
while list2:
    temp = list2[0]
    for i in list2:
        if temp > i:  # len(temp) > len(i) will sort based on length , temp[1] > i[1] will sort based on second letter 
            temp = i
    list3.append(temp)
    list2.remove(temp)
    
print list3