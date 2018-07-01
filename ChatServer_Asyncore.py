'''
Created on May 12, 2015

@author: tfalade
'''
from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

#class ChatServer(dispatcher):
#    
#    def handle_accept(self):
#        conn, addr = self.accept()
#        print('Connection attempt from', addr[0])
#        
#s = ChatServer()
#s.create_socket(socket.AF_INET, socket.SOCK_STREAM)
#s.socket.bind(('', 5006)) 
#s.listen(5)
#asyncore.loop()      


#----------------------------------------------------------
PORT = 5008
NAME = 'TestChat'

class ChatSession(async_chat):
    
    def __init__(self,server,sock):
        # Standard setup tasks:
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator("\r\n")
        self.data = []
        # Greet the user:
        self.push('Welcome to %s\r\n' % self.server.name)
        
        
    def collect_incoming_data(self, data):
        self.data.append(data)
        
    def found_terminator(self):
        line =''.join(self.data)
        self.data = []
        # Do something with the line.....
        self.server.broadcast(line)
        print(line)
        
    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)           
    

class ChatServer(dispatcher):
    
    def __init__(self, port, name):
        # Standard setup tasks
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.name = name
        self.sessions =[]
        
        
    def disconnect(self, session):
        self.sessions.remove(session)
        
    def broadcast(self, line):
        for session in self.sessions:
            session.push(line + '\r\n')        
        
    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(self, conn))
        print('Connection attempt from', addr[0])
        
if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try: asyncore.loop()
    except KeyboardInterrupt: print()            