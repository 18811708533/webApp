#!/usr/bin/python  
# -*- coding:UTF-8 -*-  

#调用pandas numpy matplotlib包  
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#将hun.txt里卖弄的数据转换成newdata.txt需要的格式
def hun_changto_newdata(): 
    f=open("newdata.txt","w")
    for i in open('hun.txt','r'):
        strtime=i[1:-2].split(',')[0].strip("'")
        strtime=i[2:11]
        strnum=i[16:-3]
        #print strtime 
        #print strnum
        print strtime+","+strnum
        f.write(strtime+","+strnum+"\n")
    f.close()
#将‘2017-06-13’字符串转换成日期类型
def strtime_to_datetime(strtime):
    import time
    t=time.strptime(strtime,"%Y-%m-%d")
    return time.strftime("%Y-%m-%d",time.localtime(time.mktime(t)))

def plot_blue():
    #读取newdata.txt文件  
    df = pd.read_table('newdata.txt',header=None,sep=',')  
    # print df  
    # print df[1:3]    #第2到第3行（索引0开始为第一行，1代表第二行，不包含第四行）  
    # print df.loc[0:10,:]    #第1行到第9行的全部列  
    # print df.loc[:,[0,7]]  #全部行的第1和第8列  
    tdate = sorted(df.loc[:,0])     #取第一列数据  
    # print tdate  
      
    tdate1 = []    #将tdate数据读取到列表中  
    for i in tdate:  
        tdate1.append(i)  
    print tdate1  
      
    # s = pd.Series(tdate1, index=tdate1)  
    s = pd.Series(range(1,len(tdate1)+1), index=tdate1)    #将日期转换为对应的数值从1开始  
    # print s  
      
    tblue = list(reversed(df.loc[:,7]))    #对数据取反  
    print tblue  
      
      
    fenzu = pd.value_counts(tblue,ascending=False)    #将数据进行分组统计，按照统计数降序排序  
    print fenzu  
    x=list(fenzu.index[:])    #获取蓝色号码  
    y=list(fenzu.values[:])    #获得蓝色统计数量  
    print x  
    print y  
      
    # print type(fenzu)  
    plt.figure(figsize=(10,6),dpi=70)    #配置画图大小、和细度  
    plt.legend(loc='best')       
    # plt.plot(fenzu,color='red')    #线图  
    plt.bar(x,y,alpha=.5, color='b',width=0.8)    #直方图参数设置  
    plt.title('The blue ball number')    #标题  
    plt.xlabel('blue number')    #x轴内容  
    plt.ylabel('times')    #y轴内容  
    plt.show()    #显示图  

 
def analyze_data_hong():      
    #读取文件  
    df = pd.read_table('newdata.txt',header=None,sep=',')  
    # print df  
    # print df[1:3]  
    # print df.loc[0:10,:]  
    # print df.loc[:,1:6]  
    tdate = sorted(df.loc[:,0])  
    # print tdate  
    h1 = df.loc[:,1]  
    h2 = df.loc[:,2]  
    h3 = df.loc[:,3]  
    h4 = df.loc[:,4]  
    h5 = df.loc[:,5]  
    h6 = df.loc[:,6]  
      
    #将数据合并到一起  
    all = h1.append(h2).append(h3).append(h4).append(h5).append(h6)  
    alldata = list(all)  
    print len(alldata)  
      
    fenzu = pd.value_counts(all,ascending=False)  
    print fenzu  
      
    x=list(fenzu.index[:])  
    y=list(fenzu.values[:])  
    print x  
    print y  
      
    # print type(fenzu)  
    plt.figure(figsize=(10,6),dpi=70)  
    plt.legend(loc='best',)  
      
      
    # plt.plot(fenzu,color='red')  
    plt.bar(x,y,alpha=.5, color='r',width=0.8)  
    plt.title('The red ball number')  
    plt.xlabel('red number')  
    plt.ylabel('times')  
    plt.show()  

def tongji_zuhe_max():
    #!/usr/bin/python  
    # -*- coding:UTF-8 -*-  
    import pandas as pd  
    import numpy as np  
    import matplotlib.pyplot as plt  
    import operator  
      
    df = pd.read_table('newdata.txt',header=None,sep=',')  
      
    tdate = sorted(df.loc[:,0])  
    # print tdate  
    h1 = df.loc[:,1:7:6].values    #取第一列红球和蓝球  
    # print h1  
    h2 = df.loc[:,2:7:5].values    #取第二列红球和蓝球  
    h3 = df.loc[:,3:7:4].values  
    h4 = df.loc[:,4:7:3].values  
    h5 = df.loc[:,5:7:2].values  
    h6 = df.loc[:,6:7:1].values  
    # tblue = df.loc[:,7]  
      
    #将上方切分的所有数据组合到一起  
    data = np.append(h1, h2, axis = 0)  
    data = np.append(data, h3, axis = 0)  
    data = np.append(data, h4, axis = 0)  
    data = np.append(data, h5, axis = 0)  
    data = np.append(data, h6, axis = 0)  
    # print data  
      
      
    data1 = pd.DataFrame(data)  
    # print data1  
    #写入到一个文件中  
    data1.to_csv('hldata.csv',index=None,header=None)  
      
    #读取文件，将组合进行统计并从大到小排序  
    f = open("hldata.csv")  
    count_dict = {}  
    for line in f.readlines():  
        line = line.strip()  
        count = count_dict.setdefault(line, 0)  
        count += 1  
        count_dict[line] = count  
    sorted_count_dict = sorted(count_dict.iteritems(), key=operator.itemgetter(1), reverse=True)  
    # for item in sorted_count_dict:  
    #     print "%s,%d" % (item[0], item[1])  
      
    # print sorted_count_dict  
      
    fenzu = pd.DataFrame(sorted_count_dict).set_index([0])  
    #print fenzu  
      
    #分别从第一列和第二列取前19个数据放到x y中  
    x = list(fenzu.index[:19])  
    y = list(fenzu.values[:19])  
    print x  
    print y  
      
    #将x对应数值，不然画图报错  
    s = pd.Series(range(1,len(x)+1), index=x)  
      
    #设置画图属性  
    plt.figure(figsize=(12,6),dpi=80)  
    plt.legend(loc='best')  
      
    # plt.plot(fenzu,color='red')  
    plt.bar(s,y,alpha=.5, color='r',width=0.8)  
    plt.title('The one red and one blue ball number')  
    plt.xlabel('one red and one blue number')  
    plt.ylabel('times')  
      
    #可以在图中放置标签字符  
    # for i in  range(0,19):  
    #     plt.text(int(i+1.4),25,x[i],color='b',size=10)  
    # plt.text(1.4,20,x[0],color='g',ha='center')  
      
    #将['1,12', '26,9', '5,13']这样的字符放到图中  
    plt.xticks(s,x, rotation=10,size=10,ha='left')  
    plt.show()  

if __name__=="__main__":
    #hun_changto_newdata()
    #plot_blue()
    #analyze_data_hong()
    tongji_zuhe_max()