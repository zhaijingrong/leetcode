import threading


# 按函数顺序打印字符
""" 使用互斥锁，锁定资源，在"""

def first():
    print("first")
    job1.release()

def second():
    job1.acquire()
    print("second")
    job2.release()

def third():
    job2.acquire()
    print("third")


if __name__ == '__main__':
    t1 = threading.Thread(target=first)
    t2= threading.Thread(target=second)
    t3= threading.Thread(target=third)

    job1 = threading.Lock()
    job2 = threading.Lock()
    job1.acquire()
    job2.acquire()

    t3.start()
    t2.start()
    t1.start()
