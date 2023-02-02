'''データの読み取り'''
files = {'イチゴ':'strawberry.txt', 'オレンジ':'orange.txt', 'ブドウ':'grape.txt'}

data = {}

for i in files:
    name = files[i]
    file = open(name, 'r')

    data[i] = file.read()
    file.close()

for out in data:
    print(f"[{out}]")
    print(data[out])
    print()
