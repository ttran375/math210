# Lab - Bonus Assignment – Cryptography

## 1. Use Scilab and the encoding matrix below to decode the following message

**Encoded message:**

    9, 0, 36, 24, 37, 42, 11, 0, 36, 24, 41, 54, 17, 18, 51, 54, 5, 0, 9, 0, 27, 39

**Encoding matrix:**

$$
B = \begin{bmatrix}
1 & 0 \\
2 & 3
\end{bmatrix}
$$

``` python
import numpy as np

# Encoded message
encoded_message = [9, 0, 36, 24, 37, 42, 11, 0, 36, 24, 41, 54, 17, 18, 51, 54, 5, 0, 9, 0, 27, 39]

# Encoding matrix B
B = np.array([[1, 0], [2, 3]])

# Inverse of the encoding matrix B
B_inv = np.linalg.inv(B)

# Reshape the encoded message into pairs
encoded_pairs = np.array(encoded_message).reshape(-1, 2)

# Decode the message
decoded_pairs = np.dot(encoded_pairs, B_inv).astype(int)

# Flatten the decoded pairs
decoded_numbers = decoded_pairs.flatten()

# Encoding key
encoding_key = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N',
    15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z', 27: '!',
    28: '?', 29: '.'
}

# Decode the numbers to characters
decoded_message = ''.join([encoding_key[num] for num in decoded_numbers if num in encoding_key])

print("Decoded message:", decoded_message)
```

    ## Decoded message: ITHINKTHEREFOREIAM
