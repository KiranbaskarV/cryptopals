from util.xor import break_single_byte_xor

encoded_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
encrypted_bytes = bytes.fromhex(encoded_string)

key_byte, plaintext, score = break_single_byte_xor(encrypted_bytes)

print("The key is", hex(key_byte))
print("The decrypted message is", plaintext)