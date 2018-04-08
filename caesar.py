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
def caesar_english(string,offset):
    '''
    this function to used to crypto the english (not only upper but lower),
    :param string: the string will be crypto
    :param offset: the offset of the crypto
    :return: string have been crypted
    '''
    f_list = []
    for i in string:
        a = ord(i)
        if a >= ord('a') and a<= ord('z'):
            f_list.append(chr((a  - ord('a') + offset)%26+ord('a')))
        elif a >= ord('A') and a<= ord('Z'):
            f_list.append(chr((a - ord('a') + offset) % 26 + ord('a')))
        else:
            f_list.append(i)
    return ''.join(f_list)



def caesar_other(string,offset):
    f_list = []
    for i in string:
        a = chr(ord(i)+offset)
        f_list.append(a)
    return ''.join(f_list)

def decrypt_caesar_english(decrypted , offset):
    f_list = []
    for i in decrypted:
        a = ord(i)
        if a >= ord('a') and a<= ord('z'):
            f_list.append(chr((a  - ord('a') - offset)%26+ord('a')))
        elif a >= ord('A') and a<= ord('Z'):
            f_list.append(chr((a - ord('a') - offset) % 26 + ord('a')))
        else:
            f_list.append(i)
    return ''.join(f_list)


def decrypt_caesar_other(decrypted , offset):
    f_list = []
    for i in decrypted:
        a = chr(ord(i) - offset)
        f_list.append(a)
    return ''.join(f_list)


    