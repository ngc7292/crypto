#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'ngc7293'
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

from flask import Flask,request,jsonify,render_template
import base64
app = Flask(__name__)

app.jinja_env.variable_start_string = '{{{{'
app.jinja_env.variable_end_string = '}}}}'

def caesar_english(string,offset):
    '''
    this function to used to crypto the english (not only upper but lower),
    :param string: the string will be crypto
    :param offset: the offset of the crypto
    :return: string have been crypted
    '''
    f_list = []
    for i in string:
        #print(i)
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
        a = ord(i)
        f_list.append(chr((a - 32 + offset) % 94 + 32))
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
        a = ord(i)
        f_list.append(chr((a - 32 - offset) % 94 + 32))
    return ''.join(f_list)

def caesar_nb(string,offset):
    '''
    this function to used to crypto the english (not only upper but lower),
    :param string: the string will be crypto
    :param offset: the offset of the crypto
    :return: string have been crypted
    '''
    f_list = []
    for i in string:
        a = ord(i)
        if a >= ord('a') and a <= ord('z'):
            f_list.append(chr((a - ord('a') + offset) % 26 + ord('a')))
        elif a >= ord('A') and a <= ord('Z'):
            f_list.append(chr((a - ord('A') + offset) % 26 + ord('A')))
        elif a >= 33 and a <= 47:
            f_list.append(chr((a - 33 + offset) % 14 + 33))
        elif a >= ord('0') and a <= ord('9'):
            f_list.append(chr((a - ord('0') + offset) % 10 + ord('0')))
        elif a >= ord(':') and a <= ord('@'):
            f_list.append(chr((a - ord(':') + offset) % 7 + ord(':')))
        elif a >= ord('[') and a <= ord('`'):
            f_list.append(chr((a - ord('[') + offset) % 6 + ord('[')))
        elif a >= ord('{') and a <= ord('~'):
            f_list.append(chr((a - ord('{') + offset) % 4 + ord('{')))
        else:
            f_list.append(i)
    return ''.join(f_list)

def decry_caesar_nb(string,offset):
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
            f_list.append(chr((a - ord('a') - offset) % 26+ord('a')))
        elif a >= ord('A') and a<= ord('Z'):
            f_list.append(chr((a - ord('A') - offset) % 26 + ord('A')))
        elif a>= 33 and a<= 47:
            f_list.append(chr((a - 33 - offset) % 14 + 33))
        elif a>= ord('0') and a<= ord('9'):
            f_list.append(chr((a - ord('0') - offset) % 10 + ord('0')))
        elif a>= ord(':') and a<= ord('@'):
            f_list.append(chr((a - ord(':') - offset) % 7 + ord(':')))
        elif a>= ord('[') and a<= ord('`'):
            f_list.append(chr((a - ord('[') - offset) % 6 + ord('[')))
        elif a>= ord('{') and a<= ord('~'):
            f_list.append(chr((a - ord('{') - offset) % 4 + ord('{')))
        else:
            f_list.append(i)
    return ''.join(f_list)


@app.route('/encrypto',methods=['GET'])
def encrypto():
    if request.method == "GET":
        types = request.args.get('type')
        string = request.args.get('string')
        offset = request.args.get('offset')
        string = str(string).replace(' ','+')
        string = str(base64.b64decode(string))[2:-1]
        # print(string)
        
        if types == None or string == None or offset == None:
            return jsonify({'status':False})
        else:
            asd = ""
            offset = int(offset)
            if types == "1":
                asd = caesar_english(string,offset)
            #elif types == "2":
            #    asd = caesar_other(string,offset)
            elif types == "3":
                asd = decrypt_caesar_english(string,offset)
            #elif types == "4":
            #    asd = decrypt_caesar_other(string,offset)
            elif types == "5":
                asd = caesar_nb(string,offset)
            elif types == "6":
                asd = decry_caesar_nb(string,offset)
                
                
            r = {'status':True,'message':asd}
            return jsonify(r)
    else:
        return jsonify({'status':False})
    
@app.route("/")
def d():
    return render_template("caesar.html")

if __name__ == '__main__':
    app.run()