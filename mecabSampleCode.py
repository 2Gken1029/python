#! python3
# mecabSampleCode.py - Mecabの基本的な使い方

# Mecabがどこにあるか調べるコマンド
# $ echo `mecab-config --dicdir`"/mecab-ipadic-neologd"

import MeCab

mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd') # -d以下はechoで調べたパス

text = '解析したいテキスト'
mecab.parse('')#文字列がGCされるのを防ぐ
node = mecab.parseToNode(text)
while node:
    #単語を取得
    word = node.surface
    #品詞を取得
    pos = node.feature.split(",")[1]
    print('{0} , {1}'.format(word, pos))
    #次の単語に進める
    node = node.next
