import string
import pytest

# 125. Valid Palindrome
# See - https://leetcode.com/problems/valid-palindrome/

class SolutionSlow:
    def isPalindrome(self, s: str) -> bool:

        # lowercase, ascii letters only
        s = s.lower()
        for c in s:
            if c not in string.ascii_letters and c not in string.digits:
                s = s.replace(c, '')

        # reverse s to check for palindrome
        return s[::-1] == s


class SolutionFast:
    def isPalindrome(self, s: str) -> bool:
        # A palindrome has equal halves, that are reverse of each outer
        # e.g. redder -> red | der : each half of a true palindrome is the reverse of the other half.

        cursor_1, cursor_2 = 0, len(s) - 1
        cursor_2 = len(s) - 1

        while cursor_1 < cursor_2:
            # skip non alpha-numeric chars
            while cursor_1 < cursor_2 and not s[cursor_1].isalnum():
                cursor_1 += 1  # Step the cursor by 1
            while cursor_1 < cursor_2 and not s[cursor_2].isalnum():
                cursor_2 -= 1  # Step the cursor by 1

            # Check if both cursors on either side are equivalent
            if s[cursor_1].lower() != s[cursor_2].lower():
                return False

            # Step the cursor by 1
            cursor_1 += 1
            cursor_2 -= 1
        return True


test_cases = [("0P", False), ("a", True), ("A man, a plan, a canal: Panama", True), ("race a car", False)]


@pytest.mark.parametrize("s, expected", test_cases)
def test_valid_palindrome_slow(s, expected):
    sol = SolutionSlow()
    is_palindrome = sol.isPalindrome(s=s)
    assert is_palindrome == expected


@pytest.mark.parametrize("s, expected", test_cases)
def test_valid_palindrome_fast(s, expected):
    sol = SolutionFast()
    is_palindrome = sol.isPalindrome(s=s)
    assert is_palindrome == expected

