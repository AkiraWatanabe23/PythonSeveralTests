'''データの読み取り'''
files = {'イチゴ':'strawberry.txt', 'オレンジ':'orange.txt', 'ブドウ':'grape.txt'}

data = {}

for k, v in files.items():
    # name = files.items()
    # file = open(str(name), 'r', encoding='UTF-8')

    # data[i] = file.read()
    # file.close()
    try:
        with open(str(v), 'r', encoding='UTF-8') as file:
            data[k] = file.read()
    except FileNotFoundError:
        print("指定したファイルが見つかりませんでした")


for out in data:
    print(f"[{out}]")
    print(data.items())
    print()
