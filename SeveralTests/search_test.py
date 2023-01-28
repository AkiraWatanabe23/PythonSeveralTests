'''モジュール「os」'''
import os

#listdir ... あるフォルダ内のファイルやフォルダの一覧を取得する関数
#以下の記述だと、ルートディレクトリにあるディレクトリの一覧を取得できる(return list)
data = os.listdir('/')

#ルートディレクトリ内のディレクトリやファイルが存在するかを判定
for i in data:
    print(i, end=" ")
    print(os.access(i, os.F_OK))

#↓一覧から「book」という名前のディレクトリを探すプログラム
def search_for_depth(get_dir, name):
    '''1, 深さ優先探索'''
    for j in os.listdir(get_dir):

        if j == name:
            print(get_dir + j)

        if os.path.isdir(get_dir + j):
            if os.access(get_dir + j, os.R_OK):
                search_for_depth(get_dir + j + '/', name)
search_for_depth('/', 'book')

#2, 幅優先探索
queue = ['/']

while len(queue) > 0:
    get = queue.pop()

    for i in os.listdir(get):
        if i == 'book':
            print(get + '/')

        if os.path.isdir(get + i):
            if os.access(get + i, os.R_OK):
                queue.append(get + i + '/')
