import random

def horoscope():
    horoscope = ["牡羊座","おうし座","ふたご座","かに座","しし座","おとめ座","てんびん座","さそり座","いて座","やぎ座","みずがめ座","うお座"]
    random.shuffle(horoscope)
    for n, i in enumerate(horoscope, 1):
        print(f"第{n}位は{i}のあなた!")