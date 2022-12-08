#デコレーター関数...関数を修飾し、新しい関数を作成するもの(関数に付加機能を付けられる)
#　　　　　　　　   複数の関数に対して同じ機能を付けたい時に使う
#https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e

#以下でデコレーター関数を定義(デコレーター関数内で関数を定義して使用する)
def decorate(func_base): # <- func_base には、デコレートする関数(今回は「func()」)が引数に入る
    def in_decolate():
        print('check')
        func_base() # <- ここでデコレートする関数の処理を実行する
    return in_decolate

#デコレーターを指定
@decorate
def func():
    print('decorate')

func() # -> check (\n) decorate