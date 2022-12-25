#色々思いついたことをテストしてみる
import random

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