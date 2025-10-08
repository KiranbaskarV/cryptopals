from Crypto.Cipher import AES
import base64

key = b"YELLOW SUBMARINE"

with open("data/7.txt", "r") as file:
    ciphertext_bytes = base64.b64decode(file.read().replace('\n', ''))

cipher = AES.new(key, AES.MODE_ECB)

print(cipher.decrypt(ciphertext_bytes).decode())