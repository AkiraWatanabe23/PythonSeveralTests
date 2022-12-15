#色々思いついたことをテストしてみる
import random

class Check:
    order: int = 0
    num: int = 0

    def __init__(self, num: int):
        self.num = num
        self.order = random.randint(1, 100)

def main():
    instance: Check = Check(num=0)
    instance.num = input()
    
    if instance.num == instance.order:
        print("Congratulations!!")
    else:
        print(f"random number is {instance.order}")

if __name__ == "__main__":
    main()