import base64, re, string
from collections import Counter

# English letter frequencies (a-z) + space
ENG = {'a':8.55,'b':1.60,'c':3.16,'d':3.87,'e':12.10,'f':2.18,'g':2.09,'h':4.96,'i':7.33,
       'j':0.22,'k':0.81,'l':4.21,'m':2.53,'n':7.17,'o':7.47,'p':2.07 ,'q':0.10,'r':6.33,
       's':6.73 ,'t':8.94,'u':2.68,'v':1.06,'w':1.83,'x':0.19,'y':1.72,'z':0.11}
SPACE = 13.0
total = sum(ENG.values()) + SPACE
EXPECTED = {k: v/total for k, v in ENG.items()}
EXPECTED[' '] = SPACE/total

def xor_single(data, key):
    return bytes(b ^ key for b in data)

def score(text: bytes) -> float:
    """Chi-squared style statistical distance to English (lower = more English)."""
    n = len(text)
    counts = Counter()
    other = 0
    for b in text:
        c = chr(b).lower()
        if c in EXPECTED: counts[c] += 1
        elif chr(b) in string.printable: other += 1
        else: other += 50
    d = 0.0
    for c, p in EXPECTED.items():
        e = p * n
        d += (counts[c] - e) ** 2 / e
    return d + other * 5

def break_single_xor(ct):
    cands = [(score(xor_single(ct, k)), k) for k in range(1, 256)]
    cands.sort()
    return cands[0][1], xor_single(ct, cands[0][1])

# ---------- Exercise 2 helpers ----------
def b64_to_bytes(s):
    s = re.sub(r'\s+', '', s)
    return base64.b64decode(s + '=' * (-len(s) % 4))

def chunks(data, n):
    return [data[i:i+n] for i in range(0, len(data), n)]

def hamming(a, b):
    return sum(bin(x ^ y).count('1') for x, y in zip(a, b))

def keylen_score(ct, n):
    cs = chunks(ct, n)
    if cs and len(cs[-1]) < n: cs = cs[:-1]
    ds = [hamming(cs[i], cs[j]) / n for i in range(len(cs)) for j in range(i+1, len(cs))]
    return sum(ds) / len(ds)

def best_keylen(ct, maxn=40):
    sc = sorted((keylen_score(ct, n), n) for n in range(2, maxn+1))
    return sc[0][1], sc[:6]

def split_streams(ct, n):
    return [ct[i::n] for i in range(n)]

def break_vigenere(ct):
    n, top = best_keylen(ct)
    print("best key lengths:", [(round(s,3), k) for s, k in top])
    key = bytes(break_single_xor(s)[0] for s in split_streams(ct, n))
    pt = bytes(c ^ key[i % n] for i, c in enumerate(ct))
    return key, pt

ct1 = b64_to_bytes(open('ct1.txt').read())
k, pt = break_single_xor(ct1)
print("== Ex1 ==\nkey = %d (0x%02x)\n%s\n" % (k, k, pt.decode(errors='replace')))
ct2 = b64_to_bytes(open('ct2.txt').read())
key, pt = break_vigenere(ct2)
print("== Ex2 ==\nkey = %r (hex %s)\n%s" % (key, key.hex(), pt.decode(errors='replace')))