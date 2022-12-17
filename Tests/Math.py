#ライブラリ「math」
import math

get = input("数字を入力してください \n")

num = int(get)

#log(a, b) [return float] ... bを底としたaの対数(対数関数)
#もし第二引数を省略した場合、ネイピア数eを底としたaの対数が返される
print(math.log(num, 2))

#exp(a) [return float] ... ネイピア数eのa乗(指数関数)
#※ math.exp(a) != math.e ** a (math.exp(a)の方がより正確な値を返す)
print(math.exp(num))