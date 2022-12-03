#Pythonの「self」について記述
#https://www.sejuku.net/blog/64106

class testFirst():
    def method(self):
        print("Hello!!")

instance = testFirst()
instance.method()
#実行結果 -> Hello!!

#self ... インスタンス自身を示すもの
#使い方 1 :インスタンス変数として参照する
class testSecond():
    def __init__(self, strA, strB):
        self.strA = strA
        self.strB = strB

test = testSecond("Good", "Morning!")
print(test.strA)
print(test.strB)
#　　　 2 :クラス変数として参照する
#　　　 3 :クラス継承に使う