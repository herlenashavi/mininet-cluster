#!/usr/bin/env python

import socket
import sys
 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = '10.0.0.2';
port = 8888;
 
while(1) :
    msg = raw_input('Enter message to send : ')
     
    try :
        s.sendto(msg, (host, port))
        d = s.recvfrom(8192)
        reply = d[0]
        addr = d[1]
         
        print 'Server reply : ' + reply
     
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
