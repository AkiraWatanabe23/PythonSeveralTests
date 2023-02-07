'''wordleテスト'''
from random import choice

words = ["above", "adult", "adapt", "brave", "build", "crime", "drive", "entry", "empty", "giant"]

def check(ans) -> bool:
    '''入力が答えと合っているか判定'''
    li_ans = list(ans)
    checking = []
    correct = 0

    get = list(input("5字の英単語を入力してください"))
    for i in range(5):
        if get[i] in ans:
            if get[i] == li_ans[i]:
                correct += 1
                checking.append('o')
            else:
                checking.append('△')
        else:
            checking.append(' ')

    if correct == 5:
        print("Clear!!")
        return True

    print(checking)
    return False

if __name__ == '__main__':
    answer = choice(words)

    while True:
        check(answer)
