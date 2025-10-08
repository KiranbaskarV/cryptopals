plaintext = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

ciphertext = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""

key = b"ICE"

def vigenere_encrypt(message_bytes, key):
    return bytes(message_bytes[i] ^ key[i % len(key)] for i in range(len(message_bytes)))

if __name__ == "__main__":
    if vigenere_encrypt(plaintext.encode(), key).hex() == ciphertext:
        print("Passed")
    else:
        print("Failed")