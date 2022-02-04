#!/usr/bin/env python3
# coding: utf-8

class Dog():

    def __init__(self, name):
        self._name = name

    # ゲッター
    @property
    def name(self):
        return self._name

    # セッター
    @name.setter
    def name(self, value):
        self._name = value
    

def main():
    # インスタンス
    dog = Dog(name='レオ')
    print(dog.name)

    dog.name = "チョコ"
    print(dog.name)

if __name__ == '__main__':
    main()


