#ユークリッドの互除法
#2つの自然数a, bにおいて、aをbで割った商をq、余りをrとしたとき、
#「aとbの最大公約数」は「bとrの最大公約数」に等しい

def gcd(n, m): # GreatestCommonDivisor(最大公約数)
    
    if n >= m:
        while m != 0:
            n = m
            m %= n
        return n
    elif n < m:
        while n != 0:
            m = n
            n %= m
        return m

get = input("自然数を2つ入力してください \n")
nums = list(map(int, get.split()))

print(gcd(nums[0], nums[1]))