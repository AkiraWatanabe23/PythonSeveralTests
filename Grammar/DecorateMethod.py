#関数デコレータ...関数を修飾し、新しい関数を作成するもの(関数に付加機能を付けられる)
#　　　　　　　　 複数の関数に対して同じ機能を付けたい時に使う
#https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e
#https://zenn.dev/ryo_kawamata/articles/learn_decorator_in_python

#以下のように関数デコレータを定義(関数デコレータ内で関数を定義する)
#ex.1)
def decorator(func_base): # <- 引数には、デコレートする関数(今回は「func()」)が入る
    def in_decolate():
        print('check')
        func_base() # <- ここでデコレートする関数[func()]の処理を実行する
    return in_decolate # <- 処理を実行した後に関数を返す

#↓ @decorator...「decorator」という関数デコレータ内で
# 下記の関数(「func()」)をデコレート(装飾)する、という意味
@decorator
def func():
    print('decorate')

@decorator
def func_test():
    print("test")

func()      # -> check (\n) decorate
func_test() # -> check (\n) test

#ex.2)引数を受け取る関数デコレータ
#def base(): ... デコレータの引数を受け取る
def base(get): # <- get...関数デコレータの引数(「@...」の時に設定する)

    #def child(): ... デコレートする関数を受け取る
    def child(func): # <- func...デコレートする関数

        #def wrap(): ... 実際の処理を記述する
        def wrap(*args, **kwargs): # <- ここには、「func()」の引数が入る
            
            x = func(*args, **kwargs)
            return f"<{get}> {x} </{get}>" # <- wrap()のreturn

        return wrap # <- child()のreturn

    return child # <- base()のreturn

@base("h")
def greet():
    return 'Hello World'

print(greet()) # -> <h> Hello World </h>