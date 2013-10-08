'''
Created on 2013-10-3

@author: casa
'''
import time

if  __name__=="__main__":
    time.sleep(2);
    print("clock1:%s" % time.clock());
    time.sleep(2);
    print("clock2:%s" % time.clock());
    time.sleep(2);
    print("clock3:%s" % time.clock());
    
    now=time.localtime();
    print(now);
    now_=time.mktime(now);
    print(now_);
    ok=time.ctime(now_);
    print(ok);
