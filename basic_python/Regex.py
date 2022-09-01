import re
### why Regex ####

##### search ####

# find numbers in the lines


str1 = """
hi how are you
i am fine
how about you
i too fine"""

pattern = ".* how .*"

for line in str1.splitlines():
   out_put = re.search(pattern, line)
   print "out_out", out_put
   if out_put:
      print line

##### match vs search ####

import re

str1 = """
hi how are you
bus is good
its a good bus
i too fine"""

pattern = "bus"

for line in str1.splitlines():
   out_put = re.match(pattern, line)
   if out_put:
      print line


#### raw string #####

str1 = "abded \n abced"
print str1

str1 = r"abded \n abced"
print str1

# line = r"abcd a \n b abced" pattern = r".* a \\n b ."

########## pattern ############

# ^ $ pattern = "^hi .* you$"

# [..] pattern = "^[hH]"

# ? pattern = "sith?ique"
# line = "55" pattern = "[\d]{2}"
# pattern = "[0-3]|[7-9]"

out_put = re.search(pattern, line)
if out_put:
   print line

######## control characters (+ ? . * ^ $ ( ) [ ] { } | \) #########

# line = "abcd a $  b abced" pattern = ".* a \$ b ."
# line = "abcd a \  b abced" pattern = ".* a \\\ b ."

############# examples ##############

pattern1 = re.search(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$', ip)

(       # for 3 times
(       # for "."
\d{1,2} # 0 - 99 
1\d{2}  # 100 - 199
2[0-4]\d # 200 - 249
25[0-5] # 250 - 255
)\. # for "."
){3} # same pattern for 3 times 


pattern1 = re.search(r'^([0-9A-F]{2}-){5}[0-9A-F]{2}$', mac, re.I)


sample_mail = "sithiqu.mtech@gmail.com"

print  re.search(r'^\w+[-\.]?\w+@\w+\.\w+$', sample_mail)


import re
ip = " 172.16.215.255"


ip = "9e-EE-CB-2F-FF-68"

#pattern = re.compile('([0-9A-F][0-9A-F]-){5}[0-9A-F][0-9A-F]')
pattern1 = re.search(r'^([0-9A-F]{2}-){5}[0-9A-F]{2}$', ip, re.I)

print pattern1

"""

if re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$', ip):
    print "Valid IP"
else:
    print "Invalid IP"
"""

