'''
Created on 2013-10-3

@author: casa
'''
import socket

if  __name__=="__main__":
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    print("create socket success");
    
    sock.bind(("localhost",4242));
    print("bind socket success");
    
    sock.listen(5);
    print("listen socket success");
    
    print("listen to client...");
    conn, address=sock.accept();
    print("get client: ");
    print(address);
        
    print("\n\n\nstart chatting:\n");
    while True:
        szbuf=conn.recv(1024)
        print("you: \n"+szbuf);
        
        if  szbuf=="0":
            conn.send("exit");
        else:
            input_s=raw_input("me: \n");
            print("wait for others enter...");
            conn.send(input_s);
            
    conn.close();
    print("end of service");
        