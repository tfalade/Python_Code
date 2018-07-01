'''
Created on Apr 9, 2015

@author: tfalade
'''
import socket

s = socket.socket()

host = socket.gethostname()
port = 5008

s.connect((host,port))
print (s.recv(1024))
