

################ scope of variables #####################33

def total(a,b,c,d,e):
    global sum1
    sum1 = a + b + c + d + e

def average(name):
    avg = sum1 / 5
    print "average mark of {} is {}".format(name,avg)

total(20,70,40,60,80)
average('sithiqu')


#### argv and kwargs  #####


def sample3(*argv,**kwargs):
    print argv
    print kwargs

sample3()
sample3(1)
sample3(x=90)
sample3(31,2,3,4,a=56,b='abc',c=87.7,d=[1,2,3,4])

def sample1(**kwargs):
    print kwargs

sample1(a=56,b='abc',c=87.7,d=[1,2,3,4])

def sample(*argv):
    print argv

sample(1,2,3,4)

list1 = [3,5,1,7,3,90,34,56]
def sample1(var,**var2):
    if 'sort' in var2:
        if var2['sort']:
            var.sort()
    if 'reverse' in var2:
        if var2['reverse']:
            var.reverse()
    return var

print sample1(list1,sort=True)
print sample1(list1,sort=True,reverse=True)
print sample1(list1,reverse=True)

# https://docs.python.org/2/library/functions.html


# import , from import , PYTHON PATH


