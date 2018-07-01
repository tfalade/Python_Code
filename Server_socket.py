'''
Created on Apr 9, 2015

@author: tfalade
'''
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host,port))

s.listen(5)
while True:
    c,addr = s.accept()
    print ('Got connection from'), str(addr)
    c.send(str('Thank you for connecting'))
    c.close()