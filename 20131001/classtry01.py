'''
Created on 2013-10-1

@author: casa
'''
class person:
    def __init__(self,name):
        self.name=name
    def sayhello(self):
        print "hello cdcdcd"

p=person("zhanglei")
p.sayhello()

class std:
    school=0
    def __init__(self,name):
        self.name=name
    def add(self):
        print self.name+'is coming'
        std.school+=1
        print std.school
    def delete(self):
        print self.name+'is leaving'
        std.school-=1
        print std.school

std1=std("mike")
std1.add()
del std1

std2=std("tom")
std2.delete()


class schoolmem:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def havelunch(self):
        print "ok, I am eatting"

class student(schoolmem):
    def __init__(self,name,num,pay):
        schoolmem.__init__(self, name, num)
        self.pay=pay
    def paycao(self):
        print 'lll'
#         print 'i am get "%d"' % self.pay
    def jj(self):
        print 'cao'
    def havelunch(self):
        schoolmem.havelunch(self)
        print 'have lunch'
        
class teacher(schoolmem):
    def __init__(self,name,num,salary):
        schoolmem.__init__(self, name, num)
        self.salary=salary     
    def salarycao(self):
        print 'i am get "%d"' % self.salary
    def havelunch(self):
        print 'i am lunch'
        print self.name
        
student1=student("zhangcasa",1,123)
student1.havelunch()

teacher1=teacher("pop",2,234)
teacher1.salarycao()
teacher1.havelunch()
