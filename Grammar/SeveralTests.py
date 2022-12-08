#色々テストしたいことをここでやる

##############################
#インスタンス化の注意点
#https://python.ms/class/
class Animal:
    #クラス変数
    att = "dog"
    name = None

    def honk(self):
        print('bowwow')

    def bark(self):
        print('woof')

instance = Animal() #インスタンス化
instance.honk() # -> bowwow
instance.bark() # -> woof

instance.name = "cat" #インスタンス化した変数からクラス変数を参照している(Animalクラスのnameの値は変更されない)
print(Animal.name) # -> None
Animal.name = "pig" #Animalクラスのクラス変数「name」を直接参照している(Animalクラスのnameの値が変更されている)
print(instance.name) # -> cat
print(Animal.name) # -> pig

"""
※注意事項

instance = Animal
instance.honk()
instance.bark()
と記述した場合、実行時にエラーが発生する
(この時、コードを記述した時点ではエラーを起こさないため、注意!!)
エラーメッセージ↓
TypeError: Animal.honk() missing 1 required positional argument: 'self'
(honk()に必要な引数「self」がありません)
"""
##############################

##############################
#引数の参照渡し、値渡しについて
#https://www.javadrive.jp/python/userfunc/index3.html

#値渡し...関数を呼び出す時に、仮引数に指定した値を「コピーして実引数に渡す」方式
#　　　   関数内で変数の値を変更しても、呼び出し元が参照している変数の値は変更されない
#参照渡し...関数を呼び出す時に、仮引数に指定した値が「保管されている場所の情報を実引数に渡す」方式
#　　　　   関数内で変数の値を変更した場合、呼び出し元が参照している変数の値も変更される
"""
pythonでは、引数を指定して関数を呼び出す時は、「参照渡し」が使用される

※str, int 等の一度作成すると変更できないイミュータブル(immutable)なオブジェクトを
引数に指定した場合と、
List, Dic 等の作成後に変更できるミュータブル(mutable)なオブジェクトを
引数に指定した場合とで挙動が異なる
"""

#変更できないイミュータブル(immutable)なオブジェクトを引数に指定した場合
def func_one(n):
    print(id(n)) #nに代入されたオブジェクトのIDを出力

def pass_by_value_like(n):
    print(n)
    n += 5 # <- 値の変更
    print(n)

a = 10
print(id(a)) # -> 140722845111368
func_one(a)  # -> 140722845111368
#↑同じオブジェクトを参照している

print(a)    # -> 10
pass_by_value_like(a) # -> 10
#             -> 15
print(a)    # -> 10 ... 呼び出し元の変数の値に変更がない
#上記のように、参照渡しでも値渡しのような挙動になる


#変更できるミュータブル(mutable)なオブジェクトを引数に指定した場合
def func_two(n):
    print(id(n))

def pass_by_refarence(n):
    print(n)
    n[0] += 5
    print(n)

a = [10, 20]
print(id(a)) # -> 2787859597696
func_two(a)  # -> 2787859597696
#↑同じオブジェクトを参照している

print(a)             # -> [10, 20]
pass_by_refarence(a) # -> [10, 20]
#                      -> [15, 20]
print(a)             # -> [15, 20] ... 呼び出し元の変数の値が変更されている
#上記のように、参照渡しの挙動をする
##############################