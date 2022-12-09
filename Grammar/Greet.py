name = 'aaa'

print('こんにちは')
print(f"Your name is {name}, right? \n Please answer with 'yes' or 'no'.")

#以下のように記述することで、変数の型を指定することができる
call: str = input()

if call == "yes":
    print(f"{name}, Nice to meet you.")
elif call == "no":
    print("Sorry, please tell me your name again.")
else:
    print("Please answer with 'yes' or 'no'.")
