#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'ralph'
__mtime__ = '2018/4/4'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓
            ┃       ┃
            ┃ ┳┛ ┗┳ ┃
            ┃   ┻   ┃
            ┗━┓   ┏━┛
              ┃   ┗━━━┓
              ┃神兽保佑┣┓
              ┃永无BUG  ┏┛
              ┗┓┓┏━┳┓┏━┛
               ┃┫┫ ┃┫┫
               ┗┻┛ ┗┻┛
"""

import random


def gcd(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    while n2 != 0:
        temp = n1 % n2
        n1 = n2
        n2 = temp
    return n1

def get_e(n):
    e = random.randint(1,n)
    g = gcd(n, e)
    while(g != 1):
        e = random.randint(1,n)
        g = gcd(n,e)
    
    
    return e

# extend gcd to execulate the d
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def getd(e, n):
    g, x, y = egcd(e, n)
    if g != 1:
        return False
    else:
        return x % n

def rsa_encrypt(m, e, n):
    return (m**e)%n

def rsa_decrypt(c, d, n):
    return (c**d)%n



