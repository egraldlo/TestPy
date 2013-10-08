'''
Created on 2013-10-3

@author: casa
'''
import threading
import Queue
import time

# q=Queue.Queue(0);
# q=Queue.LifoQueue(0);
q=Queue.PriorityQueue(0);
NUM=3;

def dojob(job):
    time.sleep(1);
    print("doing",job);
    
class mythread(threading.Thread):
    def __init__(self,input_,work):
        self.input_=input_;
        self.work=work;
        threading.Thread.__init__(self);
            
    def _process_job(self,job,work):
        dojob(job);
            
    def run(self):
        '''
        i am in the thread function
        '''
        while True:
            if self.input_.qsize()>0:
                job=self.input_.get();
                work=self.work;
                self._process_job(job,work);
            else:
                break;

if  __name__=="__main__":
    print("begining...");
    for i in range(NUM):
        q.put(i);
      
    print("q size: %d" % q.qsize());
    
    for x in range(NUM):
        time.sleep(1);
        mythread(q,x).start();
        print("hello");
        