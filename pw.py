#! pyhton3
# pw.py - パスワード管理プログラム(脆弱性あり)

PASSWORDS = {'email': 'sample@mail.com',
             'blog': 'sampleblog.com',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方: Python3 pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.argv[1] # 最初のコマンドライン引数がアカウント名

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました')
else:
    print(account + 'というアカウント名はありません')