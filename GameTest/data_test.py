'''データの読み取り'''
files = {'イチゴ':'strawberry.txt', 'オレンジ':'orange.txt', 'ブドウ':'grape.txt'}

data = {}

for k, v in files.items():
    # name = files[k]
    # file = open(str(name), 'r', encoding='UTF-8')

    # data[k] = file.read()
    # file.close()
    try:
        with open(str(v), 'r', encoding='UTF-8') as f:
            data[k] = f.read()
    except FileNotFoundError:
        print("指定したファイルが見つかりませんでした")

    print(f"[{k}]")
    print(f"{data[k]}\n")
