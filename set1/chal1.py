hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base64_ans = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

import base64

conversion = base64.b64encode(bytes.fromhex(hex_string)).decode()

if conversion == base64_ans:
    print("Passed")
else:
    print("Fail")