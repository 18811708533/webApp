#coding:utf-8
def test():
    from datetime import datetime
    now_time = datetime.now()
    a = 10
    a += 1
    b = "test string"
    print(now_time)

if __name__=="__main__":
    test()
    print ("Hello World")
