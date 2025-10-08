from util.xor import break_single_byte_xor

with open('data/4.txt', 'r') as f:
    strings = f.read().split()

results = []
for i, hex_string in enumerate(strings):
    encrypted_bytes = bytes.fromhex(hex_string)
    key_byte, plaintext, score = break_single_byte_xor(encrypted_bytes)
    results.append((plaintext, score, key_byte, i))

plaintext, _, key_byte, line_num = max(results, key=lambda p: p[1])

print("The encrypted message was", strings[line_num], "at line", line_num + 1)
print("The key was", hex(key_byte))
print("The decrypted message is", plaintext)