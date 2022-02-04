#!/usr/bin/env python3
# coding: utf-8

class Animal():

    def __init__(self, name, weight):
        # 名前
        self.name = name
        # 体重[kg]
        self.weight = weight

    # 寝る
    def sleep(self):
        print(self.name, "寝る")
    #食べる
    def eat(self):
        print(self.name, "食べる")

    # オーバーライド
    def make_sound(self):
        # 子クラスでオーバーライドしなくても良い場合
        # pass

        # 子クラスでオーバーライドして欲しい場合
        raise NotImplementedError

class Dog(Animal):

    def __init__(self, name, weight, breed):
        super().__init__(name, weight)

        # 犬種
        self.breed = breed

    # ゲッター
    @property
    def name(self):
        return self._name

    # 走る
    def run(self, speed = '普通'):
        if speed == '普通':
            print(self.name, "走る")
        elif speed == '速い':
            print(self.name, "速く走る")
        elif speed == '遅い':
            print(self.name, "遅く走る")

    # 吠える
    def make_sound(self):
        print(self.name, "ワン!ワン!")

class Bird(Animal):

    def __init__(self, name, weight, types):
        super().__init__(name, weight)

        # 鳥の種類
        self.types = types

    # 飛ぶ
    def fly(self):
        print(self.name, "飛ぶ")

    # 鳴く
    def make_sound(self):
        print(self.name, "ピー!ピー!")

def main():
    # インスタンスの作成
    animal = Animal('ペコ',100)
    dog = Dog("チョコ", "ビーグル", 10)
    bird = Bird("ピー", "インコ", 1)

    # プロパティを使う
    # print(animal.name, animal.weight)

    

    # メソッドを使う
    # animal.sleep()
    # dog.sleep()
    # dog.run()
    # dog.make_sound()
    # dog.run()
    # dog.run(speed='速い')

    # bird.sleep()
    # bird.fly()
    # bird.make_sound()



if __name__ == '__main__':
    main()