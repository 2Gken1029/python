#! python3
# countdown.py - シンプルなカウンドダウンスクリプト

import time, subprocess

time_left = 60 # カウンドダウンの残り秒数
while time_left > 0:
    print(time_letf, end='')
    time.sleep(1)
    time_left = time_left - 1

# カウンドダウン後に音声ファイルを再生する
subprocess.Popen(['open', 'alarm.wav']) # 任意の音声ファイル