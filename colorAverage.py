#! python3
# colorAverage.py - 指定画像のRGB,HSVの値を取得

import cv2
import os
import glob

files = glob.glob('../Desktop/hoge/result/*.png')

first_R = []
first_G = []
first_B = []

middle_R = []
middle_G = []
middle_B = []

end_R = []
end_G = []
end_B = []

for file in files:
    # 対象画像読み込み
    img = cv2.imread(file,cv2.IMREAD_COLOR)

    # 画像サイズ取得
    height, width, channeels = img.shape[:3]
    width_cut = width / 3

    boxToX = 0

    for i in range(3):
        # 対象範囲を切り出し
        boxFromX = boxToX #対象範囲開始位置 X座標
        boxFromY = 0 #対象範囲開始位置 Y座標
        boxToX = boxFromX + width_cut #対象範囲終了位置 X座標
        boxToY = height #対象範囲終了位置 Y座標
        # print("X始点"+str(boxFromX) + "　，　" + "X終点"+str(boxToX))
        # y:y+h, x:x+w　の順で設定
        imgBox = img[int(boxFromY): int(boxToY), int(boxFromX): int(boxToX)]

        # RGB平均値を出力
        # flattenで一次元化しmeanで平均を取得 
        b = imgBox.T[0].flatten().mean()
        g = imgBox.T[1].flatten().mean()
        r = imgBox.T[2].flatten().mean()

        # RGBの最大値のみを取得
        if(i == 0): # 前半
            first_R.append(r)
            first_G.append(g)
            first_B.append(b)
        elif(i == 1): # 中盤
            middle_R.append(r)
            middle_G.append(g)
            middle_B.append(b)
        elif(i == 2): # 後半
            end_R.append(r)
            end_G.append(g)
            end_B.append(b)
        else:
            print('異常発生')

        # RGB平均値を取得
        # if(i == 0):
        #     print('----前----')
        #     print("R: %.2f" % (r))
        #     print("G: %.2f" % (g))
        #     print("B: %.2f" % (b))
        # elif(i == 1):
        #     print('----中----')
        #     print("R: %.2f" % (r))8
        #     print("G: %.2f" % (g))
        #     print("B: %.2f" % (b))
        # elif(i == 2):
        #     print('----後----')
        #     print("R: %.2f" % (r))
        #     print("G: %.2f" % (g))
        #     print("B: %.2f" % (b))
        # else:
        #     print('異常が発生')

def average(list):
    average = sum(list)/len(list)
    return average



print('前の各色の平均値　R: ' + str(average(first_R)) + ', G: ' + str(average(first_G)) + ', B: ' + str(average(first_B)))
print('中の各色の平均値　R: ' + str(average(middle_R)) + ', G: ' + str(average(middle_G)) + ', B: ' + str(average(middle_B)))
print('後の各色の平均値　R: ' + str(average(end_R))+ ', G: ' + str(average(end_G)) + ', B: ' + str(average(end_B)))
