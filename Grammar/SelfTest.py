#Python「self」について記述
#https://www.sejuku.net/blog/64106
#https://prograshi.com/language/python/py-self-in-class/

class SelfBase():
    def method(self):
        print("Hello!!")

instance = SelfBase()
instance.method() # -> Hello!!
"""
self ... インスタンス自身を示すもの

もし、class内で定義したメソッドに引数を1つも渡さなかった場合(使う、使わないに関わらず)
「TypeError: クラス名.メソッド名() takes 0 positional arguments but 1 was given」
(メソッドには1つの引数が必須ですが、0個しか渡されていません)というエラーが出る

why?
pythonでは、クラスをインスタンスとしてから中のdefで定義した関数を呼び出す場合、
「関数(function)」としてではなく、「メソッド(method)」として呼び出す
この時、メソッドにはインスタンス自身を引数として渡さなければいけない設定になっているため、
インスタンス自身が入る引数を渡す必要がある
このインスタンス自身を入れる引数に習慣として「self」が使われる
"""

#使い方 1 :インスタンス変数として参照する
class Instance():
    def __init__(self, strA, strB):
        self.strA = strA
        self.strB = strB

test = Instance("Good", "Morning!") #ここでインスタンス化している(インスタンス変数)
print(test.strA) # -> Good
print(test.strB) # -> Morning!
"""
上記のようにインスタンス(今回は「test」)を生成する時に引数を渡すことで、
selfを使ってインスタンス変数として代入することができる
※呼び出す側は(selfにあたる部分には)引数として値を入れない
"""

#使い方 2 :クラス変数として参照する
#以下のように、クラス変数として別のメソッドで使うことができる
class ClassVariable():
    name = 'Name'

    def __init__(self, strA, strB):
        self.strA = strA
        self.strB = strB

    def output(self):
        print(self.strA)
        print(self.strB)

test = ClassVariable("Good", "Afternoon...") #インスタンス化
#クラス内の関数を呼び出す
test.output() # -> Good (\n) Afternoon...
#クラス変数を出力する
print(test.name) # -> Name

#使い方 3 :クラス継承に使う
#selfはクラス変数として参照できるため、クラスを継承した時にも参照することができる
class TestBase():
    def __init__(self):
        self.strA = "Hello World!"

#↓クラス定義時に、()内にクラス名を記述することで継承することができる
class Inheritance(TestBase):
    def output(self):
        print(self.strA)

test = Inheritance()
test.output() # -> Hello World!

#注意点↓
class Warns():
    strA = "Hello python"

    def __init__(self):
        print(f"1: {self.strA}") # -> 1: Hello Python
        self.strA = "Hello World!"
        print(f"2: {self.strA}") # -> 2: Hello World!
        strA = "Hello everyone"
        print(f"3: {self.strA}") # -> 3: Hello World!

test = Warns()
"""
1 ... self.strA はクラス変数「strA」を参照している
2 ... self.strA がインスタンス変数として扱われ、代入されている (l.80)
3 ... python の仕様として、「self.変数名」の形でクラス変数もインスタンス変数も参照できるが、

同じ名前のクラス変数とインスタンス変数があり、両方に値がある場合、インスタンス変数を優先して参照する
(3 の場合は、コンストラクタ内でstrA(クラス変数)を"Hello everyone"に変更し、出力しようとしたが
 この時点でクラス変数「strA」とインスタンス変数「self.strA」の両方に値が存在するため、
 インスタンス変数「self.strA」("Hello World!")が優先して出力される)
"""