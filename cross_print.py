import threading

# 交叉打印，两个数组1-26，A-Z，使用两个线程，交叉打印出1A，2B，..., 26Z。



def print_alpha():
    for i in range(65, 65+26):
        s1.acquire()
        print(chr(i))
        s2.release()

def print_number():
    for i in range(1, 27):
        s2.acquire()
        print(i, end='')
        s1.release()
    

if __name__ == '__main__':
    t1 = threading.Thread(target=print_alpha)
    t2 = threading.Thread(target=print_number)

    s1 = threading.Semaphore(0)
    s2 = threading.Semaphore(1)

    t2.start()
    t1.start()