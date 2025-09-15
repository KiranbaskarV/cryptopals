# https://web.archive.org/web/20170918020907/http://www.data-compression.com/english.html
letter_scores = {
    'a': 65174,
    'b': 12425,
    'c': 21734,
    'd': 34984,
    'e': 104144,
    'f': 19788,
    'g': 15861,
    'h': 49289,
    'i': 55809,
    'j': 903,
    'k': 5053,
    'l': 33149,
    'm': 20212,
    'n': 56451,
    'o': 59630,
    'p': 13765,
    'q': 861,
    'r': 49756,
    's': 51576,
    't': 72936,
    'u': 22513,
    'v': 8290,
    'w': 17127,
    'x': 1369,
    'y': 14598,
    'z': 784,
    ' ': 191818
}

def score_string(s):
    score = 0
    for char in s:
        score += letter_scores.get(char.lower(), 0)
    
    return score

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

    