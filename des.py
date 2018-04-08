#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'ralph'
__mtime__ = '2018/4/2'
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

IP = [58, 50, 42, 34, 26, 18, 10,  2,
  60, 52, 44, 36, 28, 20, 12,  4,
  62, 54, 46, 38, 30, 22, 14,  6,
  64, 56, 48, 40, 32, 24, 16,  8,
  57, 49, 41, 33, 25, 17,  9,  1,
  59, 51, 43, 35, 27, 19, 11,  3,
  61, 53, 45, 37, 29, 21, 13,  5,
  63, 55, 47, 39, 31, 23, 15,  7
]

IP_1 = [40,  8, 48, 16, 56, 24, 64, 32,
  39,  7, 47, 15, 55, 23, 63, 31,
  38,  6, 46, 14, 54, 22, 62, 30,
  37,  5, 45, 13, 53, 21, 61, 29,
  36,  4, 44, 12, 52, 20, 60, 28,
  35,  3, 43, 11, 51, 19, 59, 27,
  34,  2, 42, 10, 50, 18, 58, 26,
  33,  1, 41,  9, 49, 17, 57, 25
]

S1 = [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
      0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
      4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
      15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
]

S2 = [15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
      3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
      0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
      13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9
]

S3 = [10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
      13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
      13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
      1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12
]

S4 = [7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
    13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
    10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
    3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
]

S5 = [2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
    14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
    4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
    11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3
]

S6 = [12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
    10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
    9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
    4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13
]

S7 = [4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
    13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
    1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
    6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12
]

S8 = [13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
      1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
      7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
      2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11
]

S = [S1,S2,S3,S4,S5,S6,S7,S8]

P = [16,  7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2,  8, 24, 14,
     32, 27,  3,  9,
     19, 13, 30,  6,
     22, 11,  4, 25
]

extend_table = [32,  1,  2,  3,  4,  5,
              4,  5,  6,  7,  8,  9,
              8,  9, 10, 11, 12, 13,
              12, 13, 14, 15, 16, 17,
              16, 17, 18, 19, 20, 21,
              20, 21, 22, 23, 24, 25,
              24, 25, 26, 27, 28, 29,
              28, 29, 30, 31, 32,1
]

PC_1 = [ 57, 49, 41, 33, 25, 17,  9,
         1, 58, 50, 42, 34, 26, 18,
         10,  2, 59, 51, 43, 35, 27,
         19, 11,  3, 60, 52, 44, 36,
         63, 55, 47, 39, 31, 23, 15,
         7, 62, 54, 46, 38, 30, 22,
         14,  6, 61, 53, 45, 37, 29,
         21, 13,  5, 28, 20, 12,  4
]

PC_2 = [ 14, 17, 11, 24,  1,  5,
         3, 28, 15,  6, 21, 10,
         23, 19, 12,  4, 26,  8,
         16,  7, 27, 20, 13,  2,
         41, 52, 31, 37, 47, 55,
         30, 40, 51, 45, 33, 48,
         44, 49, 39, 56, 34, 53,
         46, 42, 50, 36, 29, 32
]

def chr_to_bin(char):
    '''
    :param string:a char
    :return: 0 and 1 string
    '''
    s = bin(ord(char))[2:]
    l = 8 - len(s)
    f_list = []
    for i in range(l):
        f_list.append('0')
    for j in s:
        f_list.append(j)
    return ''.join(f_list)
    
def str_to_bin(s):
    f_list = []
    for ii in s:
        f_list.append(chr_to_bin(ii))
    return ''.join(f_list)
    
    
def bin_to_hex(s):
    '''
    a long bin string to recover to hex
    :param s:
    :return:
    '''
    
# ip exchange
    
def change_ip(n):
    '''
    :param n: a string or list which will be changed by ip
    :return: a string
    '''
    k_list = []
    for i in range(0,len(n),7):
        a = n[i:i+7]
        if a.count('1')%2 == 0 :
            a += '0'
        else:
            a += '1'
        k_list.append(a)
    n = ''.join(k_list)
    #print(n)
    
    f_list = ['0' for i in range(64)]
    for i in range(64):
        f_list[i] = n[IP[i] - 1]
        
    return ''.join(f_list)


def change_ip_1(n):
    '''
    
    :param n: string
    :return:  string
    '''
    f_list = ['0' for i in range(64)]
    for i in range(64):
        f_list[i] = n[IP_1[i] - 1]
    
    return ''.join(f_list)


