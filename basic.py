from operator import mul
from functools import reduce
# from collections import Counter
# from collections import deque
# from itertools import combinations as comb
# from itertools import permutations as perm
# from copy import copy
# 配列二分法アルゴリズム
# https://docs.python.jp/3/library/bisect.html
# import bisect
# 桁数指定
# print('{:.3f}'.format(X))
# from collections import defaultdict
# dic = defaultdict(lambda: ...)
# 値で辞書をソート
# sorted(dic.items(), key=lambda x:x[1])
# ヒープキュー
# https://docs.python.org/ja/3/library/heapq.html
# import heapq
# 正規表現(regular expression)のためのモジュール
# import re
# import functools
# functools.lru_cache(maxsize=None) メモ化再帰をするときに呼び出し結果を覚えておく。
# 文字列操作
# import string
# 英小文字
# string.ascii_lowercase
# 英大文字
# string.ascii_uppercase

import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**6)

# alphabet
list(__import__('string').ascii_lowercase)


def inpl():
    return list(map(int, input().split()))


# 重複組み合わせは nHr = (n + r - 1)Cn
def cmb(n, r):
    # combination
    if n < r:
        return 0
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def gcd(a, b):
    # greatest common divisor
    while b > 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    # least common multiple
    return a * b // gcd(a, b)


# 互いに素なx, yについて、a * x + b * y = 1の解の一つを求める。
# 参考：http://www.tbasic.org/reference/old/ExEuclid.html
def extGCD(x, y):
    r = [1, 0, x]
    w = [0, 1, y]

    while w[2] != 1:
        q = r[2] // w[2]
        w_tmp = [r[0] - q * w[0], r[1] - q * w[1], r[2] % w[2]]
        r, w = w, w_tmp

    return w[:2]


# 階乗の逆元は(x!)^(-1) * x=((x-1)!)^(-1)を利用する。
# 1 / a mod m を求める。
def mod_inv(a, m):
    x, _ = extGCD(a, m)
    return (x + m) % m


# nの素因数を辞書形式で求める。
def factor(n):
    ret = {}
    p = 2
    root_n = int(n**0.5)
    while n > 1:
        if n % p == 0:
            n //= p
            ret[p] = ret.get(p, 0) + 1
        elif p <= root_n:
            p += 1
        else:
            p = n
    return ret
