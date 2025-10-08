def hamming_distance(str1, str2):
    assert(len(str1) == len(str2))

    str1_bits = ''.join(f"{x:08b}" for x in str1)
    str2_bits = ''.join(f"{x:08b}" for x in str2)

    dist = 0
    for i in range(len(str1_bits)):
        if str1_bits[i] != str2_bits[i]:
            dist += 1
    
    return dist

