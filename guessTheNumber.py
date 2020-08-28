#数当てゲーム
import random
select_number = random.randint(1,20)
print("1から20までの数を当ててください。")

#六回聞く
for guesses_taken in range(1,7):
    print("数を入力してください。")
    guess = int(input())

    if guess < select_number:
        print("小さいです。")
    elif guess > select_number:
        print("大きいです。")
    else:
        break

if guess == select_number:
    print("当たり！" + str(guesses_taken) + "回で当たりました！")
else:
    print("残念。正解は" + str(select_number) + "でした。")