#coding:utf-8
#urllib2的基本用法，加入用户名和密码.POSt方法，比较安全
import urllib2
import urllib
values= {"username":"a15216115048","password":"zhang123yuling"}
data= urllib.urlencode(values)
url = "http://www.csdn.net/"
request = urllib2.Request(url,data)
response=urllib2.urlopen(request)
resstr = response.read()
#将爬取的页面写入文档。
f=open(r"C:\Users\cmri\WebApp\myLearn\jingmi_pachong\learnUrllib3.html","w")
f.write(resstr)
f.close()


