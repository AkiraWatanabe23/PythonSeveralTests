#素数判定(入力値が素数かどうか判定する)
#素数...1とその数以外に正の約数を持たない自然数
import math

#素数判定を行う関数
def prime(n: int) -> bool:
    
    #2未満の数(2未満の数は、素数の定義から外れるためFalse)
    if n < 2:
        return False
    #2は素数
    elif n == 2:
        return True
    #4以上の偶数(必ず2を約数に持つためFalse)
    elif n % 2 == 0 and n >= 4:
        return False
    #それ以外(調べないと分からない)
    else:
        root = math.sqrt(n)
        
        #2～入力値の平方根まで順に割っていき、割り切れたら素数ではない(その数が約数になる)
        for i in range(2, int(root)+1):
            if n % i == 0:
                return False
        #割り切れなかったら素数(約数が1とその数以外にない)
        return True


get = input("整数を1つ入力してください \n")
num = int(get)

if prime(num):
    print(f"{num} は素数です")
else:
    print(f"{num} は素数ではありません")