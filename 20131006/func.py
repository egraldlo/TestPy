'''
Created on 2013-10-6

@author: casa
'''
def func():
    print("hello")
    
def repeat(fun,times):
    for i in range(times):
        fun()
        
repeat(func,4)

import time  
   
def timeit(func):  
    def wrapper():  
        start = time.clock()  
        func()  
        end =time.clock()  
        print 'used:', end - start  
    return wrapper  
   
@timeit  
def foo():  
    print 'in foo()'  
   
foo()  