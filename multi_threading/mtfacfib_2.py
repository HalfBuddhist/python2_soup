#!/usr/bin/env python
# coding=utf-8
"""
例18.8 斐波那契，阶乘和累加和 (mtfacfib.py)
在这个多线程程序中，我们会分别在单线程和多线程环境中，运行三个递归函数。
"""

from time import ctime, sleep

from multi_threading.myThread import MyThread


def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x-2) + fib(x-1))

def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return (x * fac(x-1))

def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return (x + sum(x-1))

funcs = [fib, fac, sum]
n = 12

def main():
    nfuncs = range(len(funcs))
    print '*** SINGLE THREAD'

    for i in nfuncs:
        print 'starting', funcs[i].__name__, 'at:', ctime()
        print funcs[i](n)
        print funcs[i].__name__, 'finished at:', ctime()

    print '\n*** MULTIPLE THREADS'
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (n,), funcs[i].__name__) #the tuple with one element
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print threads[i].getResult()

    print 'all DONE'

if __name__ == '__main__':
    main()