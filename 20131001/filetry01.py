'''
Created on 2013-10-1

@author: casa
'''
import cPickle as p
class pp:
    def __init__(self,name):
        self.name=name
    def run(self):
        print 'fuck, I am running'
 
pp1=pp("zhangcasa")
pp1.run()
f=file('/home/casa/data.xt','w')
p.dump(pp1, f)
pp1.run()
f.close
f=file('/home/casa/data.xt')
pp_1=p.load(f)
pp_1.run()
# f1=file('/home/casa/data.xt')
 
 
# pp_1.run()
# while True:
#     line=f1.readline()
#     if len(line)==0:
#         break
#     print line
# f1.close()

# import cPickle as p
# #import pickle as p
# class pp:
#     def __init__(self,name):
#         self.name=name
#     def runcd(self):
#         print("cao")
# 
# shoplistfile = 'shoplist.data'
# # the name of the file where we will store the object
# 
# shoplist = ['apple', 'mango', 'carrot']
# pp1=pp("zhanglei")
# 
# # Write to the file
# f = file(shoplistfile, 'w')
# p.dump(pp1, f) # dump the object to a file
# f.close()
# 
# del shoplist # remove the shoplist
# 
# # Read back from the storage
# f = file(shoplistfile)
# storedlist = p.load(f)
# print(storedlist)

