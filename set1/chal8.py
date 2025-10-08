with open("data/8.txt", "r") as file:
    ciphertexts = file.read().split('\n')[:-1]

for ind,ciphertext in enumerate(ciphertexts):
    groups = [ciphertext[i:i+32] for i in range(0,len(ciphertext),32)]
    if len(groups) != len(list(set(groups))):
        print("ECB detected on line", ind+1)