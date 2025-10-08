from util.score import score_string

def single_byte_xor(data, key_byte):
    return bytes(b ^ key_byte for b in data)

def break_single_byte_xor(ciphertext_bytes):
    max_score = 0
    max_score_byte = None
    decrypted_string = ""
    
    for byte in range(256):
        decryption_guess = single_byte_xor(ciphertext_bytes, byte)
        try:
            plaintext = decryption_guess.decode()
            score = score_string(plaintext)
            if score > max_score:
                max_score = score
                max_score_byte = byte
                decrypted_string = plaintext
        except UnicodeDecodeError:
            continue
    
    return max_score_byte, decrypted_string, max_score