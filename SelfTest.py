#Pythonの「self」について記述
#https://www.sejuku.net/blog/64106

class testFirst():
    def method(self):
        print("Hello!!")

instance = testFirst()
instance.method()
"""
実行結果 -> Hello!!
"""


#self ... インスタンス自身を示すもの
#使い方 1 :インスタンス変数として参照する
class testSecond():
    def __init__(self, strA, strB):
        self.strA = strA
        self.strB = strB

test = testSecond("Good", "Morning!")
print(test.strA)
print(test.strB)
"""
実行結果 -> Good
　　　　    Morning!
"""

#上記のようにインスタンス(今回は「test」)を生成する時に引数を渡すことで、
#selfを使ってインスタンス変数として代入することができる
#※呼び出す側は引数として値を入れない

#使い方 2 :クラス変数として参照する
#以下のように、クラス変数として別のメソッドで使うことができる
class testThird():
    def __init__(self, strA, strB):
        self.strA = strA
        self.strB = strB

    def output(self):
        print(self.strA)
        print(self.strB)

test = testThird("Good", "Afternoon...")
test.output()
"""
実行結果 -> Good
　　　　    Afternoon...
"""

#使い方 3 :クラス継承に使う
#selfはクラス変数として参照できるため、クラスを継承した時にも参照することができる
class forth():
    def __init__(self):
        self.strA = "Hello World!"

class fifth(forth):
    def output(self):
        print(self.strA)

test = fifth()
test.output()
"""
実行結果 -> Hello World!
"""

#注意点
class warns():
    strA = "Hello Python"
    def __init__(self):
        print(f"1: {self.strA}")
        self.strA = "Hello World!"
        print(f"2: {self.strA}")
        strA = "Hello Python"
        print(f"3: {self.strA}")

test = warns()
"""
実行結果 -> 1: Hello Python
　　　　　　2: Hello World!
　　　　　　3: Hello World!
"""

#1 ... self.strA == クラス変数「strA」であるため、OK
#2 ... 
#3 ... 