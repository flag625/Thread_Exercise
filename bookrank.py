#!/usr/bin/env python

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen


REGEX = compile(b'#([\d,]+) in Bookes')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}

def getRanking(isbn):
    page = uopen('%s%s' %(AMZN, isbn))  #or str.format()
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]

def _showRanking(isbn):
    print('_%r ranked %s' %(ISBNs[isbn], getRanking(isbn)))

def main():
    print('At %s on Amazon...' %ctime())
    for isbn in ISBNs:
        _showRanking(isbn)

@register
def _atexit():
    print('all Done at: %s' %ctime())

if __name__ == '__main__':
    main()