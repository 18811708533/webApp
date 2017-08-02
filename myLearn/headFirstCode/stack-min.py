#--coding:utf-8--
class MinStack(object):
    def __init__(self):
        self.data=[]
        self.minValue=[]
    def push(self,data):
        self.data.append(data)
        if len(self.minValue)==0:
            self.minValue.append(data)
        elif data<=self.minValue[-1]:
            self.minValue.append(data)
    def pop(self):
        if len(self.data)==0:
            return None
        else:
            temp=self.data.pop()
            if temp == self.minValue[-1]:
                self.minValue.pop()
            return temp
    def getMin(self):
        if len(self.data)==0:
            return None
        else:
            return self.minValue[-1]

    def show(self):
        print 'stack data'
        for  data in self.data:
            print data

        print 'min:',self.getMin()

if  __name__=='__main__':
    s=MinStack()
    s.push(2)
    s.push(1)
    s.show()
    s.push(4)
    s.push(3)
    s.push(2)
    s.show()
    s.pop()
    s.show()
    s.pop()
    s.pop()
    s.show()

