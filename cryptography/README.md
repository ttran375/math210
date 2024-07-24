# Lab - Bonus Assignment – Cryptography

``` python
import numpy as np

def decode_message(encoded_message, encoding_matrix, group_size):
    # Calculate the inverse of the encoding matrix
    encoding_matrix_inv = np.linalg.inv(encoding_matrix)

    # Reshape the encoded message into groups
    encoded_groups = np.array(encoded_message).reshape(-1, group_size)

    # Decode the message
    decoded_groups = np.dot(encoded_groups, encoding_matrix_inv).astype(int)

    # Flatten the decoded groups
    decoded_numbers = decoded_groups.flatten()

    # Encoding key
    encoding_key = {
        0: ' ', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 
        13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 
        25: 'Y', 26: 'Z', 27: '!', 28: '?', 29: '.'
    }

    # Decode the numbers to characters
    decoded_message = ''.join([encoding_key[num] for num in decoded_numbers if num in encoding_key])

    return decoded_message
```

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

$$ B = \begin{bmatrix} 1 & 0 \\
2 & 3 \end{bmatrix} $$

$$ \text{det}(B) = (1 \times 3) - (0 \times 2) = 3 $$

$$ B^{-1} = \frac{1}{\text{det}(B)} \cdot \text{adj}(B) $$

$$ \text{adj}(B) = \begin{bmatrix} 3 & 0 \\
-2 & 1 \end{bmatrix} $$

$$ B^{-1} = \frac{1}{3} \begin{bmatrix} 3 & 0 \\
-2 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\
-\frac{2}{3} & \frac{1}{3} \end{bmatrix} $$

$$ \begin{bmatrix} 9 & 0 \\
36 & 24 \\
37 & 42 \\
11 & 0 \\
36 & 24 \\
41 & 54 \\
17 & 18 \\
51 & 54 \\
5 & 0 \\
9 & 0 \\
27 & 39 \end{bmatrix} \times \begin{bmatrix} 1 & 0 \\
-\frac{2}{3} & \frac{1}{3} \end{bmatrix} = \begin{bmatrix} 9 & 0 \\
20 & 8 \\
9 & 14 \\
11 & 0 \\
20 & 8 \\
5 & 18 \\
5 & 6 \\
15 & 18 \\
5 & 0 \\
9 & 0 \\
1 & 13 \end{bmatrix} $$

The decoded message is:

**I THINK THEREFORE I AM**

``` python
# Question 1
encoded_message_q1 = [9, 0, 36, 24, 37, 42, 11, 0, 36, 24, 41, 54, 17, 18, 51, 54, 5, 0, 9, 0, 27, 39]
encoding_matrix_q1 = np.array([[1, 0], [2, 3]])
group_size_q1 = 2

decoded_message_q1 = decode_message(encoded_message_q1, encoding_matrix_q1, group_size_q1)
print("Decoded message for Question 1:", decoded_message_q1)
```

    ## Decoded message for Question 1: I THINK THEREFORE I AM

## 2. Use Scilab and the encoding matrix below to decode the following message

**Encoded message:**

    45, 22, -11, 31, 5, -6, 5, 9, 9, -2, 0, 3, 25, 25, 0

**Encoding matrix:**

$$
B =
\begin{bmatrix}
1 & 1 & 0 \\
-1 & 0 & 1 \\
2 & 0 & -1
\end{bmatrix}
$$

``` python
# Question 2
encoded_message_q2 = [45, 22, -11, 31, 5, -6, 5, 9, 9, -2, 0, 3, 25, 25, 0]
encoding_matrix_q2 = np.array([[1, 1, 0], [-1, 0, 1], [2, 0, -1]])
group_size_q2 = 3

decoded_message_q2 = decode_message(encoded_message_q2, encoding_matrix_q2, group_size_q2)
print("Decoded message for Question 2:", decoded_message_q2)
```

    ## Decoded message for Question 2: VALENTINE DAY

## Use this encoding key

|     | A   | B   | C   | D   | E   | F   | G   | H   | I   | J   | K   | L   | M   | N   |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  |

| O   | P   | Q   | R   | S   | T   | U   | V   | W   | X   | Y   | Z   | !   | ?   | .   |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 15  | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24  | 25  | 26  | 27  | 28  | 29  |
