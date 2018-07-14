#!/usr/bin/env python

from __future__ import with_statement
from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

lock = Lock()
loops = (randrange(2,5) for x in range(randrange(3,7)))
remaining = CleanOutputSet()


def loop(nsec):
    myname = currentThread().name

    #上下文管理器
    with lock:
        remaining.add(myname)
        print('[%s] Started %s' %(ctime(), myname))
    sleep(nsec)
    with lock:
        remaining.remove(myname)
        print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
        print('(remaining: %s)' % (remaining or 'None'))

    '''   
    lock.acquire()
    remaining.add(myname)
    print('[%s] Started %s' %(ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('[%s] Completed %s (%d secs)' %(ctime(), myname, nsec))
    print('(remaining: %s)' %(remaining or 'None'))
    lock.release()
    '''

def main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@register
def atexit():
    print('all DONE at: %s' %ctime())

if __name__ == '__main__':
    main()