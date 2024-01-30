from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

# Example usage:
codec = Codec()

# Encode a list of strings
original_strings = ['7#apple', '15#banana|split', 'cherry']
encoded_string = codec.encode(original_strings)

print("Encoded String:", encoded_string)

# Decode the encoded string back to the original list of strings
decoded_strings = codec.decode(encoded_string)

print("Decoded Strings:", decoded_strings)
