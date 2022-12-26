#ユークリッドの互除法
#2つの自然数a, bにおいて、aをbで割った商をq、余りをrとしたとき、
#「aとbの最大公約数」は「bとrの最大公約数」に等しい

def gcd(n, m):
    while m != 0:
        n = m
        m %= n
        
    return n

print(gcd(100, 30))