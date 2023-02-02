'''データの読み取り'''
files = {'イチゴ':'strawberry.txt', 'オレンジ':'orange.txt', 'ブドウ':'grape.txt'}

data = {}

for i in files:
    # name = files.items()
    # file = open(str(name), 'r', encoding='UTF-8')

    # data[i] = file.read()
    # file.close()
    name = files.items()
    with open(str(name), 'r', encoding='UTF-8') as file:
        data[i] = file.read()

for out in data:
    print(f"[{out}]")
    print(data.items())
    print()
