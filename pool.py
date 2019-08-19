"""
进程池
"""
from multiprocessing import Pool
from time import sleep,ctime

# 进程池事件
def fun(msg):
    for i in range(3):
        sleep(2)
        print(msg)
        return ctime()

if __name__=='__main__':
    # 创建进程池
    pool=Pool()
    # 向进程池添加执行时间
    for i in range(20):
        msg='hello %d'%i
        # r代表func事件的对象
        r=pool.apply_async(fun,args=(msg,))
    # 关闭进程池
    pool.close()
    # 回收进程池
    pool.join()
    # 获取事件函数的返回值
    print(r.get())