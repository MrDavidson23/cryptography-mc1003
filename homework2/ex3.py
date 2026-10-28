from itertools import product

def linear_complexity(s):
    n = len(s)
    if all(b == 0 for b in s):
        return 0, None
    for L in range(1, n + 1):
        for c in product([0, 1], repeat=L):
            ok = True
            for i in range(n - L):
                bit = 0
                for j in range(L):
                    bit ^= c[j] & s[i + j]
                if bit != s[i + L]:
                    ok = False
                    break
            if ok:
                return L, c
    return n, None


def xor_seq(a, b):
    return [x ^ y for x, y in zip(a, b)]


# A
s = [0, 1, 0, 1] * 6
t = [1, 0, 1, 0] * 6
sxort = xor_seq(s, t)
print(linear_complexity(s))
print(linear_complexity(t))
print(linear_complexity(sxort))


# B
s = [1] * 24
t = [1, 1, 0] * 8
sxort = xor_seq(s, t)
print(linear_complexity(s))
print(linear_complexity(t))
print(linear_complexity(sxort))


