#色々思いついたことをテストしてみる
import random
import copy

#じゃんけん
#グー：0, チョキ：1, パー：2
def judge(x, y):
    result: str

    if (x - y) % 3 == 0:
        result = "あいこ"
    elif (x - y) % 3 == 1:
        result = "負け"
    elif (x - y) % 3 == 2:
        result = "勝ち"
    print(result)

hands: list[str] = ["グー", "チョキ", "パー"]

get = input("手を選んでください\n 0 : グー, 1 : チョキ, 2 : パー \n")

player = int(get)
vs: int = random.randint(0, 2)

print("\nあなたの手 : {}".format(hands[player]))
print("コンピュータの手 : {}\n".format(hands[vs]))

judge(player, vs)

#copy関数について
#「copy, deepcopy」...List等の変更可能なオブジェクトを「値渡し」で参照したい場合に使うもの
li = [0, 1, [2, 3]]
li_assign = li                   # assignment
li_copy = li.copy()              # shallow copy
li_deepcopy = copy.deepcopy(li)  # deep copy

li[1] = 100
li[2][0] = 200

#実行結果には、以下のような違いがある
print(li)          # -> [0, 100, [200, 3]]
print(li_assign)   # -> [0, 100, [200, 3]]
print(li_copy)     # -> [0, 1, [200, 3]]
print(li_deepcopy) # -> [0, 1, [2, 3]]