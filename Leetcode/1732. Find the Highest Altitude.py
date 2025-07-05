class Solution:
    def largestAltitude(self, gain):
        alt = 0
        max_alt = 0
        for g in gain:
            alt += g
            max_alt = max(max_alt, alt)
        return max_alt
