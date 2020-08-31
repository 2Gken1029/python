#! python3
# resizeAndAddLogo.py - カレントディレクトリのすべての画像を300*300に収まる
#                       ようにサイズ変更し、catlogo.pngを右下に追加する。

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo_im = Image.open(LOGO_FILENAME)
logo_width, logo_height = logo_im.size

os.makedirs('withLogo', exist_ok=True)

# カレントディレクトリの全画像をループする
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
        or filename == LOGO_FILENAME:
            continue # 画像以外とロゴ画像はスキップする

    im = Image.open(filename)

    # 画像をサイズ変更する
    im.thumbnail((SQUARE_FIT_SIZE, SQUARE_FIT_SIZE))
    width, height = im.size

    # ロゴを追加する
    print('ロゴを追加中 {}...'.format(filename))
    im.paste(logo_im, (width-logo_width, height-logo_height), logo_im)

    # 変更を保存する
    im.save(os.path.join('withLogo', filename))