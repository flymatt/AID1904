"""
进程属性
"""
from multiprocessing import Process
from time import sleep,ctime

def tm():
    for i in range(3):
        sleep(2)
        print(ctime())

if __name__=='__main__':
    p=Process(target=tm,name='tedu')
    p.daemon = True #子进程随父进程退出而退出
    p.start()
    print('Name:',p.name)
    print('PID:',p.pid)
    print('Is alive:',p.is_alive())
