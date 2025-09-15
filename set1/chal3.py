from util.score import score_string

encoded_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
encrypted_bytes = bytes.fromhex(encoded_string)

max_score = 0
max_score_byte = 0
decrypted_string = ""

for byte in range(256):
    decryption_guess = b""
    for enc_byte in encrypted_bytes:
        decryption_guess += (byte ^ enc_byte).to_bytes(1,'big')

    score = score_string(decryption_guess.decode(errors='ignore'))

    if score > max_score:
        max_score = score
        max_score_byte = byte
        decrypted_string = decryption_guess.decode(errors='ignore')

print("The key is", hex(max_score_byte))
print("The decrypted message is", decrypted_string)    

    