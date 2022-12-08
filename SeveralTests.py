#色々テストしたいことをここでやる

#https://python.ms/class/

class Animal:
    att = "dog"

    def honk(self):
        print('bowwow')

    def bark(self):
        print('woof')

instance = Animal() #インスタンス化
instance.honk() # -> bowwow
instance.bark() # -> woof

"""
※注意事項

instance = Animal
instance.honk()
instance.bark()
と記述した場合、コンパイル時にエラーが発生する
(この時、コードを記述した時点ではエラーを起こさないため、注意!!)
エラー↓
TypeError: Animal.honk() missing 1 required positional argument: 'self'
(honk()に必要な引数「self」がありません)
"""