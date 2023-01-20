import os

#listdir ... あるフォルダ内のファイルやフォルダの一覧を取得する関数
#以下の記述だと、ルートディレクトリにあるディレクトリの一覧を取得できる(return list)
data = os.listdir("/")

#↓一覧から「book」という名前のディレクトリを探すプログラム

#1, 深さ優先探索
def search_for_depth(dir, name):
    for i in os.listdir(dir):
        if i == name:
            print(dir + i)
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):
                search_for_depth(dir + i + "/", name)
                
search_for_depth("/", "book")