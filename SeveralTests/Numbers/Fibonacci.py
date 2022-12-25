#フィボナッチ数列

def fibonacci(n: int) -> int:
    if n > 0:
        if n == 1 or n == 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        pass

get = input("フィボナッチ数列のインデックスを指定してください \n")
index = int(get)

print(f"フィボナッチ数列の {index} 番目の数は {fibonacci(index)} です")