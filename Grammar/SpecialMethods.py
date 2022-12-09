#pythonの特殊メソッド各種について記述
#https://blog.codecamp.jp/python-class-code

#コンストラクタ
class Test:
    #「__init__」pythonにおけるコンストラクタ(データの初期化)
    #インスタンスを生成した時に実行される関数
    #「None」...この関数の戻り値の型(Noneの場合、戻り値なし)
    def __init__(self, name) -> None:
        self.name = name

    def output(self):
        print(self.name)

instance = Test("aaa")
instance.output() # -> aaa


#四則演算(「+」「-」「*」「/」「//」)
class FourArithmetic:
    #return None の場合や、
    #複数の種類の型が返ってくることが考えられる(int の時も float の時もある)ような場合、「 -> xxx」は記述しなくてよい
    def __init__(self, value):
        self.value = value

    def __add__(self, ad): #足し算(addition)
        return self.value + ad.value

    def __sub__(self, su): #引き算(subtraction)
        return self.value - su.value

    def __mul__(self, mu): #掛け算(multiplication)
        return self.value * mu.value

    def __truediv__(self, tr): #割り算(division)
        return self.value / tr.value

    def __floordiv__(self, fl): #割り算(division) ※切り捨て
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

    #「__eq__」条件分岐などで、「==」(Equal)を利用した時に呼び出される(return bool)
    def __eq__(self, sample) -> bool:
        return self.value == sample

    #「__ne__」条件分岐などで、「!=」(Not Equal)を利用した時に呼び出される(return bool)
    def __ne__(self, ne) -> bool:
        return self.value != ne

x = Compares(100)
y = Compares('100')
z = Compares(100)

print(x == y) # -> False
print(x == z) # -> True