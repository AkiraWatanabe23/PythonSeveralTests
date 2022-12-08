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