#ライブラリ「math」
import math

get = input("数字を入力してください \n")

num: int = int(get)

#log(a, b) [return float] ... bを底としたaの対数
#もし第二引数を省略した場合、ネイピア数eを底としたaの対数が返される
print(math.log(num, 2))