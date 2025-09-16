from util.score import score_string

strings = open('data/4.txt', 'r').read().split()

max_scores = []
for i in range(len(strings)):
    max_score = 0
    max_score_byte = 0
    decrypted_string = ""

    encrypted_bytes = bytes.fromhex(strings[i])

    for byte in range(256):
        decryption_guess = b""
        for enc_byte in encrypted_bytes:
            decryption_guess += (byte ^ enc_byte).to_bytes(1,'big')

        score = score_string(decryption_guess.decode(errors='ignore'))

        if score > max_score:
            max_score = score
            max_score_byte = byte
            decrypted_string = decryption_guess.decode(errors='ignore')
    
    max_scores.append((decrypted_string, max_score, max_score_byte, i))


decrypted_string, _, max_score_byte, ind = max(max_scores, key=lambda p:p[1])
print("The encrypted message was", strings[i], "at line", i+1)
print("The key was", hex(max_score_byte))
print("The decrypted message is", decrypted_string)

