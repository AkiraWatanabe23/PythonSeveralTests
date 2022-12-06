#pythonの特殊メソッド各種について記述
#https://blog.codecamp.jp/python-class-code

class Test:
    #「__init__」pythonにおけるコンストラクタ(データの初期化)
    #インスタンスを生成した時に実行される関数
    #「None」...この関数の戻り値の型(Noneの場合、戻り値なし)
    def __init__(self, name) -> None:
        self.name = name

    #「__eq__」条件分岐などで、「==」を利用した時に呼び出される
    #return bool...2つのオブジェクトを比較し、同じならTrue, 違ったらFalseを返す
    def __eq__(self, sample) -> bool:
        return self.name == sample

    def out_put(self):
        print(self.name)

########## 以下は実行処理 ##########
instance = Test("aaa")
eq_test = Test("aaa")
eq_test2 = Test("bbb")

instance.out_put() # -> aaa
print(instance == eq_test)  # -> True
print(instance == eq_test2) # -> False


#計算関連の特殊メソッド
class Calculation:
    #return None の場合、「 -> None」は記述しなくてもよい
    def __init__(self, value):
        self.value = value

    #「__add__」足し算(addition)を行う際の演算子「+」を利用した時に呼び出される
    #return ...2つの値を足した値を返す(同じ型ならOK)
    def __add__(self, ad):
        return self.value + ad.value

    #「__sub__」引き算(subtraction)を行う際の演算子「-」を利用した時に呼び出される
    #return ...「self.value」から「su.value」を引いた値を返す(同じ型ならOK)
    def __sub__(self, su):
        return self.value - su.value

    #「__mul__」掛け算(multiplication)を行う際の演算子「*」を利用した時に呼び出される
    #return ...2つの値を掛けた値を返す(同じ型ならOK)
    def __mul__(self, mu):
        return self.value * mu.value

    #「__truediv__」割り算(division)を行う際の演算子「/」を利用した時に呼び出される
    #return ...「self.value」を「tr.value」で割った値を返す(同じ型ならOK)
    def __truediv__(self, tr):
        return self.value / tr.value

    #「__truediv__」割り算(division)を行う際の演算子「//」を利用した時に呼び出される
    #return ...「self.value」を「tr.value」で割って、切り捨てた値を返す(同じ型ならOK)
    def __floordiv__(self, fl):
        return self.value // fl.value

x = Calculation(100.5)
y = Calculation(20.0)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)