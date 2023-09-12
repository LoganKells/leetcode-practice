import pytest


class Solution:

    def abs_difference(self, s: str) -> int:
        vowels = ("a", "e", "i", "o", "u")

        # Count number of vowels and consonants in s, then take the absolute difference
        count_vowels = 0
        for c in s:
            if c in vowels:
                count_vowels += 1
        count_cons = len(s) - count_vowels

        # Return the absolute difference between the count of vowels and count of consonants for the given string.
        return abs(count_cons - count_vowels)

    def get_imbalance(self, s: str) -> int:
        # Base case
        if s == "":
            return 0
        if len(s) == 1:
            return 1

        # Recursively calculate the absolute difference of the left and right halves of a string
        idx_midpoint = len(s) // 2
        s_left, s_right = s[:idx_midpoint], s[idx_midpoint:]
        imbalance_left = self.get_imbalance(s=s_left)
        imbalance_right = self.get_imbalance(s=s_right)

        # Return the total imbalance, for a given string or sub-string, = abs_diff + imbalance left + imbalance right
        return self.abs_difference(s=s) + imbalance_left + imbalance_right


test_cases = [("sample", 10)]


@pytest.mark.parametrize("s, expected", test_cases)
def test_imbalance(s, expected):
    sol = Solution()
    imbalance = sol.get_imbalance(s=s)

    assert imbalance == expected
