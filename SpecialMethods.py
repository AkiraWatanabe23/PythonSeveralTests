#pythonの特殊メソッド各種について記述

class Test:
    #「__init__」pythonにおけるコンストラクタ
    #インスタンスを生成した時に実行される関数
    def __init__(self, name) -> None:
        self.name = name

    def out_put(self):
        print(self.name, end="")

instance = Test("aaa")
print(f"Your name is {instance.out_put()}, right?")