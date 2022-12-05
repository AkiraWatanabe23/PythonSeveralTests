#Pythonの「self」について記述
#https://www.sejuku.net/blog/64106
#https://prograshi.com/language/python/py-self-in-class/

class TestFirst():
    def method(self):
        print("Hello!!")

instance = TestFirst()
instance.method()
"""
実行結果 -> Hello!!
"""
#self ... インスタンス自身を示すもの
"""
もし、class内で定義したメソッドに引数を1つも渡さなかった場合(使う、使わないに関わらず)
「TypeError: クラス名.メソッド名() takes 0 positional arguments but 1 was given」
(メソッドには1つの引数が必須ですが、0個しか渡されていません)というエラーが出る

why?
pythonでは、クラスをインスタンスとしてから中のdefで定義した関数を呼び出す場合、
「関数(function)」としてではなく、「メソッド(method)」として呼び出す
この時、メソッドにはインスタンス自身を引数として渡さなければいけない設定になっているため、
インスタンス自身が入る引数を渡す必要があるため
このインスタンス自身を入れる引数に習慣として「self」が使われる
"""

#使い方 1 :インスタンス変数として参照する
class TestSecond():
    def __init__(self, strA, strB):
        self.strA = strA
        self.strB = strB

test = TestSecond("Good", "Morning!")
print(test.strA)
print(test.strB)
"""
実行結果 -> Good (\n) Morning!
"""

#上記のようにインスタンス(今回は「test」)を生成する時に引数を渡すことで、
#selfを使ってインスタンス変数として代入することができる
#※呼び出す側は引数として値を入れない

#使い方 2 :クラス変数として参照する
#以下のように、クラス変数として別のメソッドで使うことができる
class TestThird():
    def __init__(self, strA, strB):
        self.strA = strA
        self.strB = strB

    def output(self):
        print(self.strA)
        print(self.strB)

test = TestThird("Good", "Afternoon...")
test.output()
"""
実行結果 -> Good (\n) Afternoon...
"""

#使い方 3 :クラス継承に使う
#selfはクラス変数として参照できるため、クラスを継承した時にも参照することができる
class Forth():
    def __init__(self):
        self.strA = "Hello World!"

class Fifth(Forth):
    def output(self):
        print(self.strA)

test = Fifth()
test.output()
"""
実行結果 -> Hello World!
"""

#注意点↓
class Warns():
    strA = "Hello python"
    def __init__(self):
        print(f"1: {self.strA}")
        self.strA = "Hello World!"
        print(f"2: {self.strA}")
        strA = "Hello python"
        print(f"3: {self.strA}")

test = Warns()
"""
実行結果 -> 1: Hello Python (\n) 2: Hello World! (\n) 3: Hello World!
"""

#1 ... self.strA == クラス変数「strA」であるため、OK
#2 ... self.strAがインスタンス変数として扱われ、代入されているので、OK
#3 ... pythonの仕様として、クラス変数もインスタンス変数も「self.変数名」の形で参照できるが、
"""
クラス変数にもインスタンス変数にも値がある場合、インスタンス変数を優先して参照する
(3 の場合は、コンストラクタ内でstrA(クラス変数)を"Hello python"に変更し、出力しようとしたが
 この時点でクラス変数「strA」とインスタンス変数「self.strA」の両方に値が存在するため、インスタンス変数「self.strA」が優先して出力される)
"""