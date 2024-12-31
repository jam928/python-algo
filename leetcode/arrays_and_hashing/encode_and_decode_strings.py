from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded_parts = [f"{len(s)}?{s}" for s in strs]
        return ''.join(encoded_parts)

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []

        while i < len(s):
            # find the seperator ?
            seperator_idx = s.index('?', i)
            length = int(s[i:seperator_idx])  # extract the length
            i = seperator_idx + 1  # move to the start of the string
            decoded.append(s[i:length + i])  # extract the string
            i += length  # move past the extracted string

        return decoded

# Example usage:
codec = Codec()

# Encode a list of strings
original_strings = ['7#apple', '15#banana|split', 'cherry']
encoded_string = codec.encode(original_strings)

print("Encoded String:", encoded_string)

# Decode the encoded string back to the original list of strings
decoded_strings = codec.decode(encoded_string)

print("Decoded Strings:", decoded_strings)
