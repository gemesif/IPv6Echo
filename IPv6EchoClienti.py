#!/usr/bin/python3
#!/usr/bin/env python3

import sys
import os
import getopt
from datetime import datetime
import socket

#*********************************************************************************

#
# IPv6EchoClienti.py 
# @gemesif
# date 2020 07 16
#

#*********************************************************************************

version = '1.1'

IP = "::1"
# IP = "2a00:1450:400d:805::200e" # google.com
# PORT = 5001
PORT = 5000
TIMEOUT = 1
MESSAGE = "Hello World!"
# MESSAGE = ""
LOOP = False
varTrue = True

#*********************************************************************************

def myDate():
    pass
    now = datetime.now()
    s1 = now.strftime("%Y%m%d %H%M%S")
    return(s1)

#*********************************************************************************

print("UDP target IP:", IP)
print("UDP target port:", PORT)
print("message:", MESSAGE)

print('ARGV      :', sys.argv[1:])

try:
    options, remainder = getopt.getopt(
        sys.argv[1:],
        'hvli:p:t:',
        ['help',
         'version',
         'loop',         
         'ipaddr',
         'portnumber',
         'timeout',
         ])
except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)

print('OPTIONS   :', options)
print('REMAINING :', remainder)

msg_indent = (" ".rjust(len(os.path.split(sys.argv[0])[1]) + 1))

usagestring = '''\
Usage:
{progname} [-h | --help] | [-v | --version] | [-l | --loop]
{indent}[-i ipv6_address | --ipaddr ipv6_address] | [-p port_number | --portnumber port_number]
{indent}[-t timeout | --timeout timeout]
{indent}defaults: ipv6_address "::1" port_number 5000 timeout 1sec
              '''.format(progname=os.path.split(sys.argv[0])[1], indent=msg_indent)

versionstring = '''\
Version: {ver}
                '''.format(ver=version)

loopstring = '''\
Running in infinite loop
             '''

for opt, arg in options:
    if opt in ('-h', '--help'):
        print(usagestring)
        sys.exit(0)
        pass
    elif opt in ('-v', '--version'):
        print(versionstring) 
        sys.exit(0)
        pass
    elif opt in ('-l', '--loop'):
        print(loopstring)
        LOOP = True
        pass
    elif opt in ('-i', '--ipaddr'):
        IP = arg
        pass
    elif opt in ('-p', '--portnumber'):
        PORT = int(arg)
        pass
    elif opt in ('-t', '--timeout'):
        TIMEOUT = int(arg)
        pass

#*********************************************************************************

try:
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.settimeout(TIMEOUT)
except socket.error as msg:
    print("socket creation error:", msg)
    sys.exit(1)

count = 1
# while LOOP:    # infinite loop fot test
while varTrue:    # infinite loop fot test

    try:
        sock.sendto(MESSAGE.encode(), (IP, PORT))
    except socket.error as msg:
        print("socket sendto error:", msg)
        sys.exit(1)

    try:
        data, ip = sock.recvfrom(1024)
    except socket.error as msg:
        print("socket recvfrom error:", msg)
        sys.exit(1)

    if LOOP == False:
        pass
        print("{}".format(data.decode()))
        varTrue = False
        break
    else:
        pass
        print("{} {}".format(count, data.decode()))
        varTrue = True

    count += 1
