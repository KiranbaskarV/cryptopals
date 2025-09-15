def fixed_xor(buf1, buf2):
    assert(len(buf1) == len(buf2))

    return bytes(a ^ b for a,b in zip(bytes.fromhex(buf1), bytes.fromhex(buf2))).hex()

buf1 = "1c0111001f010100061a024b53535009181c"
buf2 = "686974207468652062756c6c277320657965"

ans = "746865206b696420646f6e277420706c6179"

if fixed_xor(buf1, buf2) == ans:
    print("Passed")
else:
    print("Failed")