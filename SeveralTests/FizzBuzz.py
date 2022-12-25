#FizzBuzz

def fizzbuzz(n: int):
    if n < 0:
        print("none")
    else:
        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print("Not")
    
    
get = input("自然数を1つ入力してください \n")
num = int(get)

fizzbuzz(num)