#!/usr/bin/env python3
# coding: utf-8

import time

def main():
    str = "hoge"*100000

    start = time.time()
    reverse_1(str)
    print ("reverse_1 time:{0}".format(time.time() - start) + "[sec]")

    start = time.time()
    reverse_2(str)
    print ("reverse_2 time:{0}".format(time.time() - start) + "[sec]")

    start = time.time()
    reverse_3(str)
    print ("reverse_3 time:{0}".format(time.time() - start) + "[sec]")

    start = time.time()
    reverse_4(str)
    print ("reverse_4 time:{0}".format(time.time() - start) + "[sec]")

    start = time.time()
    reverse_5(str)
    print ("reverse_5 time:{0}".format(time.time() - start) + "[sec]")


def reverse_1(str): # スライス
    reverse_str = str[::-1]
    # print(reverse_str)

def reverse_2(str): # for
    reverse_str = ""
    for i in range(len(str)-1, -1, -1):
        reverse_str += str[i]
    # print(reverse_str)

def reverse_3(str): # while
    reverse_str = ""
    i = len(str)
    while i > 0: 
        reverse_str += str[i-1]
        i = i - 1
    # print(reverse_str)

def reverse_4(str): # reversed
    reverse_str=''.join(reversed(str))
    # print(reverse_str)

def reverse_5(str): # 前後の文字を入れ替え
    str_list = list(str)
    l = len(str_list)
    for i, j in zip(range(l-1, 0, -1), range(l//2)):
        str_list[i], str_list[j] = str_list[j], str_list[i]
    # print("".join(t))


if __name__ == '__main__':
    main()