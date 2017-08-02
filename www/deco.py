from time import ctime

def deco1(func):
    def decorator1(*args,**kwargs):
        print ('[%s] %s is called'%(ctime(),func.__name__))
        return func(*args,**kwargs)
    return decorator1
def deco2(func):
    def decorator2(*args,**kwargs):
        print ('[%s] %s is called'%(ctime(),func.__name__))
        return func(*args,**kwargs)
    return decorator2

@deco1
@deco2
def foo():
    print ('Hello World!')

foo()