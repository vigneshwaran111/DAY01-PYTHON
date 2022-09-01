########### numpy ###############

import numpy as np 

arr = np.array([["Kumar", "23", "Engg.", "chennai"], 
                ["Ragu", "30", "Sr.Engg.", "Mumbai"], 
                ["Priya", "28", "Manager", "chennai"], 
                ["Varun", "26", "Engg.", "pune"],
                ["Vijay", "40", "Architect", "mumbai"]]) 
  

temp = arr[:3:2,:3]

print temp

#temp = arr[:,3] == "chennai"

#print arr[temp,:][:,:]

########### math ###############

import math

print math.ceil(5.2)
print math.sqrt(25)
print math.pow(2,3)
print math.exp(5)
print math.factorial(4)

print math.copysign(5,-3)

########### date time ###############
import datetime

#print datetime.now().strftime('%m%d%H%M%S')
print datetime.datetime.now()

print datetime.date(2008,5,4)
print datetime.time(5,6,7)

################### pickle ################################

import pprint, pickle

data1 = {'a': [1, 2.0, 3, 'abc'],
         'b': ('string', u'Unicode string'),
         'c': None}

var = "sample"

list1 = [1, 2, 3]

output = open('data.pkl', 'wb')

pickle.dump(var, output)
pickle.dump(data1, output)
pickle.dump(list1, output)
output.close()

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
print type(data1)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
print type(data2)
pprint.pprint(data2)

data3 = pickle.load(pkl_file)
print type(data3)
pprint.pprint(data3)

pkl_file.close()


###################### time #####################################
import time
from  time import strftime, gmtime



#print strftime('%m-%d-%Y  %A %B %I:%M:%S %p')

start = time.time()
print "start time ",  start

b=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start))

print b

time.sleep(3)  

done = time.time()
print "end time ",done

b=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(done))

print b

elapsed = done - start

print elapsed



print strftime("%m-%d-%Y  %A %b %I:%M:%S %p")

start = time.time()
print start
b=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start))

time.sleep(3)  # or do something more productive


done = time.time()
print done
a=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(done))
elapsed = done - start
print elapsed

print time.strftime('%H:%M:%S', time.localtime(elapsed))


################### csv #####################################
import csv
with open('test.csv', 'wb') as csvfile:
    f2 = csv.writer(csvfile, delimiter=',')
    f2.writerow(['python'] *5 + ['Baked Beans'])
    f2.writerow(['python', 'Lovely python', 'Wonderful python'])


with open('test.csv', 'rb') as f:
    reader2 = csv.reader(f)
 
    # read file row by row
    for row in reader2:
        print row

####################### math ######################
import math

print math.exp(5)

print math.log(5, 10)

print math.pow(3, 3)

       
################### html #####################################
from html import HTML
h = HTML()
h.p('Hello, world!')
print h   #  <p>Hello, world!</p>                     

h = HTML('html', 'text')
print h # <html>text</html>

from html import XML
h = XML('xml')
h.p
h.br('hi there')
print h

<xml>
<p />
<br>hi there</br>
</xml>

# https://pypi.python.org/pypi/html



