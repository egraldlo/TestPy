'''
Created on 2013-10-6

@author: casa
'''
import sys
import time
import poplib
import smtplib

def sendemail():
    try: 
        handle = smtplib.SMTP('smtp.126.com',25) 
        handle.login('*******@126.com','*******') 
        msg = 'To: ********@gmail.com\r\nFrom:*********@126.com\r\nSubject:hello\r\n'
        handle.sendmail('**********@126.com','********@gmail.com',msg) 
        handle.close() 
        return 1
    except: 
        return 0
    
if  __name__=="__main__":
    sendemail()