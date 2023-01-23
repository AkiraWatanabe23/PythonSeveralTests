'''ユークリッドの互除法'''
#2つの自然数a, bにおいて、aをbで割った商をq、余りをrとしたとき、
#「aとbの最大公約数」は「bとrの最大公約数」に等しい

def gcd(num1, num2):
    '''GreatestCommonDivisor(最大公約数)'''
    if num1 >= num2:
        while num2 != 0:
            num1 = num2
            num2 %= num1
        return num1
    else:
        while num1 != 0:
            num2 = num1
            num1 %= num2
        return num2

a, b = map(int, input("自然数を2つ入力してください \n").split())
print(gcd(a, b))
