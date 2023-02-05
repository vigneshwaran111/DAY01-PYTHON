
## Bitwise operators  ###########

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print "Line 1 - Value of c is ", c

c = a | b;        # 61 = 0011 1101 
print "Line 2 - Value of c is ", c

c = a ^ b;        # 49 = 0011 0001  # Bitwise XOR

print "Line 3 - Value of c is ", c

c = ~a;           # -61 = 1100 0011  # Bitwise NOT

# -61 = 1100 0011
# 1100 - first 1 is for "-ve", next 1 (2pow6) equal to 64, so -64
# 0011 - is 3
# -64 + 3 = -61
print "Line 4 - Value of c is ", c

c = a << 2;       # 240 = 1111 0000
print "Line 5 - Value of c is ", c

c = a >> 2;       # 15 = 0000 1111
print "Line 6 - Value of c is ", c

###### Relational Operator ##############
#Less than(<)
#Greater than(>)
#Less than or equal to(<=)
#Greater than or equal to(>=)
#Equal to(= =)
#Not equal to(!=)

## Logical Operators ########

# and or not 

# arithemetic operation ###########

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

# Assignment operators #########

a = 21
b = 10
c = 0

c = a + b
print "Line 1 - Value of c is ", c

c += a
print "Line 2 - Value of c is ", c 

c *= a
print "Line 3 - Value of c is ", c 

c /= a 
print "Line 4 - Value of c is ", c 

c  = 2
c %= a
print "Line 5 - Value of c is ", c

c **= a
print "Line 6 - Value of c is ", c

c //= a
print "Line 7 - Value of c is ", c
