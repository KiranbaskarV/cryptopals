plaintext = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

ciphertext = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""

key = "ICE"

def vigenere_encrypt(plaintext_bytes, key):
    ciphertext = b""

    for i in range(len(plaintext_bytes)):
        ciphertext += (ord(key[i % len(key)]) ^ plaintext_bytes[i]).to_bytes(1,"big")

    return ciphertext.hex()

if vigenere_encrypt(plaintext.encode(), key) == ciphertext:
    print("Passed")
else:
    print("Failed")