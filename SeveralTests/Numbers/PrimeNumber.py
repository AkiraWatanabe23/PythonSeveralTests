#素数判定(入力値が素数かどうか判定する)
#素数...1とその数以外に正の約数を持たない自然数
import math

def prime(num: int) -> bool:
    '''素数判定を行う関数'''
    #2未満の数(2未満の数は、素数の定義から外れるためFalse)
    if num < 2:
        return False
    #2は素数
    elif num == 2:
        return True
    #4以上の偶数(必ず2を約数に持つためFalse)
    elif num % 2 == 0 and num >= 4:
        return False
    #それ以外(調べないと分からない)
    else:
        root = math.sqrt(num)
        #2～入力値の平方根まで順に割っていき、割り切れたら素数ではない(その数が約数になる)
        for i in range(2, int(root)+1):
            if num % i == 0:
                return False
        #割り切れなかったら素数(約数が1とその数以外にない)
        return True


n = int(input("整数を1つ入力してください \n"))
print(f"{n} は素数です" if prime(n) else f"{n} は素数ではありません")
