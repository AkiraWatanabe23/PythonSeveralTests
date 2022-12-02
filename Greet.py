print('こんにちは')
print("あなたの名前を教えてください")

name = input()
print(f"あなたの名前は{name}ですか?\n はい か いいえ で答えてください")

call: str = input()

if call is "はい":
    print(f"{name}さん、よろしくお願いします")
elif call is "いいえ":
    print("もう一度名前を教えてください")
