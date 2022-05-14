from hashlib import sha1


#!/usr/bin/env python3
# coding: utf-8

def main():
    wat = int(input("指定された電子レンジ出力："))
    sec = int(input("秒数："))

    my_wat = int(input("自身の電子レンジ出力："))

    joule = wat*sec

    print(f"{my_wat}Wでの加熱時間は{joule/my_wat}秒.")

if __name__ == '__main__':
    main()