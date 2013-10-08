'''
Created on 2013-10-3

@author: casa
'''
import random;

data = [random.randint(1,10) for i in range(20)]
print(data);
data1 = [((random.randint(1,10),), {}) for i in range(20)]
print(data1);
# result=round()