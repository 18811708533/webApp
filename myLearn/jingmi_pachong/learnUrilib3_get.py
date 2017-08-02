#coding:utf-8
#get method ,can show  password and username in the lasrt of url
import urllib2
import urllib
values= {"username":"a15216115048","password":"zhang123yuling"}
data= urllib.urlencode(values)
url = "http://www.csdn.net/111S"
geturl=url+"?"+data
#geturl=url
request = urllib2.Request(geturl)

try:
    response=urllib2.urlopen(request)
    resstr = response.read()
    #将爬取的页面写入文档。
    f=open(r"C:\Users\cmri\WebApp\myLearn\jingmi_pachong\learnUrllib3.html","w")
    f.write(resstr)
    f.close()
    print "OK"
except urllib2.HTTPError,e:
    if hasattr(e,"reason"):
        print e.reason,e.code
    else:
        print "HTTPError has no attr"

except urllib2.URLError,e:
    print e.reason
    print "NO"
