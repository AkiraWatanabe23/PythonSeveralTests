'''じゃんけん'''
import random

def judge(pl1, pl2):
    '''グー: 0, チョキ: 1, パー: 2'''
    result: str

    if (pl1 - pl2) % 3 == 0:
        result = "あいこ"
    elif (pl1 - pl2) % 3 == 1:
        result = "負け"
    elif (pl1 - pl2) % 3 == 2:
        result = "勝ち"
    print(result)

hands: list[str] = ["グー", "チョキ", "パー"]

get = input("手を選んでください\n 0 : グー, 1 : チョキ, 2 : パー \n")

player = int(get)
vs: int = random.randint(0, 2)

print(f"あなたの手 : {hands[player]}")
print(f"コンピュータの手 : {hands[vs]}\n")

judge(player, vs)
