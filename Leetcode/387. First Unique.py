class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = dict()  # Initialize an empty dictionary to store the count of each character

        # Step 1: Count the occurrence of each character
        for i in s:
            if i in lookup:
                lookup[i] += 1  # If the character is already in the dictionary, increment the count
            else:
                lookup[i] = 1  # If the character appears for the first time, initialize the count to 1

        # Step 2: Find the first non-repeating character
        for i, c in enumerate(s):  # Use enumerate to get the character and its index
            if lookup[c] == 1:  # If the character appears only once
                return i  # Return the index of that character

        return -1  # If no non-repeating character is found, return -1

s = Solution()
print(s.firstUniqChar("loveleetcode"))
