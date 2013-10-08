# -*- coding: utf-8 -*-
'''
Created on 2013-10-6

@author: casa
'''
import urllib
import re
import chardet

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    page.close()
    return html

def changeCode(code_new):
    mychar=chardet.detect(code_new)
    bianma=mychar['encoding']
    if bianma == 'utf-8' or bianma == 'UTF-8':
        code_old=code_new
    else :
        code_old=code_new.decode('gb2312','ignore').encode('UTF-8')
    return code_old
    
    
    
if  __name__=='__main__':
    pp=getHtml("http://movie.douban.com/")
    ppp=changeCode(pp)
    fi=file('/home/casa/data.txt','w')
    fi.write(ppp)
    fi.close()
    
    love=getHtml("http://movie.douban.com/category/#search/types/%E7%88%B1%E6%83%85/district/%E7%BE%8E%E5%9B%BD")
    love_new_code=changeCode(love)
    file_love=file('/home/casa/love.txt','w')
    file_love.write(love_new_code)
    file_love.close()
    
    f=re.findall(ur'电影'.encode('utf-8'),ppp)
    print " ".join(f)
    
    line='zhangleicasa@gmail.com'
    urlweb='http://www.baidu.com'
    re_mail=re.compile(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$".encode('utf-8'))
    re_url=re.compile(r"[a-zA-Z0-9_]{6,12}@[a-zA-Z0-9]+(\\.[a-zA-Z]+)+".encode('utf-8'))
    re_chinese=re.compile(r"http://[\d\-a-zA-Z]+(\.[\d\-a-zA-Z]+)*/?$".encode('utf-8'))
    
    re_ww=re.compile(r"href=\"http://[a-z|A-Z|.]+/subject/[0-9]+/\"".encode('utf-8'))
    
    ff=re_mail.findall(line)
    print ff
    
    f_web=re_url.findall(urlweb)
    print f_web
    
    f_ch=re_ww.findall(ppp)
    print f_ch
    site_file=file('/home/casa/site.txt','w')
    for i in f_ch:
        sp=re.sub(r"href=",' ',i)
        sp_=sp.strip().split()
        site=''.join(sp_[-1])
        site_file.write(site+'\n')
    site_file.close()
    
    
#     print " ".join(f_ch)
    
#     file_ch=file('/home/casa/data_ch.txt','w')
#     file_ch.write(" ".join(f_ch))
#     file_ch.close()
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print 'ok'
#     print "zhanglei".replace('zhang','tu')
#     line1='jcdcdcdsdcdcdv2233'
#     print "898777777778dcdda".replace("\\d",'-')
#     line1_=re.findall(r"[a-z]{3}",line1)
#     print line1_
#     
#     line2='aa7jaajajjaajaaaa'
#     re2=re.compile(r'a*')
#     re2_=re2.findall(line2)
#     print re2_;
    
    print('草')

    


