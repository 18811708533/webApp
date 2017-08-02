#urllib2的基本用法
import urllib2
response=urllib2.urlopen("http://www.baidu.com")
print response.read()

print "Hello"