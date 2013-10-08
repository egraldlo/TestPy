'''
Created on 2013-10-6

@author: casa
'''
# import urllib
# def getHtml(url):
#     page=urllib.urlopen(url)
#     html=page.readlines()
#     page.close()
#     return html
# 
# pp=getHtml("http://movie.douban.com/")
# print(pp)

print("\n")

import re
text="is a handsome boy, he she JGood is cool, clever, JGood  and so on..."
m = re.match(r"(\w+)\s", text)
print re.sub(r'\s+', '-', text,)
s = re.search(r"(\w+)\s", text)
sp=re.split(r'\s+', text)
print sp
print s.group(0),'ok'
f=re.findall(r"(\w+)\s", text)
print f,'oooo'
if m:
    print m.group(0),'\n',m.group(1)
else:
    print "no match"

c=re.compile(r"(\w+)\s")
# print c.sub(r'\s+', '-', text,)
s1 = c.search(text)
# sp=c.split(r'\s+', text)
# print sp
print s1.group(0),'ok'
# f1=c.findall(r"(\w+)\s", text)
# print f1

m1=re.findall('\bshe\b',text)
print(m1)





















