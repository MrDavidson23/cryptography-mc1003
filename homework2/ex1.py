def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

ct = bytes.fromhex("3b30cf656ed9fe4df54e08bc57e8f247c654977b7decfa9f2c171b")
m  = b"Trust Charlie"
m2 = b"Trust Mallory"

ct2 = xor(ct[:13], xor(m, m2)) + ct[13:]
print(ct2.hex())
