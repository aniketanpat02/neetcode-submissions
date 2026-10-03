class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""

        for i in strs:
            encode_str += f"@{len(i)}#{i}"

        return encode_str

    def decode(self, s: str) -> List[str]:
        actual = []
        index = 0

        while index < len(s):

            if s[index] == '@':
                index += 1

                length_str = ""

                # Read length
                while s[index] != '#':
                    length_str += s[index]
                    index += 1

                length = int(length_str)

                # Move past '#'
                index += 1

                # Read actual string
                start = index
                end = start + length

                actual.append(s[start:end])

                index = end

        return actual