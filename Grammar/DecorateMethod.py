#デコレーター関数...関数を修飾し、新しい関数を作成するもの(関数に付加機能を付けられる)
#　　　　　　　　   複数の関数に対して同じ機能を付けたい時に使う
#https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e

#以下で関数デコレータを定義(関数デコレータ内で関数を定義し、処理を実行した後に関数をreturnする)
#ex.1)引数なし
def decorator(func_base): # <- func_base には、デコレートする関数(今回は「func()」)が引数に入る
    def in_decolate():
        print('check')
        func_base() # <- ここでデコレートする関数[func()]の処理を実行する
    return in_decolate

#デコレーターを指定
#↓「decorator」というデコレーターの定義関数内で
# 以下の関数(「func()」)をデコレート(装飾)する、という意味
@decorator
def func():
    print('decorate')

@decorator
def func_test():
    print("test")

func()      # -> check (\n) decorate
func_test() # -> check (\n) test