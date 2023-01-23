'''フィボナッチ数列'''

def fibonacci(num: int) -> int:
    '''指定されたインデックスの値を返す'''
    if num >= 0:
        if num == 0:
            return 0
        elif num == 1 or num == 2:
            return 1
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)
    else:
        pass

get = input("フィボナッチ数列のインデックスを指定してください \n")
index = int(get)

print(f"フィボナッチ数列の {index} 番目の数は {fibonacci(index)} です")
