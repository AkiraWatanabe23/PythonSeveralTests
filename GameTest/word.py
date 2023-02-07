'''wordleテスト'''
from random import choice

#単語リスト(開始時にこの中からランダムに選ぶ)
words = ["above", "adult", "adapt", "brave", "build",
         "crime", "drive", "entry", "empty", "giant",
         "point", "snake", "unity", "slime", "false",
         "earth", "mouse", "horse", "smart", "clean",
         "shift", "space", "enter", "sweat", "berry"]

def check(ans) -> bool:
    '''入力が答えと合っているか判定'''
    li_ans = list(ans)
    checking = []
    correct = 0

    get = list(input("5字の英単語を入力してください"))
    #判定処理
    for i in range(5):
        if get[i] in ans:
            if get[i] == li_ans[i]:
                correct += 1
                checking.append('o')
            else:
                checking.append('△')
        else:
            checking.append(' ')

    #合っていたらクリア
    if correct == 5:
        print("Clear!!")
        return True

    #合っていなかったら現状を出力
    print(checking)
    return False

if __name__ == '__main__':
    answer = choice(words)

    while True:
        check(answer)
