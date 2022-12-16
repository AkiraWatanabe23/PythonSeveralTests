#素数判定(入力値が素数かどうか判定する)

def prime(n: int) -> bool:
    
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


get = input("数字を1つ入力してください \n")
num = int(get)

if prime(num):
    print(f"{num} は素数です")
else:
    print(f"{num} は素数ではありません")
#現時点では正確な答えが出るが、ループ文に問題がある気がする