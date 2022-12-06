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

instance = Test("aaa")
eq_test = Test("aaa")
eq_test2 = Test("bbb")

instance.out_put() # -> aaa
print(instance == eq_test)  # -> True
print(instance == eq_test2) # -> False