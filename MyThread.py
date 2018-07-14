#!/usr/bin/env python

import threading
from time import ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print('starting %d at: %s' %(self.name, ctime()))
        self.res = self.func(*self.args)
        print('%s finished at: %s' %(self.name, ctime()))