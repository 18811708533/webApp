#coding:utf-8

#爬取段子
def scrap_choushibaike():
    import urllib
    import urllib2
    page = 1
    url = 'https://www.qiushibaike.com/hot/page/' + str(page)+'/'
    user_agent	="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
    headers = { 'User-Agent':user_agent }
    try:
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        filecontent =response.read()
        return filecontent
    except urllib2.HTTPError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason


#将爬取的页面写入文档。
def writeToFile(filecontent,fileroute):
    #r"C:\Users\cmri\WebApp\myLearn\jingmi_pachong\pachong_shizhan\choushibaike.html"
    f=open(fileroute,"w")
    f.write(filecontent)
    f.close()
    print "Has writed filecontent to "+str(fileroute)

#得到段子的用户名和段子内容
def analysisHtml(filecontent):
    import re
    content=filecontent.decode('utf-8')
    #pattern=re.compile("<div class="article block untagged mb15 typs_hot"(*)</div>")
    pattern = re.compile('<div class="article block untagged mb15 typs_hot" id=.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>',re.S)
    items=re.findall(pattern,content)
    print len(items)
    for item in items:
        print item[0],item[1]

#得到图片链接
def getImg(filecontent):
    import re
    content=filecontent.decode('utf-8')
    pattern = re.compile('<div class="article block untagged mb15 typs_hot" id=.*?<img src="(.*?)" alt=.*?<h2>.*?</h2>.*?<span>.*?</span>',re.S)
    items=re.findall(pattern,content)
    return items

#创建新目录
def mkdir(path):
    import os
    path = path.strip()
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print u"偷偷新建了名字叫做",path,u'的文件夹'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print u"名为",path,'的文件夹已经创建成功'
        return False
#下载图片
def downloadImg(items,fileroute):
    import urllib2
    mkdir(fileroute)
    i=0
    for item in items:
        i=i+1
        f=open(fileroute+"/"+str(i)+".jpg",'wb')
        try:
            u = urllib2.urlopen("http:"+item)
            f.write(u.read())
            print "写入图片"+str(i)+".jpg"
            f.close()
        except urllib2.URLError,e:
            print e.reason
def test():
    fileroute= "C:\Users\cmri\WebApp\myLearn\jingmi_pachong\pachong_shizhan\choushibaike"
    mkdir(fileroute)
    i  = 1
    f=open(fileroute+"/"+str(i)+".jpg",'wb')
    f.write("123")
    print "wang "+ fileroute+"/"+str(i)+".jpg"+"写入了数据"
    f.close()

if __name__ == '__main__':
    filecontent= scrap_choushibaike()
    writeToFile(filecontent,r"C:\Users\cmri\WebApp\myLearn\jingmi_pachong\pachong_shizhan\choushibaike.html")
    #analysisHtml(filecontent)
    imgset=getImg(filecontent)
    downloadImg(imgset,"C:\Users\cmri\WebApp\myLearn\jingmi_pachong\pachong_shizhan\choushibaike")
