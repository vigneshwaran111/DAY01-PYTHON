f = open('sithiqu1.txt','a+')
print f.readline()
print f.tell()
print "print over"
f.write("sithiqu8")
print f.tell()
print "write over  "
print f.seek(0)
print f.readline()
print "flie over"
f.close()

f = open('sithiqu.txt','r')
print f.read()
f.close()
f = open('sithiqu.txt','w')
f.write("hi1\n")
f.write("hi2\n")
f.write("hi3\n")
f.write("hi4\n")

f.close()

with open('sithiqu1.txt') as f:
    for i in reversed(f.readlines()):
        print i


with open('sithiqu1.txt') as f:
    newText=f.read().replace('sithiqu', 'yahya')

with open('sithiqu1.txt', "w") as f:
    f.write(newText)

with open('sithiqu1.txt','w+') as f, open('var.txt','w+') as f2:
    print f
    print f2

