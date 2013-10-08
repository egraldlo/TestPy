'''
Created on 2013-10-3

@author: casa
'''
import socket
import sys

if len(sys.argv)<3:
    sys.exit(1)
hostname=sys.argv[1]
port=int(sys.argv[2])

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((hostname,port))
sock.listen(1)
print("i am waiting")

# accpet will return two results, a address and socket object
request, clientaddress=sock.accept()
print("receive a request from",clientaddress)

request.send("socket receiver\n")
request.send("go away\n")
request.shutdown(2)
print("stop server")

sock.close()