'''
Created on 2013-10-3

@author: casa
'''
import socket

if  __name__=="__main__":
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(("localhost",4242));
    
    print("\n\n\nstart chatting:\n");
    while True:
        print("me: ");
        guess=raw_input('');
        print("wait for others enter...");
        
        sock.send(guess);
    
        szbuf=sock.recv(1024);
        print("you: \n"+szbuf);
        
    sock.close();
    print("end of connect");