import base64
from util.hamming import hamming_distance
from util.score import score_string
from util.xor import break_single_byte_xor
from chal5 import vigenere_encrypt as vignere_decrypt

def find_likely_keysizes(ciphertext, min_size=2, max_size=40, num_blocks=4):
    distances = []
    
    for keysize in range(min_size, max_size):
        total_distance = 0
        for i in range(num_blocks - 1):
            block1 = ciphertext[i*keysize:(i+1)*keysize]
            block2 = ciphertext[(i+1)*keysize:(i+2)*keysize]
            total_distance += hamming_distance(block1, block2)
        
        normalized = (total_distance / (num_blocks - 1)) / keysize
        distances.append((normalized, keysize))
    
    return [keysize for _, keysize in sorted(distances)[:5]]

def break_repeating_key_xor(ciphertext):
    likely_keysizes = find_likely_keysizes(ciphertext)
    
    candidates = []
    for keysize in likely_keysizes:
        blocks = [ciphertext[i::keysize] for i in range(keysize)]
        
        key = b""
        for block in blocks:
            key_byte, _, _ = break_single_byte_xor(bytes(block))
            key += bytes([key_byte])
        
        plaintext = vignere_decrypt(ciphertext, key)
        try:
            plaintext_str = plaintext.decode()
            score = score_string(plaintext_str)
            candidates.append((key, plaintext_str, score))
        except UnicodeDecodeError:
            continue
    
    return max(candidates, key=lambda c: c[2])

if __name__ == "__main__":
    with open("data/6.txt", "r") as f:
        ciphertext_bytes = base64.b64decode(f.read().replace("\n", ""))
    
    assert hamming_distance(b"this is a test", b"wokka wokka!!!") == 37
    
    key, plaintext, _ = break_repeating_key_xor(ciphertext_bytes)
    
    print("The key is:", key.decode())
    print("The plaintext is:\n", plaintext, sep="")