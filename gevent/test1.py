import gevent

def work(n):
    for i in range(n):
        # 获取当前协程
        print(gevent.getcurrent(), i)
        # gevent.sleep(1)

g1 = gevent.spawn(work, 5)
g2 = gevent.spawn(work, 4)
g3 = gevent.spawn(work, 3)
g1.join()
g2.join()
g3.join()
