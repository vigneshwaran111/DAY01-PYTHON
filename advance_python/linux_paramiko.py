

import sys

var = sys.argv
var1 = sys.argv[0]
var2 = sys.argv[1]
var3 = sys.argv[2]

print "var 1 is ", var1
print "var 2 is ", var2
print "var 3 is ", var3
print "sys.argv is ", sys.argv

sys.path
sys.exit()



#################### os #######################
os.rename(current_file_name, new_file_name)

os.remove(file_name)

os.mkdir("newdir")

print os.getcwd() # pwd

os.rmdir('/home/sithiqu/pytr/hi/') # remove folder

print os.listdir('/home/sithiqu/' ) # list files and folder

print os.path.isfile('sample.py') # True if file is present

#############     subprocess ######################



import subprocess
output = subprocess.check_output('lscpu', shell=True)
print output


os.popen('mkdir my_folder') # create directory 

########   Paramiko ############################


https://bootstrap.pypa.io/get-pip.py  C:\Python27
cd ../..  cd Python27
python get-pip.py

apt-get install python-pip
pip freeze
pip install paramiko

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect( hostname = '10.156.90.1' , port = 22 , username = 'root', password = 'password' )

stdin, stdout, stderr =ssh.exec_command('ls /home/')
stdin, stdout, stderr =ssh.exec_command("cd /home/devops/;python -c '\
from sample import *;mysqr(6)'")
out_put=stdout.read()

print out_put

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect( hostname = '151.19.134.2' , port = 2022 , username = 'root', password = 'g0g04ABS' )
#stdin, stdout, stderr =ssh.exec_command('uptime')
#abcd=stdout.read()
#print abcd
#ftp = ssh.open_sftp()
#ftp.get('/var/config/default/acpu.ini.common', 'acpu.ini.common')
#ftp.put('sap.py', '/var/log/sap.py')
#ftp.close()
#stdin, stdout, stderr =ssh.exec_command('python /var/log/sap.py')
stdin, stdout, stderr =ssh.exec_command('acpulegprov')
stdin.write('1\n')
stdin.write('2\n')
stdin.write('11\n')
stdin.write('1\n')
stdin.write('7\n')
abcd=stdout.read()
print abcd



############  ref ########################33333


file present or not  create the file 


# file permision chnage 


# find up time 
cat /proc/cpuinfo
lscpu

IP from ifocnfig
defualt route from route -n
# route -n check for its added or not 

find md5sum of the file 

md5sum teamviewer_linux.deb

uname -a # debian or ubuntu 

change file permision chmod 711 abc.sh

cal print the calender 

date # get date and time 

change the date # date +%Y%m%d -s "20120418"



