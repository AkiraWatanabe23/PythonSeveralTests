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
        # with open(str(v), mode='a', encoding='UTF-8') as f:
        #     data[k] = f.write("\n追記")
    except FileNotFoundError:
        print("指定したファイルが見つかりませんでした")

for k in data.items():
    print(f"[{k}]")
    print(data[k])
    print()
