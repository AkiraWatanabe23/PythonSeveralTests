#pythonの特殊メソッド各種について記述
#https://blog.codecamp.jp/python-class-code

#コンストラクタ
class Test:
    #「__init__」pythonにおけるコンストラクタ(データの初期化)
    #インスタンスを生成した時に実行される関数
    #「None」...この関数の戻り値の型(Noneの場合、戻り値なし)
    def __init__(self, name) -> None:
        self.name = name

    def out_put(self):
        print(self.name)

instance = Test("aaa")
instance.out_put() # -> aaa


#四則演算の特殊メソッド
class FourArithmetic:
    #return None の場合、「 -> None」は記述しなくてもよい
    def __init__(self, value):
        self.value = value

    #「__add__」足し算(addition)を行う際の演算子「+」を利用した時に呼び出される
    #return ...2つの値を足した値を返す
    def __add__(self, ad):
        return self.value + ad.value

    #「__sub__」引き算(subtraction)を行う際の演算子「-」を利用した時に呼び出される
    #return ...「self.value」から「su.value」を引いた値を返す
    def __sub__(self, su):
        return self.value - su.value

    #「__mul__」掛け算(multiplication)を行う際の演算子「*」を利用した時に呼び出される
    #return ...2つの値を掛けた値を返す
    def __mul__(self, mu):
        return self.value * mu.value

    #「__truediv__」割り算(division)を行う際の演算子「/」を利用した時に呼び出される
    #return ...「self.value」を「tr.value」で割った値を返す
    def __truediv__(self, tr):
        return self.value / tr.value

    #「__floordiv__」割り算(division)を行う際の演算子「//」を利用した時に呼び出される
    #return ...「self.value」を「fl.value」で割って、切り捨てた値を返す
    def __floordiv__(self, fl):
        return self.value // fl.value

x = FourArithmetic(100.5)
y = FourArithmetic(20)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)

#「+=」「-=」「*=」「/=」
class Calculation:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, ia):
        self.value += ia
        return self.value

    def __isub__(self, isu):
        self.value -= isu
        return self.value

    def __imul__(self, im):
        self.value *= im
        return self.value

    def __itruediv__(self, it):
        self.value /= it
        return self.value

a = Calculation(50)
print(type(a)) # -> class '__main__.Calculation'
#↑最初の時点で、変数aにはCalculation型が格納されている

a += 5
print(type(a)) # -> class 'int'
#↑この時点で、Calculation型が格納されていた変数aに、int型が格納されている
print(a)
a -= 5
print(a)
a *= 10
print(a)
a /= 5
print(a)

#比較演算子
class Compares:
    def __init__(self, value):
        self.value = value

    #「__eq__」条件分岐などで、「==」(equal)を利用した時に呼び出される
    #return bool...2つのオブジェクトを比較し、同じならTrue, 違ったらFalseを返す
    def __eq__(self, sample) -> bool:
        return self.name == sample

    #「__ne__」条件分岐などで、「!=」(Not Equal)を利用した時に呼び出される
    #return bool...2つのオブジェクトを比較し、同じならFalse, 違ったらTrueを返す
    def __ne__(self, ne) -> bool:
        return self.value != ne