def get_L_R(n):
    return n[:32],n[32:]


# The Feistel (F) function

def extend_change(r):
    '''
    input 8*4=32bits and output 8*6=48bits input is r(i-1)
    :param r: string
    :return: string
    '''
    f_list = ['0' for i in range(48)]
    for i in range(48):
        f_list[i] = r[extend_table[i]-1]
    
    return ''.join(f_list)
    
def xor_key(e_f,key):
    f_list = []
    for i in range(len(e_f)):
        a = str(int(e_f[i])^int(key[i]))
        f_list.append(a)
    return ''.join(f_list)
        
def s_exchange(x_f):
    '''
    input 8*6 = 48bits and output 8*4 = 32bits s exchange box
    :return: string
    '''
    x_list =[ x_f[i:i+6] for i in range(0,48,6)]
    r_f = ""
    for i in range(len(x_list)):
        x_cols = int(x_list[i][0]+x_list[i][5],2)
        x_rows = int(x_list[i][1:5],2)
        x_nums = x_cols*16+x_rows
        s_e = bin(S[i][x_nums])[2:]
        for i in range(4-len(s_e)):
            s_e = '0'+s_e
        r_f += s_e
        # print(x_list[i],x_cols,x_rows,s_e)
    
    return r_f
    
def p_exchange(x_f):
    '''
    input 32bits and output 32bits which like ip exchange
    :param x_f: string
    :return: string
    '''
    f_list = ['0' for i in range(32)]
    for i in range(32):
        f_list[i] = x_f[P[i]-1]
    return ''.join(f_list)

def xor_pf_l(p_f,L):
    '''
    after p box exchange the result xor with l(i-1) to output r(i)
    :param p_f:
    :param L:
    :return:
    '''
    f_list = []
    for i in range(32):
        f_num = str(int(p_f[i])^int(L[i]))
        f_list.append(f_num)
    
    return ''.join(f_list)


#the key extend
def key_extend(k):
    '''
    from a key which 56 bits to extend 16 keys every one is 48bits
    :param k: a string 56 bits
    :return: a list had 16 keys
    '''
    f_cd_list = ['0' for i in range(56)]
    #k_list = []
    #for i in range(0,len(k),7):
    #    a = k[i:i+7]
    #    if a.count('1')%2 == 0 :
    #        a += '0'
    #    else:
    #        a += '1'
    #    k_list.append(a)
    #k = ''.join(k_list)
    
    
    for i in range(56):
        f_cd_list[i] = k[PC_1[i]-1]
        
    f_cd = "".join(f_cd_list)
    
    # C,D is string's list
    C = [f_cd[:28]]
    D = [f_cd[28:]]
    F_CD = [f_cd]
    k_list = []
    for i in range(16):
        if i+1 in [1,2,9,16]:
            c = C[i][1:]+'0'
            d = D[i][1:]+'0'
        else:
            c = C[i][2:]+'00'
            d = D[i][2:]+'00'
        C.append(c)
        D.append(d)
        F_CD.append(c+d)
        cd = c+d
        k = ""
        for i in range(48):
            k += cd[PC_2[i]-1]
        k_list.append(k)
    
    return k_list

def des_encrypt(crypto,key):
    '''
    the main function of the des crypto
    :param crypto: a string
    :param key: a string
    :return: a 64 bits string
    '''
    if len(key) != 8:
        return False
    crypto = str_to_bin(crypto)
    print(crypto)
    c_p = len(crypto)%64
    if c_p != 0:
        crypto += '0'*(56-c_p)
    key = str_to_bin(key)
    print(len(key))
    key_list = key_extend(key)
    L_R = change_ip(crypto)
    l,r = get_L_R(L_R)
    L = [l]
    R = [r]
    for i in range(16):
        e_f = extend_change(R[i])
        x_f = xor_key(e_f,key_list[i])
        s_f = s_exchange(x_f)
        p_f = p_exchange(s_f)
        xor_f = xor_pf_l(p_f,L[i])
        if i != 15:
            R.append(xor_f)
            L.append(R[i])
        else:
            R.append(R[i])
            L.append(xor_f)
    
    L_R = L[16]+R[16]
    m = change_ip_1(L_R)
    
    return m





if __name__ == '__main__':
    key = 'abcdefgh'
    a = 'aaaaaaaa'
    c = des_encrypt(a,key)
    print(c)
    
    
    