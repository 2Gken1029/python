import time
def calc_prod():
    # 1~99,999の積を求める
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

start_time = time.time()
prod = calc_prod()
end_time = time.time()
print('計算結果は{}桁です。'.format(len(str(prod))))
print('計算時間は{}秒でした。'.format(end_time - start_time))